# ============================================================
# SESSION 3: Control Flow, Functions & Comprehensions
# Day 2 Morning | 10:00 AM – 1:00 PM
# Topics: if/elif/else, loops, functions, list & dict comprehensions
# ============================================================


# ── PART 1: Control Flow ────────────────────────────────────
# Type here live:




# ── PART 2: Functions ───────────────────────────────────────
# Type here live:




# ── PART 3: List Comprehensions ─────────────────────────────
# Show loop version FIRST, then rewrite as comprehension
# Type here live:




# ── PART 4: Dict Comprehensions ─────────────────────────────
# Type here live:




# ── PART 5: Grade Classifier (guided exercise) ──────────────
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Flatten a nested list using list comprehension ONLY.
# No loops allowed — one comprehension expression only.
# Example: [[1,2],[3,4],[5]] → [1,2,3,4,5]
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: Control Flow
# marks = 72
# if marks >= 90:
#     grade = "A"
# elif marks >= 75:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# elif marks >= 40:
#     grade = "D"
# else:
#     grade = "F"
# print(grade)
#
# # Ternary
# result = "pass" if marks >= 40 else "fail"
# print(result)
#
# # Loop with break and continue
# for i in range(10):
#     if i == 3:
#         continue   # skip 3
#     if i == 7:
#         break      # stop at 7
#     print(i)

# # PART 2: Functions
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# print(greet("Raj"))
# print(greet("Priya", greeting="Namaste"))
#
# # Multiple return values
# def min_max(nums):
#     return min(nums), max(nums)
#
# lo, hi = min_max([3, 1, 9, 2])
# print(f"Min: {lo}, Max: {hi}")

# # PART 3: List Comprehensions
# # Loop version first:
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)
#
# # Now the comprehension:
# squares = [x ** 2 for x in range(10)]
# print(squares)
#
# # Conditional comprehension:
# evens = [x for x in range(20) if x % 2 == 0]
# print(evens)
#
# # Comprehension on strings:
# words = ["hello", "world", "python"]
# upper = [w.upper() for w in words]
# print(upper)

# # PART 4: Dict Comprehensions
# names = ["Raj", "Priya", "Amit"]
# name_lens = {name: len(name) for name in names}
# print(name_lens)
#
# # Conditional dict comprehension:
# long_names = {name: len(name) for name in names if len(name) > 3}
# print(long_names)

# # PART 5: Grade Classifier
# def get_grade(mark):
#     if mark >= 90: return "A"
#     elif mark >= 75: return "B"
#     elif mark >= 60: return "C"
#     elif mark >= 40: return "D"
#     else: return "F"
#
# students = [("Raj", 88), ("Priya", 92), ("Amit", 38), ("Sneha", 74)]
# grades = {name: get_grade(m) for name, m in students}
# print(grades)

# # PROBLEM SOLUTION
# nested = [[1, 2], [3, 4], [5]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)   # [1, 2, 3, 4, 5]

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Using dict comprehension, create a word-length dictionary
# from a sentence, then filter to words longer than 4 characters.
