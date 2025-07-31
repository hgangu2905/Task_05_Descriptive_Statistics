import pandas as pd
import sys
import os

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Redirect output to both console and file
class DualOutput:
    def __init__(self, *files):
        self.files = files
    def write(self, msg):
        for f in self.files:
            f.write(msg)
    def flush(self):
        for f in self.files:
            f.flush()

output_file = open("outputs/descriptive_stats.txt", "w")
sys.stdout = DualOutput(sys.stdout, output_file)

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Add total and average score
df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]
df["average_score"] = df["total_score"] / 3

print("===== Basic Dataset Info =====")
print("Number of records:", len(df))
print("Columns:", list(df.columns))
print("\nUnique values per column:\n", df.nunique())

print("\n===== Descriptive Stats for Individual Scores =====")
score_cols = ["math score", "reading score", "writing score"]
print(df[score_cols].describe())

print("\n===== Correlation Between Scores =====")
print(df[score_cols].corr())

print("\n===== Top 5 Students by Total Score =====")
print(df.sort_values("total_score", ascending=False).head(5)[["gender", "race/ethnicity", "total_score"]])

print("\n===== Bottom 5 Students by Total Score =====")
print(df.sort_values("total_score").head(5)[["gender", "race/ethnicity", "total_score"]])

print("\n===== Best and Worst Subject for Each Student (Sample 5) =====")
df["best_subject"] = df[score_cols].idxmax(axis=1)
df["worst_subject"] = df[score_cols].idxmin(axis=1)
print(df[["math score", "reading score", "writing score", "best_subject", "worst_subject"]].head(5))

print("\n===== Score Categories =====")
def categorize(score):
    if score < 150:
        return "Failing"
    elif score < 210:
        return "Average"
    else:
        return "Excellent"

df["performance_category"] = df["total_score"].apply(categorize)
print(df["performance_category"].value_counts())

print("\n===== Average Total Score by Gender =====")
print(df.groupby("gender")["total_score"].mean())

print("\n===== Average Total Score by Parental Education =====")
print(df.groupby("parental level of education")["total_score"].mean().sort_values(ascending=False))

print("\n===== Average Total Score by Test Prep Course =====")
print(df.groupby("test preparation course")["total_score"].mean())

print("\n===== Underperforming Students (total_score < 150) =====")
print(df[df["total_score"] < 150][["gender", "parental level of education", "test preparation course", "total_score"]].head())

# Close the output file
output_file.close()
