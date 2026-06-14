# ============================================================
# SESSION 6: Regex, Collections & requests API
# Day 3 Afternoon | 2:00 PM – 5:00 PM
# Topics: re module, Counter, defaultdict, requests
# ============================================================
# NOTE: Run `pip install requests` before this session if not done
# ============================================================


# ── PART 1: Regex basics ────────────────────────────────────
# Type here live:




# ── PART 2: re.sub — cleaning data ──────────────────────────
# Type here live:




# ── PART 3: Email validation ────────────────────────────────
# Type here live:




# ── PART 4: Counter ─────────────────────────────────────────
# Type here live:




# ── PART 5: defaultdict ─────────────────────────────────────
# Type here live:




# ── PART 6: requests — live API call ────────────────────────
# Type here live:




# ── PART 7: Log Analyzer (guided exercise) ──────────────────
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Given a multiline log string, use regex to extract all error
# codes in format ERROR_XXX (where XXX is digits).
# Use Counter to count occurrences. Print most common first.
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: Regex basics
# import re
#
# text = "My phone is 9876543210 and backup is 9123456789"
# phones = re.findall(r"\d{10}", text)
# print(phones)    # ['9876543210', '9123456789']
#
# # Extract all numbers (any length)
# text2 = "Order 123 has 45 items worth 6789 rupees"
# nums = re.findall(r"\d+", text2)
# print(nums)      # ['123', '45', '6789']
#
# # re.search — finds first match, returns match object
# match = re.search(r"\d+", text2)
# if match:
#     print(match.group())   # '123'

# # PART 2: re.sub — cleaning data
# dirty = "Hello!!!  World???"
# clean = re.sub(r"[^a-zA-Z ]", "", dirty)
# print(clean)    # "Hello  World"
#
# # Remove extra spaces
# messy = "too   many    spaces"
# fixed = re.sub(r"\s+", " ", messy).strip()
# print(fixed)    # "too many spaces"

# # PART 3: Email validation
# def is_valid_email(email):
#     pattern = r"^[\w.+-]+@[\w-]+\.[a-z]{2,}$"
#     return bool(re.match(pattern, email))
#
# print(is_valid_email("raj@example.com"))    # True
# print(is_valid_email("not-an-email"))       # False
# print(is_valid_email("raj@.com"))           # False

# # PART 4: Counter
# from collections import Counter
#
# words = ["python", "java", "python", "go", "python", "java"]
# c = Counter(words)
# print(c)                    # Counter({'python': 3, 'java': 2, 'go': 1})
# print(c.most_common(2))     # [('python', 3), ('java', 2)]
# print(c["python"])          # 3
# print(c["ruby"])            # 0 — no KeyError!
#
# # Counter on a string
# letter_count = Counter("mississippi")
# print(letter_count.most_common(3))

# # PART 5: defaultdict
# from collections import defaultdict
#
# # Regular dict raises KeyError on missing key
# # d = {}; d["key"].append(1)  ← KeyError!
#
# # defaultdict creates a default value automatically
# scores = defaultdict(list)
# scores["Raj"].append(88)
# scores["Raj"].append(92)
# scores["Priya"].append(79)
# print(dict(scores))
#
# # defaultdict(int) for counting
# word_count = defaultdict(int)
# for word in ["a", "b", "a", "c", "a", "b"]:
#     word_count[word] += 1
# print(dict(word_count))

# # PART 6: requests
# import requests
#
# url = "https://api.github.com/users/torvalds"
# response = requests.get(url)
# print(response.status_code)   # 200
#
# data = response.json()
# print(f"Name        : {data['name']}")
# print(f"Public repos: {data['public_repos']}")
# print(f"Followers   : {data['followers']}")
#
# # Error handling
# try:
#     r = requests.get("https://api.github.com/users/torvalds", timeout=5)
#     r.raise_for_status()   # raises exception for 4xx/5xx
#     print(r.json()["login"])
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")

# # PART 7: Log Analyzer (guided)
# import re
# from collections import Counter
#
# log = """2024-01-15 ERROR_404 page not found
# 2024-01-15 ERROR_500 internal server error
# 2024-01-16 ERROR_404 another missing page
# 2024-01-16 ERROR_200 ok
# 2024-01-16 ERROR_404 yet another 404"""
#
# codes = re.findall(r"ERROR_\d+", log)
# print(Counter(codes).most_common())

# # PROBLEM SOLUTION
# import re
# from collections import Counter
#
# log = """
# 2024-01-15 10:23 ERROR_404 Not Found
# 2024-01-15 10:45 ERROR_500 Server Error
# 2024-01-16 09:10 ERROR_404 Not Found
# 2024-01-16 11:30 ERROR_200 OK
# 2024-01-17 08:55 ERROR_404 Not Found
# 2024-01-17 09:00 ERROR_500 Server Error
# """
#
# codes = re.findall(r"ERROR_\d+", log)
# freq = Counter(codes)
# for code, count in freq.most_common():
#     print(f"{code}: {count} occurrences")

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Call the GitHub API with YOUR username:
# https://api.github.com/users/YOUR_USERNAME
# Extract name, public repos count, and followers.
# Print them formatted. Handle the case where request fails.
