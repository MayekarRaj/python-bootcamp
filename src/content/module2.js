export const module2 = {
  title: 'Module 2 — Intermediate Python',
  subtitle:
    'Sessions 3–6: Control flow, functions, comprehensions, file I/O, and APIs',
  sessions: [
    {
      sessionNumber: 3,
      title: 'Control Flow, Functions & Comprehensions',
      topics: [
        'if/elif/else',
        'for/while loops',
        'Functions',
        'List comprehensions',
        'Dict comprehensions',
      ],
      cheatsheet: [
        {
          concept: 'Function definition',
          description:
            'def greet(name, greeting="Hello"): return f"{greeting}, {name}!"',
        },
        {
          concept: '*args',
          description:
            'Accepts any number of positional args as a tuple. Example: def total(*nums): return sum(nums)',
        },
        {
          concept: 'List comprehension',
          description:
            '[expr for item in iterable if condition]. Example: [x**2 for x in range(10) if x % 2 == 0]',
        },
        {
          concept: 'Dict comprehension',
          description:
            '{k: v for k, v in items}. Example: {name: len(name) for name in ["Raj", "Priya"]}',
        },
        {
          concept: 'Loop control',
          description: 'break exits loop, continue skips to next iteration',
        },
      ],
      problem:
        'Flatten a nested list using list comprehension only. Example: [[1,2],[3,4],[5]] → [1,2,3,4,5]',
      takehome:
        'Using dict comprehension, create a word-length dictionary from a sentence, then filter to words longer than 4 characters.',
    },
    {
      sessionNumber: 4,
      title: 'Intermediate Concepts',
      topics: [
        '*args',
        '**kwargs',
        'lambda',
        'Generators (basic)',
        'enumerate',
        'zip',
      ],
      cheatsheet: [
        {
          concept: '**kwargs',
          description:
            'Accepts keyword args as a dict. Example: def profile(**info): print(info["name"])',
        },
        {
          concept: 'lambda',
          description:
            'Anonymous one-line function. Example: sorted(students, key=lambda s: s["cgpa"], reverse=True)',
        },
        {
          concept: 'map/filter with lambda',
          description: 'list(filter(lambda x: x > 40, scores))',
        },
        {
          concept: 'Generator',
          description:
            'Uses yield, memory efficient for large sequences. Example: def counter(n): for i in range(n): yield i',
        },
        {
          concept: 'enumerate',
          description:
            'for i, val in enumerate(items) — gives index and value together',
        },
        {
          concept: 'zip',
          description:
            'for a, b in zip(list1, list2) — pairs elements from two lists',
        },
      ],
      problem:
        'Write a function that takes any number of scores and returns only passing ones (≥40), sorted descending. Use *args and filter with lambda.',
      takehome:
        'Use zip to combine a list of student names and marks into a dict, then use a generator to yield only students who passed.',
    },
    {
      sessionNumber: 5,
      title: 'File I/O, Exceptions, JSON',
      topics: [
        'try/except/finally',
        'Custom exceptions',
        'open() for read/write',
        'JSON load/dump',
        'CSV with csv module',
      ],
      cheatsheet: [
        {
          concept: 'try/except',
          description:
            'try: risky_code() except FileNotFoundError as e: print(e) finally: print("always runs")',
        },
        {
          concept: 'File read',
          description:
            'with open("file.txt", "r") as f: content = f.read() — always use with, it auto-closes',
        },
        {
          concept: 'File write',
          description:
            'with open("out.txt", "w") as f: f.write("hello") — "w" overwrites, "a" appends',
        },
        {
          concept: 'JSON',
          description:
            'import json; data = json.load(f) to read; json.dump(data, f, indent=2) to write',
        },
        {
          concept: 'CSV',
          description:
            'import csv; reader = csv.DictReader(f) — gives each row as a dict with column headers as keys',
        },
      ],
      problem:
        'Read a CSV file of student records. Handle missing or malformed rows gracefully. Print only valid records sorted by marks.',
      takehome:
        "Read a JSON config file, modify one value, and write it back. Handle the case where the file doesn't exist.",
    },
    {
      sessionNumber: 6,
      title: 'Regex, Collections, requests',
      topics: [
        're module basics',
        'Counter',
        'defaultdict',
        'requests library',
        'API JSON parsing',
      ],
      cheatsheet: [
        {
          concept: 're.findall(pattern, string)',
          description:
            'Returns all matches as list. Example: re.findall(r"\\d+", "score: 92 and 88") → ["92","88"]',
        },
        {
          concept: 're.sub(pattern, replacement, string)',
          description: 'Replace matches',
        },
        {
          concept: 'Common patterns',
          description:
            '\\d+ for digits, \\w+ for words, \\s for whitespace, ^ start, $ end',
        },
        {
          concept: 'Counter',
          description:
            'from collections import Counter; Counter(["a","b","a"]) → {"a":2,"b":1}; .most_common(3)',
        },
        {
          concept: 'defaultdict',
          description:
            'Never raises KeyError. Example: from collections import defaultdict; d = defaultdict(list); d["key"].append(1)',
        },
        {
          concept: 'requests',
          description:
            'import requests; r = requests.get(url); r.json() to parse response; r.status_code to check',
        },
      ],
      problem:
        'From a multiline log string, use regex and Counter to count occurrences of each error code (format: ERROR_XXX).',
      takehome:
        'Call the GitHub API (https://api.github.com/users/YOUR_USERNAME), extract name, public repos count, and followers, print them formatted.',
    },
  ],
}
