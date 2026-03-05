import pandas as pd

# Load dataset
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

# ------------------------
# 1. Handle missing values
# ------------------------
df['Mental_Health_Condition'] = df['Mental_Health_Condition'].fillna('Unknown')
df['Physical_Activity'] = df['Physical_Activity'].fillna('Unknown')

# ------------------------
# 2. Handle default/placeholder values
# ------------------------
default_placeholders = ['NA', 'N/A', '-', 'None', 'null', 'NaN']
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].replace(default_placeholders, 'Unknown')

# ------------------------
# 3. Remove duplicate rows
# ------------------------
df = df.drop_duplicates()

# ------------------------
# 4. Handle incorrect values
# ------------------------
# For Number_of_Virtual_Meetings, 0 is considered valid but flagged
if 'Number_of_Virtual_Meetings' in df.columns:
    df['Virtual_Meetings_Flag'] = df['Number_of_Virtual_Meetings'].apply(lambda x: 1 if x == 0 else 0)

# ------------------------
# 5. Standardise inconsistent values
# ------------------------
# Ensure consistent capitalisation for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].str.strip().str.capitalize()

# ------------------------
# 6. Optional: Check numeric ranges and flag outliers
# ------------------------
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    min_val, max_val = df[col].min(), df[col].max()
    print(f"{col}: min={min_val}, max={max_val}")

# ------------------------
# 7. Save cleaned dataset
# ------------------------
df.to_csv("Impact_of_Remote_Work_Cleaned.csv", index=False)
print("Dataset is now cleaned and ready for analysis.")

