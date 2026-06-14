# ============================================================
# SESSION 2: Collections — Lists, Tuples, Dicts, Sets
# Day 1 Afternoon | 2:00 PM – 5:00 PM
# Topics: List, Tuple, Dict, Set — creation, access, methods
# ============================================================


# ── PART 1: Lists ───────────────────────────────────────────
# Type here live:




# ── PART 2: Tuples ──────────────────────────────────────────
# Type here live:




# ── PART 3: Sets ────────────────────────────────────────────
# Type here live:




# ── PART 4: Dicts — the key section ─────────────────────────
# Type here live:




# ── PART 5: Marks Analyzer (guided exercise) ────────────────
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Given a list of (student_name, marks) tuples, return the
# names of students who scored strictly above the class average.
# Example: [("Raj",88),("Priya",92),("Amit",61)] → ["Raj","Priya"]
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: Lists
# marks = [88, 92, 74, 95, 61]
# print(marks[0])      # 88
# print(marks[-1])     # 61
# print(marks[1:3])    # [92, 74]
# marks.append(80)
# marks.sort()
# print(marks)
# popped = marks.pop()
# print(popped)

# # PART 2: Tuples
# coords = (19.07, 72.87)   # Mumbai lat/lng — immutable
# lat, lng = coords          # unpacking
# print(lat, lng)
# # coords[0] = 20           # ← this would raise TypeError

# # PART 3: Sets
# visitors = {"Raj", "Priya", "Raj", "Amit"}
# print(visitors)               # Raj appears only once
# print("Raj" in visitors)      # True — fast lookup
# visitors.add("Sneha")
# print(len(visitors))

# # PART 4: Dicts
# student = {}
# student["name"] = "Raj"
# student["age"] = 22
# student["cgpa"] = 8.4
# print(student)
# print(student.get("marks", "Not found"))   # safe — no KeyError
# student.update({"city": "Mumbai", "year": 3})
# for key, val in student.items():
#     print(f"{key}: {val}")

# # PART 5: Marks Analyzer
# class_data = [("Raj", 88), ("Priya", 92), ("Amit", 61), ("Sneha", 79)]
# avg = sum(m for _, m in class_data) / len(class_data)
# above = [(n, m) for n, m in class_data if m > avg]
# print(f"Average: {avg:.1f}")
# print("Above average:", above)

# # PROBLEM SOLUTION
# data = [("Raj", 88), ("Priya", 92), ("Amit", 61), ("Sneha", 79)]
# avg = sum(m for _, m in data) / len(data)
# result = [name for name, marks in data if marks > avg]
# print(f"Average: {avg:.1f}")
# print("Above average:", result)

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Given a sentence, count the frequency of each word and
# print the top 3 most common words in order.
