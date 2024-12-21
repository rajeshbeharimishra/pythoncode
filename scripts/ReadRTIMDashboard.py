import os
import pandas as pd

def read_excel_files(folder_path, sheet_name):
    # List all files in the specified folder
    files = os.listdir(folder_path)
    
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
                if len(df) > 7:
                    print("A8:", df.iloc[6, 0])
                    print("B8:", df.iloc[6, 1])
                    print("C8:", df.iloc[6, 2])
                    print("D8:", df.iloc[6, 3])
                else:
                    print("The worksheet has less than 8 rows.")
                print()
                
            except Exception as e:
                print(f"Error reading file {file}: {e}")

# Specify the folder containing Excel files
folder_path = 'C:\\Users\\rajesh.mishra\\Desktop\\RTIM Dashboard\\January'
# Specify the worksheet name
sheet_name = 'RTIM-DISP-SPS Counts'  # Change 'Sheet1' to the desired sheet name

# Call the function to read Excel files
read_excel_files(folder_path, sheet_name)

