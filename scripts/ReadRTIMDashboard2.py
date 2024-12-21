import os
import pandas as pd

def read_excel_files(folder_path, sheet_name, output_file):
    # List all files in the specified folder
    files = os.listdir(folder_path)
    # Create an empty list to store the data
    data = []
    
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):  # Check if file is Excel file
            file_path = os.path.join(folder_path, file)
            
            # Read the Excel file
            # Read the Excel file
            try:
                # Read the specified worksheet
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Print values in columns A8, B8, C8, and D8
                print("File:", file)
                #if len(df) > 7:
                row = df.iloc[3]
                data.append([file] + row.tolist())
                #else:
                    #print("The worksheet has less than 8 rows.")
                #print()
                
            except Exception as e:
                print(f"Error reading file {file}: {e}")
    # Create a DataFrame from the collected data
    df_output = pd.DataFrame(data, columns=['File', 'A8', 'B8', 'C8', 'D8','E8','F8','G8'])

    # Write the DataFrame to an Excel file
    try:
        df_output.to_excel(output_file, index=False)
        print("Data has been written to", output_file)
    except Exception as e:
        print(f"Error writing to Excel file {output_file}: {e}")


# Specify the folder containing Excel files
folder_path = 'C:\\Users\\rajesh.mishra\\Desktop\\RTIM Dashboard\\January'
# Specify the worksheet name
sheet_name = 'RTIM-DISP-SPS Counts'  # Change 'Sheet1' to the desired sheet name

# Specify the output file
output_file = 'C:\\Users\\rajesh.mishra\\Desktop\\RTIM Dashboard\\January\\output_rtim.xlsx'

# Call the function to read Excel files
read_excel_files(folder_path, sheet_name, output_file)

