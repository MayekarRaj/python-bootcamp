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
marks = [88, 92, 74, 95, 61]
# print(marks[0])      # 88
# print(marks[-1])     # 61
# print(marks[1:3])    # [92, 74]
# marks.append(80)
# marks.sort()
# print(marks)
# popped = marks.pop()
# pop2 = marks.pop(2)
# print(popped)
# print(pop2)

# marks.append(80)   # adds to END
# marks.insert(2, 99)# inserts 99 at index 2
# marks.pop()        # removes and returns last item
# marks.pop(0)       # removes and returns item at index 0
# marks.remove(74)   # removes first occurrence of value 74
# marks.sort()       # sorts IN PLACE — modifies original
# marks.reverse()    # reverses IN PLACE
# sorted(marks)      # returns NEW sorted list — original unchanged
# marks.count(88)    # count occurrences of 88
# marks.index(92)    # returns index of first occurrence of 92


print("--------------------------------")
marks2 = marks
marks.append(100)
print(marks2)
markscopy = marks.copy()       # shallow copy — important: marks2 = marks does NOT copy
# print(markscopy)
marks.append(101)
print(markscopy)
print(marks)
print(marks2)
print("--------------------------------")

#list concatenation 
# [1,2] + [3,4]
print([1,2] + [3,4])
print([1,2] * 3)

# a, b = b, a

# # PART 2: Tuples
coords = (19.07, 72.87)   # Mumbai lat/lng — immutable
lat, lng = coords          # unpacking
print(lat, lng)
# coords[0] = 20           # ← this would raise TypeError

# PART 2: Tuples
# coords = (19.07, 72.87)   # Mumbai lat/lng — immutable
# lat, lng = coords          # unpacking
# print(lat, lng)
# # coords[0] = 20           # ← this would raise TypeError

# tuple concatenation
# (1,2) + (3,4)
print((1,2) + (3,4))
print((1,2) * 3)


first, *rest = (1, 2, 3, 4)
print(first, rest)

first, *rest, last = (1, 2, 3, 4)
print(first, rest, last)
name, *scores = ("Raj", 88, 92, 75, 95)
print(name, scores)



# # PART 3: Sets
visitors = {"Raj", "Priya", "Raj", "Amit"}
print(visitors)               # Raj appears only once
print("Raj" in visitors)      # True — fast lookup
visitors.add("Sneha")
print(len(visitors))

# # PART 4: Dicts
student = {}
student["name"] = "Raj"


student["age"] = 22
student["cgpa"] = 8.4
# student["Name"] = "Raj"
print(student['name'])
print(student)
print(student.get("name", "Not found"))   # safe — no KeyError
student.update({"city": "Mumbai", "year": 3})
print(student)
print("*************")
for key in student.items():
    # print(f"{key}: {val}")
    print(key)
print("*************")


"name" in student       # True — checks KEYS only
"Raj" in student        # False — "Raj" is a value, not a key

classroom = {
    "Raj":   {"marks": 88, "grade": "A"},
    "Priya": {"marks": 92, "grade": "A"},
}
print(classroom["Raj"]["marks"])   # 88

# # PART 5: Marks Analyzer
# class_data = [("Raj", 88), ("Priya", 92), ("Amit", 61), ("Sneha", 79)]
# avg = sum(m for _, m in class_data) / len(class_data)
# above = [(n, m) for n, m in class_data if m > avg]
# print(f"Average: {avg:.1f}")
# print("Above average:", above)


# Given a list of (student_name, marks) tuples, return the
# names of students who scored strictly above the class average.
# Example: [("Raj",88),("Priya",92),("Amit",61)] → ["Raj","Priya"]

# PROBLEM OF THE SESSION — Session 2 (Replacement)
# You have two separate lists:
#   names  = ["Raj", "Priya", "Amit", "Sneha"]
#   marks  = [88, 92, 61, 79]
#
# Find the average mark.
# Print the names of students who scored above the average.
#
# Example output:
#   Average: 80.0
#   Above average: ['Raj', 'Priya']

# # PROBLEM SOLUTION
# data = [("Raj", 88), ("Priya", 92), ("Amit", 61), ("Sneha", 79)]
# avg = sum(m for _, m in data) / len(data)
# result = [name for name, marks in data if marks > avg]
# print(f"Average: {avg:.1f}")
# print("Above average:", result)

#SOLUTION:
print("--------------------------------solution--------------------------------")
names = ["Raj", "Priya", "Amit", "Sneha"]
marks = [88, 92, 61, 79]

avg = sum(marks) / len(marks)
print(f"Average: {avg:.1f}")

above = []
for i in range(len(names)):
    if marks[i] > avg:
        above.append(names[i])

print("Above average:", above)

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Given a sentence, count the frequency of each word and
# print the top 3 most common words in order.
