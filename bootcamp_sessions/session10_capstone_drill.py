# ============================================================
# SESSION 10: Capstone Presentations & Wrap-up
# Day 5 Afternoon | 2:00 PM – 5:00 PM
# ============================================================
# No live coding this session.
# This file contains the 10-question interview drill for you
# to run with the class after presentations.
# ============================================================


# ── INTERVIEW DRILL — 10 questions, one per session ─────────
# Run rapid-fire. Students answer out loud.
# Give 30 seconds per question. Discuss briefly after each.


# Q1 (Session 1 — Strings):
# What is the output of "Python"[1:4]?
# Answer: "yth"


# Q2 (Session 2 — Collections):
# How do you safely get a value from a dict without raising a KeyError?
# Answer: dict.get("key", default_value)


# Q3 (Session 3 — Comprehensions):
# Write a list comprehension that returns even squares from 1 to 10.
# Answer: [x**2 for x in range(1, 11) if x % 2 == 0]  → [4, 16, 36, 64, 100]


# Q4 (Session 4 — *args / Lambda):
# When would you use **kwargs instead of a regular parameter?
# Answer: When the function needs to accept an unknown number of keyword arguments.


# Q5 (Session 5 — File I/O):
# What is the difference between file modes "w" and "a"?
# Answer: "w" overwrites the file (destroys existing content).
#         "a" appends to the end without destroying existing content.


# Q6 (Session 6 — Collections):
# What does Counter.most_common(3) return?
# Answer: A list of the 3 most common (element, count) tuples, sorted by count descending.


# Q7 (Session 7 — OOP):
# What does @property do? Why use it instead of a regular method?
# Answer: Lets you access a method like an attribute (no parentheses).
#         Used for controlled read access — you can validate/compute on the way out.


# Q8 (Session 8 — Inheritance):
# What does super().__init__() do in a child class?
# Answer: Calls the parent class's __init__ so parent attributes are set up.
#         Without it, the parent's setup is skipped entirely.


# Q9 (Session 9 — Pandas):
# What is the difference between groupby().sum() and groupby().agg()?
# Answer: .sum() aggregates one column with one operation.
#         .agg() lets you apply multiple operations to multiple columns at once.


# Q10 (Open):
# What was the hardest concept this week and how did you work through it?
# (No single answer — let students reflect. This is the most valuable question.)


# ── STUDENT PRESENTATION PROMPT ─────────────────────────────
# For each student (5 minutes each):
#
# 1. Show us your project running
# 2. Walk us through one interesting part of your code
# 3. What is one thing you would add if you had more time?
#
# You ask ONE question after each presentation.
# Keep a timer visible. 5 minutes is strict.


# ── CLOSING NOTE ─────────────────────────────────────────────
# Read this at the very end of Day 5:
#
# "You've covered in 5 days what most self-taught developers
#  take months to piece together. The foundation is solid —
#  now it's about reps. Pick one project from the website,
#  start it this weekend, and push it to GitHub.
#  That is the only next step that matters."
