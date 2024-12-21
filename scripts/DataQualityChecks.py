import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample Data
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, np.nan],
    'Age': [25, 35, 50, 28, np.nan, 45, 60, 30, 40, 35],
    'Salary': [50000, 60000, 75000, np.nan, 40000, 100000, 110000, 48000, 70000, 62000],
    'Email': ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com', 'e@e.com', 'f@f.com', 'g@c.com', 'h@h.com', 'i@i.com', 'i@i.com']
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

### Step 1: Data Quality Checks ###

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
    actual_types = df.dtypes
    type_issues = actual_types[actual_types != expected_types]
    return type_issues

### Step 2: Generate Data Quality Report ###

def data_quality_report(df):
    report = {}
    
    # Missing Value Check
    missing_percent = missing_values_check(df)
    report['MissingValues'] = missing_percent
    
    # Outlier Detection
    report['Outliers'] = {col: detect_outliers(df, col) for col in df.select_dtypes(include=[np.number]).columns}
    
    # Duplicate Check
    report['Duplicates'] = check_duplicates(df)
    
    # Data Type Validation
    expected_types = pd.Series({
        'ID': 'float64',
        'Age': 'float64',
        'Salary': 'float64',
        'Email': 'object'
    })
    report['TypeIssues'] = validate_data_types(df, expected_types)
    
    return report

# Run the data quality report
dq_report = data_quality_report(df)
print("Data Quality Report:")
print(dq_report)

### Step 3: Data Quality Scoring ###
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

# Calculate data quality score
dq_score = data_quality_score(df, dq_report)
print(f"Data Quality Score: {dq_score:.2f}%")

### Step 4: Machine Learning Model (Optional - Random Forest for Classification) ###
# Example: Use the data for a prediction task if required

# Simulate a target column for prediction
df['Target'] = np.random.choice([0, 1], size=len(df))

# Splitting the data into train/test
X = df[['Age', 'Salary']].fillna(df[['Age', 'Salary']].mean())  # Handle missing values for ML
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Make predictions and calculate accuracy
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy: {accuracy:.2f}")

