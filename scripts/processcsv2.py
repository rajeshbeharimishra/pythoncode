import os
import csv
import datetime
import logging
import cx_Oracle

# Set up logging
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

# Oracle connection details
oracle_username = 'your_username'
oracle_password = 'your_password'
oracle_host = 'localhost'
oracle_port = '1521'
oracle_service = 'your_oracle_service'

# Directory paths
data_directory = '/path/to/csv/files'
bak_directory = '/path/to/bak/files'

# Oracle table name
oracle_table = 'your_table'

# Summary table name
summary_table = 'your_summary_table'


def process_csv_file(file_path):
    try:
        # Check if corresponding bak file exists
        bak_file_path = os.path.join(bak_directory, os.path.basename(file_path) + '.bak')
        if os.path.exists(bak_file_path):
            raise Exception('Bak file already exists')

        # Read CSV file
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Assuming the first row is the header

            # Connect to Oracle database
            oracle_connection = cx_Oracle.connect(
                f"{oracle_username}/{oracle_password}@{oracle_host}:{oracle_port}/{oracle_service}")
            cursor = oracle_connection.cursor()

            batch_size = 1000
            rows = []
            count = 0

            # Process each row and apply transformations
            for row in csv_reader:
                transformed_row = transform_row(row)  # Apply your transformations here

                # Add transformed row to the batch
                rows.append(transformed_row)
                count += 1

                # Load the batch into Oracle table
                if count % batch_size == 0:
                    cursor.executemany(f"INSERT INTO {oracle_table} VALUES (:1, :2, :3)",
                                       rows)  # Modify the query and bind parameters based on your table structure
                    rows = []

            # Load any remaining rows
            cursor.executemany(f"INSERT INTO {oracle_table} VALUES (:1, :2, :3)", rows)

            # Record summary in summary table
            summary_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(f"INSERT INTO {summary_table} VALUES (:1, :2)", (file_path, summary_date))

            # Create bak file
            with open(bak_file_path, 'w'):
                pass

            # Commit changes and close connection
            oracle_connection.commit()
            cursor.close()
            oracle_connection.close()

    except Exception as e:
        logging.exception(f"Error processing file: {file_path}")


def transform_row(row):
    # Apply your custom transformations on each field of the row
    transformed_row = []
    for field in row:
        # Transformation logic
        transformed_field = field  # Placeholder logic, replace it with your actual transformation
        transformed_row.append(transformed_field)
    return transformed_row


def main():
    try:
        # Read the files in the directory
        for file_name in os.listdir(data_directory):
            if file_name.endswith('.csv'):
                file_path = os.path.join(data_directory, file_name)
                process_csv_file(file_path)
            else:
                logging.warning(f"Ignoring non-CSV file: {file_name}")

    except Exception as e:
        logging.exception('An error occurred while processing files.')


if __name__ == '__main__':
    main()
