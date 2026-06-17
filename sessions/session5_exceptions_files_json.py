# # ============================================================
# # SESSION 5: Exception Handling, File I/O & JSON
# # Day 3 Morning | 10:00 AM – 1:00 PM
# # Topics: try/except/finally, open(), csv module, json module
# # ============================================================


# # ── PART 1: Exceptions — crash first, then handle ───────────
# # Type here live:




# # ── PART 2: File I/O — read and write ───────────────────────
# # Type here live:




# # ── PART 3: CSV with csv.DictReader ─────────────────────────
# # Type here live:




# # ── PART 4: JSON — load and dump ────────────────────────────
# # Type here live:




# # ── PART 5: Config Reader (guided exercise) ─────────────────
# # Type here live:




# # ── PROBLEM OF THE SESSION ──────────────────────────────────
# # Create a CSV with columns: name, age, marks.
# # Include 2-3 rows with missing or non-numeric marks.
# # Read it with csv.DictReader. Skip malformed rows gracefully.
# # Print only valid records sorted by marks descending.
# # Students attempt independently. Type your solution here:




# # ============================================================
# # REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# # ============================================================

# print(1 / 0)       # ZeroDivisionError
# int("abc")         # ValueError
# d = {}; d["key"]   # KeyError
# lst = []; lst[5]   # IndexError

# # # PART 1: Exceptions
# # # Step 1 — let it crash first
# # # print(1 / 0)
# #
# # # Step 2 — wrap it
# try:
#     result = 1 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     # ALWAYS runs — error or not
#     print("This always runs")
# #
# # # Multiple exception types
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("That's not a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("This always runs — cleanup goes here")

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# # except ValueError:
# #     print("That's not a valid number")
# # except ZeroDivisionError:
# #     print("Cannot divide by zero")
# # except (ValueError, TypeError):
# #     print("Wrong value or wrong type")
# except Exception as e:
#     print(f"Something unexpected: {e}")
# finally:
#     print("Done")

# # except Exception as e — catches any exception and gives you the error object. 
# # str(e) or e.args gives the message. Use as a last resort — too broad a catch hides bugs.
# #

# # Raising your own exception
# def set_age(age):
#     if age < 0:
#         raise ValueError(f"Age cannot be negative: {age}")
#     return age

# try:
#     set_age(-5)
# except ValueError as e:
#     print(e)   # Age cannot be negative: -5


# # # PART 2: File I/O

# f = open("notes.txt", "w")   # open file
# f.write("Hello Raj")         # do work
# f.write(10 / 0)              # error here — ZeroDivisionError
# f.close()                    # manually close file


# # Write a file

# with - context manager - automatically closes the file even if an error occurs

# with open("notes.txt", "w") as f:
#     f.write("Python is fun\n")
#     f.write("File handling is easy\n")

# # # Read it back
# with open("notes.txt", "r") as f:
#     content = f.read()
# print(content)
# #
# # Read line by line
# with open("notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())
# #
# # Append mode — does not overwrite
# with open("notes.txt", "a") as f:
#     f.write("Line 3 added later\n")
# #
# # Handle file not found
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found — check the path")

with open("students.csv", "r", encoding="utf-8") as f:
    content = f.read()
# # If utf-8 fails: try encoding="utf-8-sig" or encoding="latin-1"

# # PART 3: CSV
import csv
#
# # Create sample CSV
rows = [
    ["name", "marks"],
    ["Raj", "88"],
    ["Priya", "92"],
    ["Amit", ""],      # missing marks — bad row
]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader:
        print(row)   # ['Raj', '22', '88']
#
# # Read with DictReader — each row is a dict
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)   # {'name': 'Raj', 'marks': '88'}

# CSV values are always strings — cast when needed:

# # PART 4: JSON
import json
#
config = {"app": "bootcamp", "version": 1, "debug": True}
#
# # Write JSON
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# # Read JSON
with open("config.json", "r") as f:
    loaded = json.load(f)
#
print(loaded["app"])     # bootcamp
print(type(loaded))      # <class 'dict'>
#

# json.dumps — to string (not file)
json_str = json.dumps(config)
print(json_str)

# json.loads — from string (not file)
back = json.loads(json_str)
print(back["version"])

# Type mapping — Python ↔ JSON:
# PythonJSON 
# dict -> object {} 
# list -> array []
# str -> string ""
# int / float -> number
# True / False -> true / false
# None -> null

# LBYL - Look Before You Leap
if "marks" in row and row["marks"].isdigit():
    marks = int(row["marks"])

# EAFP - Easier to Ask Forgiveness than Permission
try:
    marks = int(row["marks"])
except (ValueError, KeyError):
    marks = 0

# # PROBLEM SOLUTION
# import csv
#
# data = "name,age,marks\nRaj,22,88\nPriya,21,\nAmit,23,abc\nSneha,22,79\n"
# with open("students.csv", "w") as f:
#     f.write(data)
#
# valid = []
# with open("students.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         try:
#             marks = int(row["marks"])
#             valid.append({"name": row["name"], "marks": marks})
#         except (ValueError, KeyError):
#             print(f"Skipping bad row: {row}")
#
# valid.sort(key=lambda x: x["marks"], reverse=True)
# for s in valid:
#     print(f"{s['name']}: {s['marks']}")

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Read a JSON config file, modify one value, and write it back.
# Handle the case where the file doesn't exist by creating it
# with default values.
