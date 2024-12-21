import pandas as pd
import shutil
import os

# Read the CSV file
file_path_1 = 'C:\\Users\\rajesh.mishra\\Downloads\\FRAUDRA_TIMESHEET_DETAILS_report.csv'
file_path_2 = 'C:\\Users\\rajesh.mishra\\Downloads\\PROJECT_CODES_TOTAL_EFFORT_report.csv'
file_path_3 = 'C:\\Users\\rajesh.mishra\\Downloads\\RAJESH_TEAM_TIMESHEET_DETAILS_report.csv'
file_path_4 = 'C:\\Users\\rajesh.mishra\\Downloads\\SXM_TIMESHEET_DETAILS_report.csv'

data1 = pd.read_csv(file_path_1)
data2 = pd.read_csv(file_path_2)
data3 = pd.read_csv(file_path_3)
data4 = pd.read_csv(file_path_4)
print(data1)

# Remove the first and last rows
#data1 = data1.iloc[1:-1]
#data2 = data2.iloc[1:-1]
#data3 = data3.iloc[1:-1]
#data4 = data4.iloc[1:-1]

# Save modified data as Excel file
#output_path1 = 'C:\\WorkingDir\\Training\\AIMA\\Tableau\\datafiles\\FRAUDRA_TIMESHEET_DETAILS_report.xlsx'
#data1.to_excel(output_path1, index=False, header=True)

#output_path2 = 'C:\\WorkingDir\\Training\\AIMA\\Tableau\\datafiles\\PROJECT_CODES_TOTAL_EFFORT_report.xlsx'
#data2.to_excel(output_path2, index=False)

#output_path3 = 'C:\\WorkingDir\\Training\\AIMA\\Tableau\\datafiles\\RAJESH_TEAM_TIMESHEET_DETAILS_report.xlsx'
#data3.to_excel(output_path3, index=False)

#output_path4 = 'C:\\WorkingDir\\Training\\AIMA\\Tableau\\datafiles\\SXM_TIMESHEET_DETAILS_report.xlsx'
#data3.to_excel(output_path4, index=False)

# Move the file to another directory
#destination_directory = 'path/to/destination/directory'
#shutil.move(output_path, os.path.join(destination_directory, 'modified_data.xlsx'))
