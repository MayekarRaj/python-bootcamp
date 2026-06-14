export const quickReference = [
  {
    id: 'builtins',
    title: 'Built-in Functions',
    items: [
      {
        name: 'print()',
        description: 'Print values to the console.',
        code: `print("Hello", "World", sep=", ")`,
      },
      {
        name: 'len()',
        description: 'Number of items in a sequence or collection.',
        code: `len([1, 2, 3])\n# → 3`,
      },
      {
        name: 'range()',
        description: 'Generates a sequence of numbers (lazy).',
        code: `list(range(0, 10, 2))\n# → [0, 2, 4, 6, 8]`,
      },
      {
        name: 'type()',
        description: 'Returns the type of an object.',
        code: `type(3.14)\n# → <class 'float'>`,
      },
      {
        name: 'int() / str() / float()',
        description: 'Convert between number and string types.',
        code: `int("42")    # → 42\nstr(42)      # → "42"\nfloat("3.14")  # → 3.14`,
      },
      {
        name: 'list() / dict() / set()',
        description: 'Convert an iterable into a list, dict, or set.',
        code: `list("abc")       # → ['a', 'b', 'c']\ndict(a=1, b=2)     # → {'a': 1, 'b': 2}\nset([1, 1, 2])     # → {1, 2}`,
      },
      {
        name: 'zip()',
        description: 'Pairs up elements from multiple iterables.',
        code: `list(zip([1, 2], ["a", "b"]))\n# → [(1, 'a'), (2, 'b')]`,
      },
      {
        name: 'enumerate()',
        description: 'Adds an index counter to an iterable.',
        code: `list(enumerate(["a", "b"]))\n# → [(0, 'a'), (1, 'b')]`,
      },
      {
        name: 'map()',
        description: 'Applies a function to every item of an iterable.',
        code: `list(map(str, [1, 2, 3]))\n# → ['1', '2', '3']`,
      },
      {
        name: 'filter()',
        description: 'Keeps items where the function returns True.',
        code: `list(filter(lambda x: x > 0, [-1, 0, 1]))\n# → [1]`,
      },
      {
        name: 'sorted()',
        description: 'Returns a new sorted list from an iterable.',
        code: `sorted([3, 1, 2])\n# → [1, 2, 3]`,
      },
      {
        name: 'max() / min()',
        description: 'Largest / smallest item in an iterable.',
        code: `max([3, 1, 2])  # → 3\nmin([3, 1, 2])  # → 1`,
      },
      {
        name: 'sum()',
        description: 'Adds up all items in an iterable.',
        code: `sum([1, 2, 3])\n# → 6`,
      },
      {
        name: 'abs()',
        description: 'Absolute (non-negative) value of a number.',
        code: `abs(-5)\n# → 5`,
      },
    ],
  },
  {
    id: 'string-methods',
    title: 'String Methods',
    items: [
      {
        name: '.upper() / .lower()',
        description: 'Convert to all uppercase or lowercase.',
        code: `"abc".upper()  # → "ABC"\n"ABC".lower()  # → "abc"`,
      },
      {
        name: '.strip()',
        description: 'Removes leading/trailing whitespace.',
        code: `"  hi  ".strip()\n# → "hi"`,
      },
      {
        name: '.split()',
        description: 'Splits a string into a list by a delimiter.',
        code: `"a,b,c".split(",")\n# → ['a', 'b', 'c']`,
      },
      {
        name: '.join()',
        description: 'Joins a list of strings using this string as glue.',
        code: `",".join(["a", "b", "c"])\n# → "a,b,c"`,
      },
      {
        name: '.replace()',
        description: 'Replaces all occurrences of a substring.',
        code: `"hello".replace("l", "L")\n# → "heLLo"`,
      },
      {
        name: '.find()',
        description: 'Index of first match, or -1 if not found.',
        code: `"hello".find("l")\n# → 2`,
      },
      {
        name: '.startswith() / .endswith()',
        description: 'Check if a string starts or ends with a substring.',
        code: `"hello".startswith("he")  # → True\n"hello".endswith("lo")    # → True`,
      },
      {
        name: '.format()',
        description: 'Old-style string formatting with placeholders.',
        code: `"{} is {}".format("Raj", 22)\n# → "Raj is 22"`,
      },
      {
        name: 'f-strings',
        description: 'Inline expression formatting — the modern way.',
        code: `name, age = "Raj", 22\nf"{name} is {age} years old"`,
      },
    ],
  },
  {
    id: 'list-methods',
    title: 'List Methods',
    items: [
      {
        name: '.append()',
        description: 'Add a single item to the end.',
        code: `nums.append(4)`,
      },
      {
        name: '.extend()',
        description: 'Add multiple items from another iterable.',
        code: `nums.extend([5, 6])`,
      },
      {
        name: '.insert()',
        description: 'Insert an item at a given index.',
        code: `nums.insert(0, -1)`,
      },
      {
        name: '.remove()',
        description: 'Remove the first matching value.',
        code: `nums.remove(3)`,
      },
      {
        name: '.pop()',
        description: 'Remove & return item at index (default: last).',
        code: `nums.pop()    # last item\nnums.pop(0)   # first item`,
      },
      {
        name: '.sort() / .reverse()',
        description: 'Sort or reverse the list in place.',
        code: `nums.sort(reverse=True)\nnums.reverse()`,
      },
      {
        name: '.index()',
        description: 'Index of the first matching value.',
        code: `nums.index(3)\n# → index of first 3`,
      },
      {
        name: '.count()',
        description: 'Number of times a value appears.',
        code: `nums.count(3)\n# → number of 3s`,
      },
      {
        name: '.copy()',
        description: 'Shallow copy of the list.',
        code: `nums2 = nums.copy()`,
      },
    ],
  },
  {
    id: 'dict-methods',
    title: 'Dict Methods',
    items: [
      {
        name: '.keys()',
        description: 'View of all keys.',
        code: `d.keys()\n# → dict_keys(['a', 'b'])`,
      },
      {
        name: '.values()',
        description: 'View of all values.',
        code: `d.values()\n# → dict_values([1, 2])`,
      },
      {
        name: '.items()',
        description: 'View of (key, value) pairs.',
        code: `d.items()\n# → dict_items([('a', 1), ('b', 2)])`,
      },
      {
        name: '.get()',
        description: 'Safe lookup with a default if key is missing.',
        code: `d.get("c", 0)\n# → 0 if "c" not in d`,
      },
      {
        name: '.update()',
        description: 'Merge another dict (or kwargs) into this one.',
        code: `d.update({"c": 3})`,
      },
      {
        name: '.pop()',
        description: 'Remove a key and return its value.',
        code: `d.pop("a")\n# → value that was at "a"`,
      },
      {
        name: '.setdefault()',
        description: 'Get a key, inserting a default if it is missing.',
        code: `d.setdefault("tags", []).append("new")`,
      },
    ],
  },
  {
    id: 'file-modes',
    title: 'File Modes',
    items: [
      {
        name: '"r"',
        description: 'Read (default). The file must already exist.',
        code: `open("data.txt", "r")`,
      },
      {
        name: '"w"',
        description: 'Write. Creates the file or overwrites existing content.',
        code: `open("data.txt", "w")`,
      },
      {
        name: '"a"',
        description: 'Append. Creates the file if missing, writes go to the end.',
        code: `open("data.txt", "a")`,
      },
      {
        name: '"rb"',
        description: 'Read binary. For non-text files like images or PDFs.',
        code: `open("image.png", "rb")`,
      },
      {
        name: '"wb"',
        description: 'Write binary. Overwrites the file with binary data.',
        code: `open("image.png", "wb")`,
      },
    ],
  },
  {
    id: 'exceptions',
    title: 'Exception Types',
    items: [
      {
        name: 'ValueError',
        description: 'A value has the right type but an invalid value.',
        code: `int("abc")\n# ValueError: invalid literal`,
      },
      {
        name: 'TypeError',
        description: 'An operation is applied to an incompatible type.',
        code: `"2" + 2\n# TypeError: can only concatenate str`,
      },
      {
        name: 'KeyError',
        description: 'A dict key does not exist.',
        code: `{"a": 1}["b"]\n# KeyError: 'b'`,
      },
      {
        name: 'IndexError',
        description: 'A list index is out of range.',
        code: `[1, 2, 3][5]\n# IndexError: list index out of range`,
      },
      {
        name: 'FileNotFoundError',
        description: 'The file path passed to open() does not exist.',
        code: `open("missing.txt")\n# FileNotFoundError`,
      },
      {
        name: 'AttributeError',
        description: 'An object has no such attribute or method.',
        code: `"abc".append("d")\n# AttributeError: 'str' object has no attribute 'append'`,
      },
    ],
  },
  {
    id: 'comprehensions',
    title: 'Comprehension Patterns',
    items: [
      {
        name: 'List comprehension',
        description: 'Build a new list by transforming each item.',
        code: `[x * 2 for x in range(5)]\n# → [0, 2, 4, 6, 8]`,
      },
      {
        name: 'Dict comprehension',
        description: 'Build a dict from key/value expressions.',
        code: `{x: x * 2 for x in range(3)}\n# → {0: 0, 1: 2, 2: 4}`,
      },
      {
        name: 'Set comprehension',
        description: 'Build a set of unique computed values.',
        code: `{x % 3 for x in range(10)}\n# → {0, 1, 2}`,
      },
      {
        name: 'Conditional comprehension',
        description: 'Filter items while building the new collection.',
        code: `[x for x in range(10) if x % 2 == 0]\n# → [0, 2, 4, 6, 8]`,
      },
    ],
  },
  {
    id: 'oop',
    title: 'OOP Quick Reference',
    items: [
      {
        name: 'class',
        description: 'Defines a new object blueprint (type).',
        code: `class Dog:
    sound = "Woof"`,
      },
      {
        name: '__init__',
        description: 'Constructor — runs automatically when an object is created.',
        code: `def __init__(self, name):
    self.name = name`,
      },
      {
        name: 'self',
        description: 'Refers to the current instance; always the first parameter.',
        code: `def bark(self):
    print(f"{self.name} says Woof")`,
      },
      {
        name: 'Inheritance',
        description: "A child class inherits its parent's attributes & methods.",
        code: `class Puppy(Dog):
    pass`,
      },
      {
        name: 'super()',
        description: "Calls the parent class's method, usually in __init__.",
        code: `def __init__(self, name, age):
    super().__init__(name)`,
      },
      {
        name: '@property',
        description: 'Lets a method be accessed like a plain attribute.',
        code: `@property
def age_in_months(self):
    return self.age * 12`,
      },
      {
        name: '@classmethod',
        description: 'Receives the class (cls) — useful for alternate constructors.',
        code: `@classmethod
def from_string(cls, s):
    return cls(*s.split(","))`,
      },
      {
        name: '@staticmethod',
        description: 'A utility function with no access to self or cls.',
        code: `@staticmethod
def is_valid_name(name):
    return len(name) > 0`,
      },
    ],
  },
]
