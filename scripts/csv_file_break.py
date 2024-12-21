import os
import csv

# Configuration
input_filename = '2023_10222023_BillerSrcData_2.csv'
output_folder = 'output'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the input file and read the header
with open(input_filename, 'r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    # Iterate over the remaining rows
    file_index = 1
    rows_per_file = 50000  # Number of rows per file

    for i, row in enumerate(reader, start=1):
        # Calculate the file index based on the row number
        if i % rows_per_file == 1:
            output_filename = os.path.join(output_folder, f'output_{file_index}.csv')
            file_index += 1

            # Create a new file and write the header
            with open(output_filename, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
            # Write the current row to the file
                writer.writerow(row)
        else:
            # Append the row to the current file
            with open(output_filename, 'a', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(row)