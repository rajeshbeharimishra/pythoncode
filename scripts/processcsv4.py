import os
import pandas as pd
import cx_Oracle
import logging
from datetime import datetime

# Set up logging
log_filename = 'logfile.log'
logging.basicConfig(filename=log_filename, level=logging.INFO)

def read_csv_apply_transform(csv_path):
    try:
        df = pd.read_csv(csv_path)

        # Apply your transformations on the DataFrame
        # For example, you can add a new column or modify existing ones
        # df['new_column'] = df['existing_column'].apply(your_transformation_function)

        return df
    except Exception as e:
        logging.error(f"Error reading or transforming CSV file {csv_path}: {str(e)}")
        return None

def write_to_oracle(df, table_name, batch_size=1000):
    try:
        conn = cx_Oracle.connect('your_oracle_connection_string')
        cursor = conn.cursor()

        # Assuming 'your_oracle_connection_string' is in the format: 'username/password@hostname:port/service_name'

        for i in range(0, len(df), batch_size):
            batch_df = df.iloc[i:i+batch_size]
            records = batch_df.to_dict(orient='records')

            cursor.executemany(f"INSERT INTO {table_name} VALUES (:1, :2, :3, ...)", records)
            conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        logging.error(f"Error writing to Oracle table {table_name}: {str(e)}")

def main():
    input_directory = 'input_directory'
    bak_directory = 'bak_directory'
    summary_table = 'summary_table'
    oracle_table = 'your_oracle_table'

    if not os.path.exists(bak_directory):
        os.makedirs(bak_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            csv_path = os.path.join(input_directory, filename)
            bak_path = os.path.join(bak_directory, f"{os.path.splitext(filename)[0]}.bak")

            if not os.path.exists(bak_path):
                try:
                    # Read and transform CSV
                    df = read_csv_apply_transform(csv_path)

                    if df is not None:
                        # Write to Oracle in batches
                        write_to_oracle(df, oracle_table)

                        # Record summary in summary table
                        summary_record = {'filename': filename, 'processed_at': datetime.now()}
                        summary_df = pd.DataFrame([summary_record])
                        write_to_oracle(summary_df, summary_table)

                        # Create a backup file
                        df.to_csv(bak_path, index=False)

                except Exception as e:
                    logging.error(f"Error processing file {filename}: {str(e)}")

if __name__ == "__main__":
    main()
