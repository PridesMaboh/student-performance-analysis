from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

# Load the CSV
df = pd.read_csv(DATA / "raw_student_data.csv", encoding="latin1")

# Show original columns
print("Original columns:", df.columns)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Cleaned columns:", df.columns)

# Convert numeric columns
numeric_cols = ["age", "studyhours", "python", "db"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicates
df = df.drop_duplicates()

# Clean gender
df["gender"] = df["gender"].astype(str).str.strip().str.title()
df["gender"] = df["gender"].replace({
    "F": "Female",
    "M": "Male"
})

# Clean previous education
df["preveducation"] = df["preveducation"].astype(str).str.strip().str.title()

df["preveducation"] = df["preveducation"].replace({
    "Highschool": "High School",
    "High School ": "High School",
    "Highschool ": "High School",
    "Barrrchelors": "Bachelors",
    "Diplomaaa": "Diploma"
})

# Fix missing Python scores
df["python"] = df["python"].fillna(df["python"].mean())

# Final checks
print("\nUnique education values:", df["preveducation"].unique())
print("Unique gender values:", df["gender"].unique())
print("\nMissing values:\n", df.isna().sum())

# Export cleaned file
df.to_csv(DATA / "cleaned_student_data.csv", index=False)
print("\nCleaned file saved!")
numeric_cols = ["age", "studyhours", "entryexam", "python", "db"]

corr = df[numeric_cols].corr()
print("\nCorrelation Matrix:")
print(corr)
