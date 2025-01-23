from flask import Flask, request, jsonify
from config import get_db_connection

app = Flask(__name__)

# Test route to check API is running
@app.route('/')
def home():
    return jsonify({"message": "API is running!"})

# Endpoint for user matching
@app.route('/match', methods=['POST'])
def match_users():
    # Get the input data from the request
    data = request.json
    req_name = data.get('name', None)
    req_phone = data.get('phone', None)
    req_email = data.get('email', None)
    req_address = data.get('address', None)
    req_city = data.get('city', None)
    req_state = data.get('state', None)
    req_zip = data.get('zip', None)
    req_dob = data.get('date_of_birth', None)
    req_id_type = data.get('id_type', None)
    req_id_value = data.get('id_value', None)

    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Call the stored function
        cursor.execute("""
            SELECT * FROM getMatchSummaryNew(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (req_name, req_phone, req_email, req_address, req_city, req_state, req_zip, req_dob, req_id_type, req_id_value))

        # Fetch the results
        results = cursor.fetchall()

        # Format the response
        response = []
        for row in results:
            response.append({
                "user_id": row[0],
                "name_score": round(row[1], 2),
                "phone_score": round(row[2], 2),
                "email_score": round(row[3], 2),
                "address_score": round(row[4], 2),
                "dob_score": round(row[5], 2),
                "id_score": round(row[6], 2) if row[6] is not None else None
            })

        cursor.close()
        conn.close()

        # Return the response as JSON
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/match-details/<int:request_id>', methods=['GET'])
def get_match_details(request_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM getMatchDetails(%s)", (request_id,))
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        # Format the results as a list of dictionaries
        response = [dict(zip(columns, row)) for row in results]
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True)