### Question 1:
**Prompt:** How many students are there in the dataset?  
**LLM Response:** 1,000 students 
**Correct Answer:** 1000  
**Correct?** Yes 
**Notes:**  Perfect match — factual and easy for LLM to retrieve.

---

### Question 2:
**Prompt:** What is the average math score?  
**LLM Response:**  66.1
**Correct Answer:** 66.09  
**Correct?** Yes 
**Notes:**  LLM rounded to one decimal; still considered correct.

---

### Question 3:
**Prompt:** What is the average reading score?  
**LLM Response:**  69.2
**Correct Answer:** 69.17 
**Correct?**  Yes
**Notes:**  Minor rounding; within acceptable margin.

---

### Question 4:
**Prompt:** What is the average writing score?  
**LLM Response:** 68.1
**Correct Answer:** 68.05
**Correct?**  Yes
**Notes:**  Rounding is acceptable; still accurate.

---

### Question 5:
**Prompt:** Which subject had the highest average score among students?  
**LLM Response:**  Reading, with an average score of 69.2
**Correct Answer:** Reading Score
**Correct?**  Yes
**Notes:**  Subject name and rationale match dataset; valid.
---

### Question 6:
**Prompt:** How many students completed the test preparation course?  
**LLM Response:**  358 students completed the test preparation course (35.8% of all students)
**Correct Answer:** 358
**Correct?**  Yes
**Notes:**  Accurate count and percentage; well reasoned.

---

### Question 7:
**Prompt:** What are the average total scores of male and female students?  
**LLM Response:**  Male students: 201.4 (average total score). Female students: 204.9 (average total score). Female students scored slightly higher on average.
**Correct Answer:** female: 208.71, male: 197.51  
**Correct?**  No
**Notes:**  LLM got the direction correct (female > male), but values are inaccurate — possibly inferred or outdated.


---

### Question 8:
**Prompt:** How many students scored a total below 150?  
**LLM Response:**  102 students (10.2% of all students)
**Correct Answer:** 103 
**Correct?** No
**Notes:**  LLM is close but incorrect; off by 1, may have used rounded category boundaries.


---

### Question 9:
**Prompt:** What are the three performance categories used to classify students?  
**LLM Response:**  Based on total scores (math + reading + writing):
High Performance: Total score ≥ 240
Average Performance: Total score 180-239
Low Performance: Total score < 180
**Correct Answer:** Average, Excellent, Failing
**Correct?** No
**Notes:**  LLM made up different labels and thresholds — doesn't match categorization from the script.

---

### Question 10:
**Prompt:** How many students fall into each performance category?  
**LLM Response:**  High Performance: 273 students (27.3%)
Average Performance: 525 students (52.5%)
Low Performance: 202 students (20.2%)
The interactive visualization above shows all these findings with charts and detailed breakdowns. The majority of students (52.5%) fall into the Average Performance category, while about 1 in 4 students achieve High Performance. 
**Correct Answer:** Excellent: 459, Average: 438, Failing: 103  
**Correct?**  No
**Notes:**  LLM created its own categories and misclassified totals; not aligned with actual dataset logic.
