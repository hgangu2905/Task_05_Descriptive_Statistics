
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

