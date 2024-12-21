import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load Data from CSV
def load_data(file_path):
    """
    Loads data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: pandas DataFrame with the loaded data.
    """
    df = pd.read_csv(file_path)
    return df

# Step 2: Data Quality Checks

# 1. Missing Values Check
def missing_values_check(df):
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    return missing_percent

# 2. Outlier Detection (Using Z-Score)
def detect_outliers(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    outliers = df[np.abs((df[column] - mean) / std) > threshold]
    return len(outliers)

# 3. Duplicates Check
def check_duplicates(df):
    return df.duplicated().sum()

# 4. Data Type Validation

def validate_data_types(df, expected_types):
    common_columns = expected_types.index.intersection(df.columns)
    actual_types = df[common_columns].dtypes
    type_issues = actual_types[actual_types != expected_types[common_columns]]
    return type_issues

# Email Validation
def validate_emails(df, email_column='email'):
    """
    Checks for invalid email addresses.
    :param df: pandas DataFrame containing the data.
    :param email_column: The column in the DataFrame that contains email addresses.
    :return: A Series of rows with invalid emails.
    """
    if email_column in df.columns:
        # Convert the column to string and fill NaN with empty strings
        email_series = df[email_column].astype(str).fillna('')
        
        # Regular expression to match a valid email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Find invalid emails
        invalid_emails = email_series[~email_series.str.match(email_pattern)]
        return invalid_emails
    else:
        return pd.Series([], dtype="object")  # Return empty if the column is missing

# ZIP Code Validation
def validate_zip_codes(df, zip_column='zip'):
    """
    Checks for invalid ZIP codes.
    :param df: pandas DataFrame containing the data.
    :param zip_column: The column in the DataFrame that contains ZIP codes.
    :return: A Series of rows with invalid ZIP codes.
    """
    if zip_column in df.columns:
        # Convert the column to string and fill NaN with empty strings
        zip_series = df[zip_column].astype(str).fillna('')
        
        # Regular expression to match 5-digit or 9-digit ZIP codes
        zip_pattern = r'^\d{5}(-\d{4})?$'
        
        # Find invalid ZIP codes
        invalid_zips = zip_series[~zip_series.str.match(zip_pattern)]
        return invalid_zips
    else:
        return pd.Series([], dtype="object")  # Return empty if the column is missing


# Step 3: Generate Data Quality Report

def data_quality_report(df):
    report = {}
    
    # Missing Value Check
    missing_percent = missing_values_check(df)
    report['MissingValues'] = missing_percent
    
    # Outlier Detection (for numerical columns)
    report['Outliers'] = {col: detect_outliers(df, col) for col in df.select_dtypes(include=[np.number]).columns}
    
    # Duplicate Check
    report['Duplicates'] = check_duplicates(df)
    
    # Data Type Validation (example)
    expected_types = pd.Series({
        'id': 'int64',  # Adjust according to your data
        'first_name': 'object',
        'last_name': 'object',
        'company_name': 'object',
        'address': 'object',
        'city': 'object',
        'county': 'object',
        'state': 'object',
        'zip': 'int64',
        'phone1': 'object',
        'phone2': 'object',
        'email': 'object',
        'web': 'object',
        'age': 'int64',
        'salary': 'float64'
        
    })
    report['TypeIssues'] = validate_data_types(df, expected_types)
    # Email Validation
    if 'email' in df.columns:
        report['InvalidEmails'] = validate_emails(df)
    else:
        report['InvalidEmails'] = "Email column not found."
    
    # ZIP Code Validation
    if 'zip' in df.columns:
        report['InvalidZIPCodes'] = validate_zip_codes(df)
    else:
        report['InvalidZIPCodes'] = "ZIP code column not found."
    
    return report

# Step 4: Data Quality Scoring

def data_quality_score(df, report):
    total_checks = 4  # We have 4 checks: missing, outliers, duplicates, type validation
    
    # Missing values score
    missing_score = (df.notnull().sum().sum() / df.size) * 100
    
    # Outlier score
    outliers = sum(report['Outliers'].values())
    outlier_score = ((len(df) - outliers) / len(df)) * 100
    
    # Duplicates score
    duplicate_score = ((len(df) - report['Duplicates']) / len(df)) * 100
    
    # Data type validation score
    type_issue_count = len(report['TypeIssues'])
    type_validation_score = ((len(df.columns) - type_issue_count) / len(df.columns)) * 100
    
    # Average score
    average_score = (missing_score + outlier_score + duplicate_score + type_validation_score) / total_checks
    return average_score

# Step 5: Example Machine Learning Model (Optional)

def build_and_evaluate_model(df):
    # Simulate a target column for prediction
    df['Target'] = np.random.choice([0, 1], size=len(df))

    # Handle missing values for ML and select numerical columns
    X = df[['age', 'salary']].fillna(df[['age', 'salary']].mean())  # Fill missing values
    y = df['Target']
    
    # Splitting the data into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Random Forest Classifier
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    
    # Make predictions and calculate accuracy
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Random Forest Model Accuracy: {accuracy:.2f}")
    
    return accuracy

# Main Function to Perform Data Quality Checks on a CSV File
def main(file_path):
    # Load the CSV data
    df = load_data(file_path)
    
    # Generate the data quality report
    dq_report = data_quality_report(df)
    print("Data Quality Report:")
    print(dq_report)
    
    # Calculate the data quality score
    dq_score = data_quality_score(df, dq_report)
    print(f"Data Quality Score: {dq_score:.2f}%")
    
    # Optional: Build and evaluate a model on the dataset
    model_accuracy = build_and_evaluate_model(df)
    print(f"Model Accuracy: {model_accuracy:.2f}")

# Example Usage
if __name__ == "__main__":
    # Provide the path to your CSV file
    csv_file_path = "C:\\WorkingDir\\Training\\Python\\Employee-Details.csv"
    main(csv_file_path)
