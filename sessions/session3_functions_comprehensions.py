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

# PART 1: Control Flow
marks = 72
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"
print(grade)

# Ternary
# result = output1 if condition else output2
result = "pass" if marks >= 40 else "fail"
print(result)

# # Loop with break and continue
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1   # count = count + 1

for i in range(5):
    print(i)

attempts = 0
password = ""
while password != "python2026":
    password = input("Enter password: ")
    attempts += 1
print(f"Correct! Took {attempts} attempt(s).")

day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("End of week")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:                         # default
        print("Midweek")

# # PART 2: Functions
def greet(name, greeting="Hello". score="90"):
    return f"{greeting}, {name}!"

print(greet("Raj"))
print(greet("Priya", greeting="Namaste"))
print(greet("Raj", greeting="Namaste", score=90))

def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 9, 2])
o1, o2 = min_max("abc")
print(o1, o2)
print(f"Min: {lo}, Max: {hi}")

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
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
#
# # Now the comprehension:
squares = [x ** 2 for x in range(10)]
print(squares)
#
# # Conditional comprehension:
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
#
# # Comprehension on strings:
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)

# # PART 4: Dict Comprehensions
#Loop version first:
name_lens = {}
names = ["Raj", "Priya", "Amit"]
for name in names:
    name_lens[name] = len(name)
print(name_lens)


name_lens = {name: len(name) for name in names}
print(name_lens)
#
# # Conditional dict comprehension:
long_names = {name: len(name) for name in names if len(name) > 3}
print(long_names)


#SCOPE:
# Scope Examples

# # ── LOCAL SCOPE ─────────────────────────────────────────────
def greet():
    message = "Hello Raj"   # local variable — exists only inside greet()
    print(message)

greet()
print(message)   # ← NameError: message is not defined
#                    # message was destroyed when greet() finished


# # ── GLOBAL SCOPE ────────────────────────────────────────────
course = "Python Bootcamp"   # global variable — exists everywhere

def show_course():
    print(course)   # functions can READ global variables

show_course()   # Python Bootcamp
print(course)   # Python Bootcamp — still accessible outside too


# # ── REASSIGNING GLOBAL INSIDE FUNCTION — the problem ────────
count = 0

def increment():
    count = count + 1   # ← UnboundLocalError!
                        # Python sees count on the left side and
                        # treats it as a LOCAL variable
                        # but it hasn't been assigned yet locally

increment()   # uncomment to see the error


# # ── global KEYWORD — the fix (but avoid this pattern) ───────
# count = 0

# def increment():
#     global count    # tells Python: use the global count, not a local one
#     count = count + 1

# increment()
# increment()
# print(count)   # 2


# # ── THE RIGHT WAY — pass in, return out ─────────────────────
# # Instead of relying on global variables, pass values as
# # parameters and return the result. This is the clean pattern.

# def increment(count):
#     return count + 1   # pure function — no global state touched

# count = 0
# count = increment(count)
# count = increment(count)
# print(count)   # 2 — same result, no global keyword needed


# # ── SAME NAME, DIFFERENT SCOPE ───────────────────────────────
# name = "Global Raj"   # global

# def show_name():
#     name = "Local Raj"   # local — completely separate variable
#     print(name)          # Local Raj

# show_name()
# print(name)   # Global Raj — global was never touched


# Pure Function Example

# NOT pure — has a side effect (modifies the list passed in)
def add_bonus_impure(marks, bonus):
    marks.append(bonus)   # modifies the original list — side effect
    return marks

scores = [88, 92, 74]
add_bonus_impure(scores, 100)
print(scores)   # [88, 92, 74, 100] — original was changed!


# # PURE — same input always gives same output, nothing outside is touched
def add_bonus_pure(marks, bonus):
    return marks + [bonus]   # creates a NEW list — original untouched

scores = [88, 92, 74]
result = add_bonus_pure(scores, 100)
print(scores)   # [88, 92, 74]       — original unchanged
print(result)   # [88, 92, 74, 100]  — new list returned

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

#Loop version:
# flat = []

# for sublist in nested:      # go through each inner list
#     for item in sublist:    # go through each item inside it
#         flat.append(item)   # add to flat list

#step by step:
# sublist = [1, 2]  →  item = 1, then item = 2
# sublist = [3, 4]  →  item = 3, then item = 4
# sublist = [5]     →  item = 5

# result → [1, 2, 3, 4, 5]

# [expression for item in list] -----normal comprehension
# [expression for outer in list for inner in outer] -----nested comprehension

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Using dict comprehension, create a word-length dictionary
# from a sentence, then filter to words longer than 4 characters.
