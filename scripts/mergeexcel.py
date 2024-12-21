import pandas as pd
import os

# Function to merge Excel files from a directory
def merge_excel_files(directory, output_file):
    # Get list of Excel files in the directory
    excel_files = [file for file in os.listdir(directory) if file.endswith('.xlsx')]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each Excel file and read data into a DataFrame
    for file in excel_files:
        file_path = os.path.join(directory, file)
        # Read Excel file into a DataFrame
        data = pd.read_excel(file_path)
        # Append DataFrame to the list
        dfs.append(data)

    # Concatenate all DataFrames into one
    merged_data = pd.concat(dfs, ignore_index=True)

    # Write merged data to a new Excel file
    merged_data.to_excel(output_file, index=False)
    print("Merged Excel files saved to", output_file)

# Directory containing Excel files
directory = 'C:\\WorkingDir\\Projects\\ACTIVE\\SXM\\BIOPS\\Fortnightly-MonthlyReport\\2024\\April'
# Output file name for merged Excel file
output_file = 'C:\\WorkingDir\\Projects\\ACTIVE\\SXM\\BIOPS\\Fortnightly-MonthlyReport\\2024\\merged_data.xlsx'

# Call the function to merge Excel files
merge_excel_files(directory, output_file)

