import os
import csv
import datetime
import shutil
import logging
import cx_Oracle

# Configure logging
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Set directory paths
csv_directory = '/path/to/csv/directory'
bak_directory = '/path/to/bak/directory'

# Oracle database information
oracle_username = 'your_username'
oracle_password = 'your_password'
oracle_host = 'your_host'
oracle_port = 'your_port'
oracle_service = 'your_service_name'

def create_backup_file(filename):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    bak_filename = os.path.splitext(filename)[0] + '.bak_' + timestamp
    shutil.copy2(filename, os.path.join(bak_directory, bak_filename))

def process_csv(filename):
    try:
        bak_filename = os.path.splitext(filename)[0] + '.bak'
        if not os.path.exists(os.path.join(csv_directory, bak_filename)):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                for row in reader:
                    # Apply transformation on fields (sample operation)
                    transformed_row = [field.upper() for field in row]
                    
                    # Load into Oracle database table
                    oracle_connection = cx_Oracle.connect(oracle_username, oracle_password, oracle_host+':'+oracle_port+'/'+oracle_service)
                    cursor = oracle_connection.cursor()
                    cursor.execute("INSERT INTO your_table_name VALUES (:1, :2, :3)", transformed_row)
                    cursor.close()
                    oracle_connection.commit()
                    oracle_connection.close()
                    
            # Record summary in summary table
            summary_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            oracle_connection = cx_Oracle.connect(oracle_username, oracle_password, oracle_host+':'+oracle_port+'/'+oracle_service)
            cursor = oracle_connection.cursor()
            cursor.execute("INSERT INTO summary_table (timestamp, filename) VALUES (:1, :2)", (summary_timestamp, filename))
            cursor.close()
            oracle_connection.commit()
            oracle_connection.close()

            # Create backup file
            create_backup_file(filename)
            
    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    try:
        # Read directory and process CSV files
        for file in os.listdir(csv_directory):
            if file.endswith('.csv'):
                process_csv(os.path.join(csv_directory, file))
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    main()