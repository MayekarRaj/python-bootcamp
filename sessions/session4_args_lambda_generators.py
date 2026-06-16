# ============================================================
# SESSION 4: Intermediate — *args, **kwargs, Lambda, Generators
# Day 2 Afternoon | 2:00 PM – 5:00 PM
# Topics: *args, **kwargs, lambda, map/filter, enumerate, zip, generators
# ============================================================
def total(*nums):
    print(type(nums))
    print(nums)
    return sum(nums)

# print()
print(total(10, 20, 30))       # 60
print(total(5, 5))             # 10
print(total(1, 2, 3, 4, 5))   # 15

print("--------------------------------")
nums = [1, 2, 3]
print(*nums)    # same as print(1, 2, 3) — unpacks the list
# print(total(*nums))
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


def report(title, *scores):
    print(f"--- {title} ---")
    print(f"Scores: {scores}")

report("Exam", 88, 92, 74)

print("--------------------------------")
def func(a, b, c): #10, 20, 30 
    print(a, b, c)

func(20, 30, 10) #20, 30, 10
func(10, 20, 30) #20, 30, 10


def greet(name, greeting="Hello", score="90"):
    return f"{greeting}, {name}! Your score is {score}."

print(greet("Raj"))
print(greet("Priya", greeting="Namaste"))
print(greet("Raj", score="90", greeting="Namaste"))

print("--------------------------------")

# --- Exam ---
# Scores: (88, 92, 74)

# PART 2: **kwargs
def print_profile(**info):
    for key in info.items():
        print(key)
    for key, val in info.items():
        print(f"{key}: {val}")
#
print_profile(name="Raj", age=22, city="Mumbai")

# def print_profile(**info):
#     for key, val in info.items():
#         print(f"{key}: {val}")

# print_profile(name="Raj", age=22, city="Mumbai")
# # name: Raj
# # age: 22
# # city: Mumbai

def show_types(*kwargs):
    print(type(kwargs))   # <class 'tuple'>
    for item in kwargs:
        print(item)
# show_types(name="Raj", age=22, city="Mumbai")

# Order in function signature:
def fn(positional, *args, **kwargs):
    pass

# # PART 3: Combining *args and **kwargs
def report(title, *scores, **meta):
    print(f"--- {title} ---")
    print(f"Scores: {scores}")
    print(f"Meta  : {meta}")

report("Exam Results", 88, 92, 74, semester=3, subject="Python")

# config = {"name": "Raj", "age": 22}
# print_profile(**config)   # same as print_profile(name="Raj", age=22)

# # PART 4: Lambda

# normal function
def square(x):
    return x * 2

# same as lambda
square = lambda x: x * 2

print(square(5))  # 10

reverse   = lambda s: s[::-1]
print(reverse("Raj"))     

# lambda x: x * 2 — takes x, returns x * 2
# # With sorted
students = [("Raj", 88), ("Priya", 92), ("Amit", 61)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks)
# [('Priya', 92), ('Raj', 88), ('Amit', 61)]

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, numbers))
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)  # [2, 4, 6]

# filter() → keeps only items where lambda/function returns True

#
# # With filter
# scores = [88, 32, 92, 15, 74, 38]
# passing = list(filter(lambda x: x >= 40, scores))
# print(passing)
# [88, 92, 74]


def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result1 = list(map(square, numbers))
result2 = list(map(lambda x: x ** 2, numbers))
print(result1)  # [1, 4, 9, 16, 25]
print(result2)  # [1, 4, 9, 16, 25]
#
# # With map
# names = ["raj", "priya", "amit"]
# titled = list(map(lambda n: n.title(), names))
# print(titled)
# ["Raj", "Priya", "Amit"]
# map() → applies lambda to every item in the list


# What lambda cannot do:
# Cannot have multiple statements
# Cannot have an if/else block (only ternary x if cond else y)
# Cannot have a docstring
# Cannot be debugged easily — no name in tracebacks


# # These three do the same thing:
# list(map(lambda x: x**2, range(5)))          # map
# [x**2 for x in range(5)]                      # comprehension
# # filter equivalent:
# list(filter(lambda x: x % 2 == 0, range(10))) # filter
# [x for x in range(10) if x % 2 == 0]          # comprehension


# # PART 5: enumerate and zip
print("--------------------------------enumerate--------------------------------")
names = ["Raj", "Priya", "Amit"]
result = enumerate(names)
print(type(result))
print(list(result))
for i in enumerate(names):
    print(i)
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
print("--------------------------------enumerate--------------------------------")


subjects = ["Math", "Python", "OS"]
for name, subj in zip(names, subjects):
    print(f"{name} → {subj}")

# zip to make a dict
student_dict = dict(zip(names, subjects))
print(student_dict)

# # PART 6: Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(5):
    print(val)

# How it works under the hood:

# First call to next() runs until it hits yield, pauses, returns the value
# Next call resumes from exactly where it paused
# When the function ends, raises StopIteration
# for loops handle this automatically
#
# Generator is lazy — range() is a generator
gen = (x ** 2 for x in range(10))  # generator expression
print(next(gen))  # 0
print(next(gen))  # 1

# gen = (x**2 for x in range(10))   # generator — lazy
# lst = [x**2 for x in range(10)]   # list — eager, all computed now
# # This creates a list of 1 million numbers in memory all at once
# nums = [x**2 for x in range(1_000_000)]   # ~8MB in memory

# # This creates ONE number at a time — almost zero memory
# nums = (x**2 for x in range(1_000_000))   # generator expression
print("--------------------------------generator--------------------------------")
gen = (x for x in range(3))
print(list(gen))   # [0, 1, 2]
print(list(gen))   # []  ← empty — generator is done, can't reuse it
print("--------------------------------generator--------------------------------")


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
