import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# LOAD DATA (WINDOWS PATH)
# ---------------------------------------------------------
df = pd.read_csv(
    r"C:\Users\frupr\OneDrive\My Portfolios\PYTHON\data\cleaned_student_data.csv"
)

# ---------------------------------------------------------
# BASIC DATA INSPECTION
# ---------------------------------------------------------
print(df.head())
print(df.info())

print("\nMissing values per column:")
print(df.isna().sum())

# ---------------------------------------------------------
# NUMERIC SUMMARY
# ---------------------------------------------------------
num_cols = ["age", "studyhours", "python", "db"]

print("\nDescriptive statistics:")
print(df[num_cols].describe())

print("\nExtended statistics:")
print(df[num_cols].agg(["mean", "median", "std", "min", "max", "skew", "kurt"]))

# ---------------------------------------------------------
# CATEGORICAL SUMMARY
# ---------------------------------------------------------
cat_cols = ["gender", "country", "residence", "preveducation"]

for col in cat_cols:
    print(f"\n=== {col} ===")
    print(df[col].value_counts())
    print("Proportions:")
    print(df[col].value_counts(normalize=True).round(3))

# ---------------------------------------------------------
# STANDARDISE COUNTRY
# ---------------------------------------------------------
country_map = {
    "Norway": "Norway",
    "norway": "Norway",
    "Norge": "Norway",
    "Rsa": "South Africa",
    "South Africa": "South Africa",
    "UK": "United Kingdom",
    "Somali": "Somalia"
}
df["country"] = df["country"].replace(country_map)

# ---------------------------------------------------------
# STANDARDISE RESIDENCE
# ---------------------------------------------------------
residence_map = {
    "BI Residence": "BI Residence",
    "BI-Residence": "BI Residence",
    "BIResidence": "BI Residence",
    "BI_Residence": "BI Residence"
}
df["residence"] = df["residence"].replace(residence_map)

print("\nCleaned COUNTRY values:")
print(df["country"].value_counts())

print("\nCleaned RESIDENCE values:")
print(df["residence"].value_counts())

# ---------------------------------------------------------
# SAVE CLEANED FILE
# ---------------------------------------------------------
df.to_csv(
    r"C:\Users\frupr\OneDrive\My Portfolios\PYTHON\data\cleaned_student_data.csv",
    index=False
)
print("\nFile saved successfully.")

# ---------------------------------------------------------
# PHASE 2: CORRELATION ANALYSIS
# ---------------------------------------------------------
numeric_cols = ["age", "studyhours", "python", "db", "entryexam"]
corr = df[numeric_cols].corr()

print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
# ---------------------------------------------------------
# PHASE 3: DISTRIBUTION ANALYSIS
# ---------------------------------------------------------

numeric_cols = ["age", "studyhours", "entryexam", "python", "db"]

for col in numeric_cols:
    plt.figure(figsize=(10, 4))

    # Histogram + KDE
    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot for outliers
    plt.figure(figsize=(8, 2))
    sns.boxplot(x=df[col], color="lightgreen")
    plt.title(f"Boxplot of {col}")
    plt.show()
    # ---------------------------------------------------------
    # PHASE 4: BIVARIATE VISUAL ANALYSIS
    # ---------------------------------------------------------

    # 1. Study Hours vs Python Score
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="studyhours", y="python", hue="gender")
    plt.title("Study Hours vs Python Score")
    plt.show()

    # 2. Study Hours vs Entry Exam
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="studyhours", y="entryexam", hue="gender")
    plt.title("Study Hours vs Entry Exam Score")
    plt.show()

    # 3. Python vs Database Score
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="python", y="db", hue="gender")
    plt.title("Python vs Database Score")
    plt.show()

    # 4. Age vs Python Score
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="age", y="python", hue="gender")
    plt.title("Age vs Python Score")
    plt.show()

    # 5. Gender vs Python Score (Boxplot)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="gender", y="python")
    plt.title("Python Score by Gender")
    plt.show()

    # 6. Residence vs Study Hours
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="residence", y="studyhours")
    plt.title("Study Hours by Residence Type")
    plt.xticks(rotation=45)
    plt.show()

    # 7. Previous Education vs Python Score
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="preveducation", y="python")
    plt.title("Python Score by Previous Education")
    plt.xticks(rotation=45)
    plt.show()
# ---------------------------------------------------------
# PHASE 5: OUTLIER DETECTION & ANALYSIS
# ---------------------------------------------------------

import numpy as np

numeric_cols = ["age", "studyhours", "entryexam", "python", "db"]

def detect_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = series[(series < lower) | (series > upper)]
    return outliers, lower, upper

print("\n=== OUTLIER ANALYSIS (IQR METHOD) ===")

for col in numeric_cols:
    outliers, lower, upper = detect_outliers_iqr(df[col])
    print(f"\n{col.upper()}:")
    print(f"Lower bound: {lower:.2f}, Upper bound: {upper:.2f}")
    print(f"Number of outliers: {len(outliers)}")
    if len(outliers) > 0:
        print("Outlier values:", list(outliers.values))

    # Visual boxplot
    plt.figure(figsize=(8, 2))
    sns.boxplot(x=df[col], color="salmon")
    plt.title(f"Outliers in {col}")
    plt.show()
# ---------------------------------------------------------
# PHASE 6: GROUPED ANALYSIS & SEGMENT INSIGHTS
# ---------------------------------------------------------

# 1. Gender vs Python Score
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="gender", y="python")
plt.title("Python Score by Gender")
plt.show()

# 2. Gender vs Entry Exam
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="gender", y="entryexam")
plt.title("Entry Exam Score by Gender")
plt.show()

# 3. Residence vs Study Hours
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="residence", y="studyhours")
plt.title("Study Hours by Residence Type")
plt.xticks(rotation=45)
plt.show()

# 4. Previous Education vs Python Score
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="preveducation", y="python")
plt.title("Python Score by Previous Education")
plt.xticks(rotation=45)
plt.show()

# 5. Country vs Python Score (Top 5 countries only)
top_countries = df['country'].value_counts().head(5).index
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[df['country'].isin(top_countries)], x="country", y="python")
plt.title("Python Score by Country (Top 5)")
plt.xticks(rotation=45)
plt.show()

# 6. High vs Low Performers (Python)
df["performance_group"] = df["python"].apply(lambda x: "High" if x >= df["python"].median() else "Low")

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="performance_group", y="studyhours")
plt.title("Study Hours: High vs Low Python Performers")
plt.show()

# ---------------------------------------------------------
# PHASE 7: FEATURE ENGINEERING
# ---------------------------------------------------------

# 1. Performance group (Python)
df["performance_group"] = df["python"].apply(
    lambda x: "High" if x >= df["python"].median() else "Low"
)

# 2. Study efficiency
df["study_efficiency"] = df["python"] / df["studyhours"]

# 3. Combined technical score
df["tech_score"] = (df["python"] + df["db"]) / 2

# 4. Age group
def age_group(age):
    if age <= 30:
        return "Young"
    elif age <= 45:
        return "Mid"
    else:
        return "Senior"

df["age_group"] = df["age"].apply(age_group)

# 5. Education strength score
edu_map = {
    "High School": 1,
    "Diploma": 2,
    "Bachelors": 3,
    "Masters": 4,
    "Doctorate": 5
}
df["edu_strength"] = df["preveducation"].map(edu_map)

# 6. Domestic vs International
df["is_domestic"] = df["country"].apply(lambda x: 1 if x == "Norway" else 0)

print("\nNew engineered features added:")
print(df[["performance_group", "study_efficiency", "tech_score", "age_group", "edu_strength", "is_domestic"]].head())
# ---------------------------------------------------------
# PHASE 8: PREDICTIVE MODELLING
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Regression: Predict Python score
features = ["studyhours", "entryexam", "db", "edu_strength", "is_domestic"]
X = df[features]
y = df["python"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_reg = LinearRegression()
model_reg.fit(X_train, y_train)

y_pred = model_reg.predict(X_test)

print("\n=== REGRESSION MODEL RESULTS ===")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Feature importance
importance = pd.Series(model_reg.coef_, index=features)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Encode target
le = LabelEncoder()
df["performance_encoded"] = le.fit_transform(df["performance_group"])

# Classification features
features_class = ["studyhours", "entryexam", "db", "edu_strength", "is_domestic"]
Xc = df[features_class]
yc = df["performance_encoded"]

Xc_train, Xc_test, yc_train, yc_test = train_test_split(Xc, yc, test_size=0.2, random_state=42)

model_clf = RandomForestClassifier(n_estimators=200, random_state=42)
model_clf.fit(Xc_train, yc_train)

yc_pred = model_clf.predict(Xc_test)

print("\n=== CLASSIFICATION MODEL RESULTS ===")
print("Accuracy:", accuracy_score(yc_test, yc_pred))
print("\nClassification Report:")
print(classification_report(yc_test, yc_pred))

# Feature importance
importances = pd.Series(model_clf.feature_importances_, index=features_class)
print("\nFeature Importance:")
print(importances.sort_values(ascending=False))
df.describe(include='all')