# Task_05_Descriptive_Stats

## 📚 Project Overview

This research project investigates the ability of Large Language Models (LLMs) — specifically **Claude.ai by Anthropic** — to answer natural language questions grounded in descriptive statistics derived from a structured dataset. The goal is to evaluate Claude’s ability to perform factual recall, numerical reasoning, and decision-making based on summarized data.

This task was completed as part of a research-intensive course supervised by Professor Jeff Strome at Syracuse University.

---

## 📊 Dataset: Student Performance in Exams

- **Source:** [Kaggle – Students Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Description:** This dataset contains exam scores in math, reading, and writing for 1,000 students, along with demographic attributes like gender, parental education, and test prep completion.
- **Note:** *Per project requirements, the dataset is **not included** in this repository. Please download it manually and place it inside the `data/` folder as `StudentsPerformance.csv`.*

---

## 🧭 Project Goals

1. Compute descriptive statistics on the dataset using Python.
2. Design natural language prompts to query the dataset.
3. Ask Claude.ai to answer these questions using only summary information.
4. Validate Claude’s answers against ground-truth script-based results.
5. Analyze where Claude succeeds, struggles, or fails in reasoning.

---

## 🗂️ Repository Structure

```
Task_05_Descriptive_Stats/
├── data/
│ └── StudentsPerformance.csv # (Local only – not uploaded)
├── outputs/
│ ├── descriptive_stats.txt # Raw printed stats
│ └── validation_stats.json # Correct answers from dataset
├── .gitignore # Prevents dataset and outputs from being committed
├── basic_questions.md # 10 basic questions with Claude responses + validation
├── complex_questions.md # 5 complex questions with reasoning evaluation
├── descriptive_stats.py # Script to compute descriptive stats
└── validate_answers.py # Script to generate correct answers programmatically
```
---

## 🛠️ Tools and Technologies

- **Python 3.9+**
- **Pandas** for data analysis
- **Claude.ai** (Anthropic) for LLM responses
- **Markdown** for prompt and answer logs
- **JSON** for automated output storage and validation

---

## 🧪 Methodology

### 1. Statistical Analysis
We used `descriptive_stats.py` to calculate:
- Average, min, max scores per subject
- Total scores and performance classification (Failing, Average, Excellent)
- Group-wise performance by gender, test prep, and parental education

Results were saved to `outputs/descriptive_stats.txt`.

---

### 2. Prompt Engineering
We created:
- 🔹 **10 Basic Questions** — involving averages, counts, group means
- 🔹 **5 Complex Questions** — involving reasoning, comparisons, and decisions

Claude.ai was used to answer these prompts, and responses were logged in:
- `basic_questions.md`
- `complex_questions.md`

---

### 3. Validation and Comparison
Using `validate_answers.py`, we generated the ground truth for all 15 questions directly from the dataset. This allowed us to:
- Compare Claude's responses against exact values
- Evaluate whether Claude’s reasoning was accurate or flawed
- Store answers programmatically in `validation_stats.json`

---

## 📊 Evaluation Summary

| Question Type | Total Questions | Correct | Incorrect | Accuracy |
|---------------|------------------|---------|-----------|----------|
| Basic         | 10               | 7       | 3         | ✅ 70%   |
| Complex       | 5                | 3       | 2         | ✅ 60%   |

---

## 🧠 Observations

- Claude.ai performed well on direct questions involving averages and group counts.
- It struggled with:
  - Custom label classification (e.g., “Excellent” vs “High Performance”)
  - Off-by-one errors or assumptions about category thresholds
- Strong reasoning was shown in some answers, but errors emerged in logic-heavy tasks.
- Prompt phrasing and clarity made a noticeable difference in accuracy.

---

## 🙏 Acknowledgments

This work was completed as part of a research project under the mentorship of Professor Jeff Strome at the Syracuse University School of Information Studies. Special thanks to Anthropic’s Claude.ai for providing a unique perspective on LLM-based statistical reasoning.

