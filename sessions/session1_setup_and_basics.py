# ============================================================
# SESSION 1: Setup & Python Basics
# Day 1 Morning | 10:00 AM – 1:00 PM
# Topics: Variables, Data Types, Strings, f-strings
# ============================================================
# HOW TO USE THIS FILE:
#   - Type code in the LIVE CODING AREA below
#   - Reference solution is commented out at the bottom
#   - Do NOT paste — type everything live with students
# ============================================================


# ── PART 1: Variables & Data Types ──────────────────────────
# Type here live:




# ── PART 2: Strings & String Methods ────────────────────────
# Type here live:




# ── PART 3: f-strings ───────────────────────────────────────
# Type here live:




# ── PART 4: Student Profile Program (guided exercise) ───────
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Given a sentence as input, return the most frequent word
# (case-insensitive).
# Example: "The cat sat on the mat" → "the"
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: Variables & Data Types
name = "Raj"
age = 22
cgpa = 8.4
is_passing = True


#
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(cgpa))       # <class 'float'>
print(type(is_passing)) # <class 'bool'>

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)

a = b = 10
print(a, b)
# a, *b, c = 1, 2, 3, 4
# print(a, b, c)

# a, *b, c = 1, 2, 3, 4
# print(a, b, c)

# a, *b, c = 1, 2, 3, 4
# print(a, b, c)

# # PART 2: Strings & String Methods
city = "Mumbai"
print(city.upper())         # MUMBAI
print(city.lower())         # mumbai
print(city[0:3])            # Mum
print(city[-1])             # i
print(len(city))            # 6
#
sentence = "  Hello World  "
print(sentence.strip())     # "Hello World"
print(sentence.split("l"))     # ['Hello', 'World']

#
greeting = "Hello"
print(greeting.replace("Hello", "Namaste"))  # Namaste

# # PART 3: f-strings
name = "Raj"
age = 22
city = "Mumbai"
print(f"Hello {name}, you are {age} years old and live in {city}")
print(f"Name has {len(name)} characters")
print(f"CGPA: {cgpa:.2f}")  # 1 decimal place

# # PART 4: Student Profile Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"--- Student Profile ---")
print(f"Name    : {name.title()}")
print(f"Age     : {age}")
print(f"City    : {city}")
print(f"Initials: {name[0].upper()}")

# # PROBLEM SOLUTION
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1 
print(max(freq, key=freq.get))
 
# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Write a program that takes a full name as input and prints:
#   1. Initials (e.g. R.M.)
#   2. Name reversed word-by-word (e.g. "Raj Mayekar" → "Mayekar Raj")
#   3. Number of vowels in the full name
