import pandas as pd

# Load the Excel file
file_path = "C:\\Users\\rajesh.mishra\\Desktop\\Charter_Dup_Pin_21Aug2024\\Charter_Dup_Pin_21Aug2024.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Print column names to verify they are as expected
print("Columns in the DataFrame:", df.columns)

# Create a new column that concatenates columns E and F with a space
df['CTND'] = df['CUST_FNAME'] + " " + df['CUST_LNAME']

# Verify the 'Concatenated' column creation
print("First few rows after creating 'CTND' column:")
print(df[['CUST_FNAME', 'CUST_LNAME', 'CTND']].head())

# Define a function to check if all concatenated values are the same for each group
def check_same(group):
    if group['CTND'].nunique() == 1:
        return 'SAME'
    else:
        return 'NOT SAME'

# Apply the function to each group defined by the unique values in column C
df['Result'] = df.groupby('SPARE_4')['CTND'].transform(check_same)

# Save the result back to a new Excel file
output_file_path = "C:\\Users\\rajesh.mishra\\Desktop\\Charter_Dup_Pin_21Aug2024\\output_with_results.xlsx"
df.to_excel(output_file_path, index=False)

print("Result saved to:", output_file_path)
