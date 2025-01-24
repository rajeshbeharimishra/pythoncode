from flask import Flask, render_template, request, make_response
from jellyfish import soundex, jaro_winkler_similarity, levenshtein_distance
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime

app = Flask(__name__)

# Function to normalize names
def normalize_name(name):
    return ' '.join(name.lower().strip().split())

# Function to calculate name similarity score
def compare_names(name1, name2):
    # Split names into components (first, middle, last)
    name1_parts = name1.split()
    name2_parts = name2.split()

    first_name1 = name1_parts[0] if len(name1_parts) > 0 else ""
    middle_name1 = name1_parts[1] if len(name1_parts) == 3 else ""
    last_name1 = name1_parts[-1] if len(name1_parts) > 1 else ""

    first_name2 = name2_parts[0] if len(name2_parts) > 0 else ""
    middle_name2 = name2_parts[1] if len(name2_parts) == 3 else ""
    last_name2 = name2_parts[-1] if len(name2_parts) > 1 else ""

    # Normalize names
    first_name1 = normalize_name(first_name1)
    middle_name1 = normalize_name(middle_name1)
    last_name1 = normalize_name(last_name1)

    first_name2 = normalize_name(first_name2)
    middle_name2 = normalize_name(middle_name2)
    last_name2 = normalize_name(last_name2)

    # Compute similarity scores
    soundex_score_first = 1 if soundex(first_name1) == soundex(first_name2) else 0
    soundex_score_last = 1 if soundex(last_name1) == soundex(last_name2) else 0
    soundex_score_middle = 1 if middle_name1 and middle_name2 and soundex(middle_name1) == soundex(middle_name2) else 0

    jaro_score_first = jaro_winkler_similarity(first_name1, first_name2)
    jaro_score_last = jaro_winkler_similarity(last_name1, last_name2)
    jaro_score_middle = jaro_winkler_similarity(middle_name1, middle_name2) if middle_name1 and middle_name2 else 0

    levenshtein_score_first = 1 - levenshtein_distance(first_name1, first_name2) / max(len(first_name1), len(first_name2)) if first_name1 and first_name2 else 0
    levenshtein_score_last = 1 - levenshtein_distance(last_name1, last_name2) / max(len(last_name1), len(last_name2)) if last_name1 and last_name2 else 0
    levenshtein_score_middle = 1 - levenshtein_distance(middle_name1, middle_name2) / max(len(middle_name1), len(middle_name2)) if middle_name1 and middle_name2 else 0

    if middle_name1 and middle_name2:
       name_score = (
            0.3 * (soundex_score_first + jaro_score_first + levenshtein_score_first) / 3 +
            0.15 * (soundex_score_middle + jaro_score_middle + levenshtein_score_middle) / 3 +
            0.55 * (soundex_score_last + jaro_score_last + levenshtein_score_last) / 3
        )
    else:
        name_score = (
            0.4 * (soundex_score_first + jaro_score_first + levenshtein_score_first) / 3 +
            0.6 * (soundex_score_last + jaro_score_last + levenshtein_score_last) / 3
        )

    return name_score

def combined_similarity(value1, value2):
    value1 = value1.strip().lower()
    value2 = value2.strip().lower()
    
    if not value1 or not value2:
        return 0.0
    
    jaro_score = jaro_winkler_similarity(value1, value2)
    levenshtein_score = 1 - levenshtein_distance(value1, value2) / max(len(value1), len(value2))
    #return (jaro_score + levenshtein_score)/2
    return (0.3*jaro_score + 0.7*levenshtein_score)

def compare_dates_of_birth(dob1, dob2):
    try:
        dob1_parsed = datetime.strptime(dob1, "%Y-%m-%d")
        dob2_parsed = datetime.strptime(dob2, "%Y-%m-%d")

        if dob1_parsed == dob2_parsed:
            return 1.0  # Exact match

        # Check for transposed month and day
        dob1_reversed = datetime(dob1_parsed.year, dob1_parsed.day, dob1_parsed.month)
        if dob1_reversed == dob2_parsed:
            return 0.8  # High confidence for transposition

        # Check year-only match
        if dob1_parsed.year == dob2_parsed.year:
            if dob1_parsed.month == dob2_parsed.month or dob1_parsed.day == dob2_parsed.day:
                return 0.6  # Partial match on year and one other component
            return 0.5  # Partial match on year only

        # Check if month and day match regardless of year
        if dob1_parsed.month == dob2_parsed.month and dob1_parsed.day == dob2_parsed.day:
            return 0.7  # Partial match on month and day

        return 0.0  # No significant match
    except ValueError:
        return 0.0

# Function to compare emails
def compare_emails(email1, email2):
    email1 = email1.strip().lower()
    email2 = email2.strip().lower()
    return 1 if email1 == email2 else jaro_winkler_similarity(email1, email2)

# Function to compare phone numbers
def compare_phone_numbers(phone1, phone2):
    phone1 = ''.join(filter(str.isdigit, phone1))  # Remove non-numeric characters
    phone2 = ''.join(filter(str.isdigit, phone2))
    return 1 if phone1 == phone2 else jaro_winkler_similarity(phone1, phone2)
    
# Function to compare addresses
def compare_addresses_advanced(addr1, city1, state1, zip1, addr2, city2, state2, zip2):
    # Compute component-wise similarity
    addr_similarity = combined_similarity(addr1, addr2)
    city_similarity = combined_similarity(city1, city2)
    state_similarity = combined_similarity(state1, state2)
    zip_similarity = 1 if zip1.strip() == zip2.strip() else combined_similarity(zip1, zip2)
    
    # Weighted average for string-based similarity
    string_similarity = (
        0.4 * addr_similarity +
        0.15 * city_similarity +
        0.15 * state_similarity +
        0.3 * zip_similarity
    )
    return string_similarity

def compare_ids(id1, id2):
    return round(combined_similarity(id1, id2) * 100, 2)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Collect form inputs
    name1 = request.form['name1']
    name2 = request.form['name2']
    dob1 = request.form['dob1']
    dob2 = request.form['dob2']
    email1 = request.form['email1']
    email2 = request.form['email2']
    phone1 = request.form['phone1']
    phone2 = request.form['phone2']
    addr1 = request.form['addr1']
    city1 = request.form['city1']
    state1 = request.form['state1']
    zip1 = request.form['zip1']
    addr2 = request.form['addr2']
    city2 = request.form['city2']
    state2 = request.form['state2']
    zip2 = request.form['zip2']
    id_type = request.form['id_type']
    id1 = request.form['id1']
    id2 = request.form['id2']
    
    # Calculate scores
    name_score = round(compare_names(name1, name2) * 100, 2)
    dob_score = round(compare_dates_of_birth(dob1, dob2) * 100, 2)
    email_score = round(compare_emails(email1, email2) * 100, 2)
    phone_score = round(compare_phone_numbers(phone1, phone2) * 100, 2)
    #addr_score = round(combined_similarity(f"{addr1}, {city1}, {state1}, {zip1}", f"{addr2}, {city2}, {state2}, {zip2}") * 100, 2)
    addr_score = round(compare_addresses_advanced(addr1, city1, state1, zip1, addr2, city2, state2, zip2) * 100, 2)
    id_score = compare_ids(id1, id2)
    
    # Pass scores to the result page
    return render_template('result.html', name_score=name_score, dob_score=dob_score,
                           email_score=email_score, phone_score=phone_score, addr_score=addr_score,id_score=id_score)


@app.after_request
def add_cache_control(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == '__main__':
    app.run(debug=True)