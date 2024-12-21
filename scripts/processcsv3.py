import csv

def parse_csv(file_path):
    """
    Parse CSV file and return a list of dictionaries representing each row.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def transform_data(data):
    """
    Apply transformation logic to the parsed data.
    In this example, we convert the 'age' column to integers.
    """
    for row in data:
        row['age'] = int(row['age'])
    return data

def load_data(data):
    """
    Perform any necessary actions to load the transformed data.
    In this example, we print the transformed data.
    """
    for row in data:
        print(row)

# Example usage
file_path = 'example.csv'

# Parse CSV
parsed_data = parse_csv(file_path)

# Transform data
transformed_data = transform_data(parsed_data)

# Load data
load_data(transformed_data)
