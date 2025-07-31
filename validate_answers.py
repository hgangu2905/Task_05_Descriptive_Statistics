import pandas as pd
import json
import os

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Add total and average scores
df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]
df["average_score"] = df["total_score"] / 3

# Add category column
def categorize(score):
    if score < 150:
        return "Failing"
    elif score < 210:
        return "Average"
    else:
        return "Excellent"
df["performance_category"] = df["total_score"].apply(categorize)

# Best and worst subject per student (not used directly but optional for expansion)
score_cols = ["math score", "reading score", "writing score"]
df["best_subject"] = df[score_cols].idxmax(axis=1)
df["worst_subject"] = df[score_cols].idxmin(axis=1)

# Begin question/answer dictionary
answers = []

# BASIC QUESTIONS
answers.append({
    "question": "How many students are there in the dataset?",
    "correct_answer": int(len(df))
})

answers.append({
    "question": "What is the average math score?",
    "correct_answer": round(df["math score"].mean(), 2)
})

answers.append({
    "question": "What is the average reading score?",
    "correct_answer": round(df["reading score"].mean(), 2)
})

answers.append({
    "question": "What is the average writing score?",
    "correct_answer": round(df["writing score"].mean(), 2)
})

avg_scores = df[score_cols].mean()
answers.append({
    "question": "Which subject had the highest average score among students?",
    "correct_answer": avg_scores.idxmax()
})

test_prep_counts = df["test preparation course"].value_counts().to_dict()
answers.append({
    "question": "How many students completed the test preparation course?",
    "correct_answer": int(test_prep_counts.get("completed", 0))
})

gender_scores = df.groupby("gender")["total_score"].mean().to_dict()
answers.append({
    "question": "What are the average total scores of male and female students?",
    "correct_answer": {k: round(v, 2) for k, v in gender_scores.items()}
})

answers.append({
    "question": "How many students scored a total below 150?",
    "correct_answer": int((df["total_score"] < 150).sum())
})

answers.append({
    "question": "What are the three performance categories used to classify students?",
    "correct_answer": sorted(df["performance_category"].unique().tolist())
})

answers.append({
    "question": "How many students fall into each performance category?",
    "correct_answer": df["performance_category"].value_counts().to_dict()
})

# COMPLEX QUESTIONS

group_by_edu = df.groupby("parental level of education")["total_score"].mean()
answers.append({
    "question": "Which parental education group has the highest average total score?",
    "correct_answer": group_by_edu.idxmax()
})

# Test prep benefit by gender
test_prep_gender = df[df["test preparation course"] == "completed"].groupby("gender")["total_score"].mean().to_dict()
answers.append({
    "question": "Who benefits more from test preparation — males or females?",
    "correct_answer": max(test_prep_gender, key=test_prep_gender.get)
})

# Subject with most variation
std_devs = df[score_cols].std()
answers.append({
    "question": "Which subject shows the most variation in student performance?",
    "correct_answer": std_devs.idxmax()
})

race_writing = df.groupby("race/ethnicity")["writing score"].mean()
answers.append({
    "question": "Which group (by race/ethnicity) has the highest average writing score?",
    "correct_answer": race_writing.idxmax()
})

answers.append({
    "question": "If I want to increase the number of “Excellent” students, which performance category should I focus on and why?",
    "correct_answer": "Focus on 'Average' category, as they are closest to Excellent and more likely to improve with intervention."
})

# Save to JSON
os.makedirs("outputs", exist_ok=True)
with open("outputs/validation_stats.json", "w") as f:
    json.dump(answers, f, indent=2)

print("✅ Validation answers saved to outputs/validation_stats.json")
