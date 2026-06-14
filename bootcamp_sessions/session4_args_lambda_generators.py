# ============================================================
# SESSION 4: Intermediate — *args, **kwargs, Lambda, Generators
# Day 2 Afternoon | 2:00 PM – 5:00 PM
# Topics: *args, **kwargs, lambda, map/filter, enumerate, zip, generators
# ============================================================


# ── PART 1: *args ───────────────────────────────────────────
# Type here live:




# ── PART 2: **kwargs ────────────────────────────────────────
# Type here live:




# ── PART 3: Combining *args and **kwargs ────────────────────
# Type here live:




# ── PART 4: Lambda with sorted / filter / map ───────────────
# Type here live:




# ── PART 5: enumerate and zip ───────────────────────────────
# Type here live:




# ── PART 6: Generators ──────────────────────────────────────
# Type here live:




# ── PART 7: Score Filter (guided exercise) ──────────────────
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Write a function that accepts any number of exam scores
# using *args. Return only passing scores (>=40), sorted
# descending. Use filter() with a lambda inside the function.
# Example: passing_scores(88, 32, 92, 15, 74) → [92, 88, 74]
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: *args
# def total(*nums):
#     return sum(nums)
#
# print(total(10, 20, 30))       # 60
# print(total(5, 5))             # 10
# print(total(1, 2, 3, 4, 5))   # 15
#
# # args is a TUPLE inside the function
# def show_types(*args):
#     print(type(args))   # <class 'tuple'>
#     for item in args:
#         print(item)
# show_types("a", 1, True)

# # PART 2: **kwargs
# def print_profile(**info):
#     for key, val in info.items():
#         print(f"{key}: {val}")
#
# print_profile(name="Raj", age=22, city="Mumbai")

# # PART 3: Combining *args and **kwargs
# def report(title, *scores, **meta):
#     print(f"--- {title} ---")
#     print(f"Scores: {scores}")
#     print(f"Meta  : {meta}")
#
# report("Exam Results", 88, 92, 74, semester=3, subject="Python")

# # PART 4: Lambda
# # With sorted
# students = [("Raj", 88), ("Priya", 92), ("Amit", 61)]
# by_marks = sorted(students, key=lambda s: s[1], reverse=True)
# print(by_marks)
#
# # With filter
# scores = [88, 32, 92, 15, 74, 38]
# passing = list(filter(lambda x: x >= 40, scores))
# print(passing)
#
# # With map
# names = ["raj", "priya", "amit"]
# titled = list(map(lambda n: n.title(), names))
# print(titled)

# # PART 5: enumerate and zip
# names = ["Raj", "Priya", "Amit"]
# for i, name in enumerate(names, start=1):
#     print(f"{i}. {name}")
#
# subjects = ["Math", "Python", "OS"]
# for name, subj in zip(names, subjects):
#     print(f"{name} → {subj}")
#
# # zip to make a dict
# student_dict = dict(zip(names, subjects))
# print(student_dict)

# # PART 6: Generators
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
# for val in countdown(5):
#     print(val)
#
# # Generator is lazy — range() is a generator
# gen = (x ** 2 for x in range(10))  # generator expression
# print(next(gen))  # 0
# print(next(gen))  # 1

# # PROBLEM SOLUTION
# def passing_scores(*scores):
#     passing = list(filter(lambda x: x >= 40, scores))
#     return sorted(passing, reverse=True)
#
# print(passing_scores(88, 32, 92, 15, 74))   # [92, 88, 74]
# print(passing_scores(20, 15, 10))            # []

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Use zip to combine a list of student names and marks into a
# dict. Then use a generator to yield only students who passed
# (marks >= 40).
