import psycopg2

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Admin@123",
        host="localhost",
        port="5432"
    )