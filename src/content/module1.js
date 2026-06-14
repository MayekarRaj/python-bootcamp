export const module1 = {
  title: 'Module 1 — Python Foundations',
  subtitle: 'Sessions 1–2: Setup, basics, and core collections',
  sessions: [
    {
      sessionNumber: 1,
      title: 'Setup & Basics',
      topics: [
        'VS Code setup',
        'pip & venv',
        'Variables & data types',
        'Strings & f-strings',
        'Basic I/O',
      ],
      cheatsheet: [
        {
          concept: 'Variables',
          description:
            'No declaration needed, dynamic typing. Example: name = "Raj"; age = 22; cgpa = 8.4',
        },
        {
          concept: 'Data types',
          description: 'int, float, str, bool. Example: type(22) → int',
        },
        {
          concept: 'f-strings',
          description:
            'Cleanest way to format. Example: f"Hello {name}, you are {age} years old"',
        },
        {
          concept: 'String methods',
          description:
            '.upper(), .lower(), .strip(), .split(), .replace(). Example: "hello".upper() → "HELLO"',
        },
        {
          concept: 'Slicing',
          description:
            's[start:end:step]. Example: "Python"[0:3] → "Pyt"',
        },
      ],
      problem:
        "Given a sentence as input, return the most frequent word (ignore case). Example: 'the cat sat on the mat' → 'the'",
      takehome:
        "Write a program that takes a user's full name as input and prints: initials, name in reverse, and how many vowels are in the name.",
    },
    {
      sessionNumber: 2,
      title: 'Collections',
      topics: [
        'Lists',
        'Tuples',
        'Dicts',
        'Sets',
        'Creation, access, mutation',
        'Common methods',
      ],
      cheatsheet: [
        {
          concept: 'List',
          description:
            'Ordered, mutable. Example: marks = [88, 92, 74]; marks.append(95); marks.sort()',
        },
        {
          concept: 'Tuple',
          description:
            'Ordered, immutable — use for fixed data. Example: coords = (19.07, 72.87)',
        },
        {
          concept: 'Dict',
          description:
            'Key-value lookup table. Example: student = {"name": "Raj", "cgpa": 8.4}; student["cgpa"]',
        },
        {
          concept: 'Set',
          description:
            'Unordered, unique values. Example: {1,2,2,3} → {1,2,3}. Use for deduplication.',
        },
        {
          concept: 'Common dict methods',
          description: '.keys(), .values(), .items(), .get(key, default)',
        },
      ],
      problem:
        'Given a list of student name-mark tuples, return the names of students who scored above the class average.',
      takehome:
        'Given a sentence, count the frequency of each word and print the top 3 most common words.',
    },
  ],
}
