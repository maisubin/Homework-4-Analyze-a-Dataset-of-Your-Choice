
import pandas as pd

# ------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------
df = pd.read_csv("data/AI_Impact_On_Jobs_2030.csv")

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATAFRAME INFO ===")
print(df.info())

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

# ------------------------------------------------
# 2. Accessing Data Using loc and iloc
# ------------------------------------------------
print("\n=== loc: Single Row by Label (row label 0) ===")
print(df.loc[0])

print("\n=== iloc: Single Row by Position (row 1) ===")
print(df.iloc[1])

print("\n=== loc: Slice of Rows by Label (0 to 4) ===")
print(df.loc[0:4])

print("\n=== iloc: Slice of Rows by Position (rows 0 to 4) ===")
print(df.iloc[0:5])

print("\n=== Single Column by Name: Average_Salary ===")
print(df["Average_Salary"].head())

print("\n=== Single Cell using loc (row 0, Job_Title) ===")
print(df.loc[0, "Job_Title"])

# ------------------------------------------------
# 3. Filtering Data
# ------------------------------------------------
print("\n=== FILTER 1: Jobs with Average Salary > 100,000 ===")
filter1 = df[df["Average_Salary"] > 100000]
print(filter1.head())

print("\n=== FILTER 2: Salary > 100,000 AND Automation Probability < 0.4 ===")
filter2 = df[(df["Average_Salary"] > 100000) &
             (df["Automation_Probability_2030"] < 0.4)]
print(filter2.head())

# ------------------------------------------------
# 4. Add and Drop Columns
# ------------------------------------------------
print("\n=== ADD NEW COLUMN: AI_Risk_Score ===")
df["AI_Risk_Score"] = df["AI_Exposure_Index"] * df["Automation_Probability_2030"]
print(df[["Job_Title", "AI_Risk_Score"]].head())

print("\n=== DROP COLUMN: AI_Risk_Score ===")
df = df.drop("AI_Risk_Score", axis=1)
print(df.columns)

# ------------------------------------------------
# 5. Groupby Aggregation
# ------------------------------------------------
print("\n=== GROUPBY: MEAN Average_Salary PER Risk_Category ===")
group_result = df.groupby("Risk_Category")["Average_Salary"].mean()
print(group_result)

print("\n=== SCRIPT COMPLETED SUCCESSFULLY ===")
