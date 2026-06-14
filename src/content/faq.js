export const faqSections = [
  {
    id: 'python-installation',
    icon: '🐍',
    title: 'Python Installation',
    items: [
      {
        question: 'python command not found in terminal',
        answer:
          'On Mac, try python3 instead of python. On Windows, reinstall Python from python.org and check "Add Python to PATH" during installation. Then restart your terminal.',
      },
      {
        question:
          'I have multiple Python versions installed — which one runs?',
        answer:
          'Type "which python3" (Mac/Linux) or "where python" (Windows) to see the path. Use python3 explicitly if unsure.',
      },
      {
        question: 'pip command not found',
        answer:
          'Try pip3 instead of pip. If that fails: python3 -m pip install packagename. On Windows: py -m pip install packagename.',
      },
    ],
  },
  {
    id: 'vscode-setup',
    icon: '🧰',
    title: 'VS Code Setup',
    items: [
      {
        question:
          'VS Code doesn\'t recognise Python — shows import errors on valid code',
        answer:
          'Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows), type "Python: Select Interpreter", choose the Python 3.x version from the list. If none appear, install the Python extension from the Extensions panel first.',
      },
      {
        question:
          'Terminal in VS Code says "python not found" but it works in my system terminal',
        answer:
          'The VS Code terminal uses a different PATH. Open settings, search "terminal integrated env", and add your Python path. Easier fix: use the system terminal for running files.',
      },
      {
        question: "My file runs but print() output doesn't show",
        answer:
          'Make sure you saved the file (Cmd+S / Ctrl+S). Check you\'re running the right file — look at the terminal command, it should say "python3 yourfile.py".',
      },
    ],
  },
  {
    id: 'virtual-environments',
    icon: '📦',
    title: 'Virtual Environments',
    items: [
      {
        question: 'How do I create and activate a venv?',
        answer:
          'Create: python3 -m venv venv\nActivate Mac/Linux: source venv/bin/activate\nActivate Windows: venv\\Scripts\\activate\nYou\'ll see (venv) in your terminal when it\'s active.',
      },
      {
        question: 'pip install works but import still fails',
        answer:
          'Your venv is probably not activated. Look for (venv) at the start of your terminal line. If it\'s missing, activate it first, then install again.',
      },
      {
        question: 'I accidentally installed packages globally instead of in venv',
        answer:
          "That's okay for now — it still works. Just activate your venv next time before installing.",
      },
    ],
  },
  {
    id: 'common-errors',
    icon: '⚠️',
    title: 'Common Python Errors',
    items: [
      {
        question: 'SyntaxError: invalid syntax',
        answer:
          "Python found something it couldn't understand. Check: missing colon after if/for/def, unclosed bracket or quote, = instead of == in a condition. The error line number is your starting point.",
      },
      {
        question: 'IndentationError: unexpected indent',
        answer:
          'Python uses indentation to define blocks. Don\'t mix tabs and spaces. In VS Code, the bottom right corner shows "Spaces: 4" — keep it consistent. Select all and use Format Document (Shift+Alt+F) to auto-fix.',
      },
      {
        question: "NameError: name 'x' is not defined",
        answer:
          'You used a variable before creating it, or misspelled it. Python is case-sensitive: name and Name are different variables.',
      },
      {
        question: 'TypeError: can only concatenate str (not int) to str',
        answer:
          'You\'re trying to join a string and a number with +. Use an f-string instead: f"I am {age} years old" instead of "I am " + age.',
      },
      {
        question: "ModuleNotFoundError: No module named 'requests'",
        answer:
          'The package isn\'t installed. Run: pip3 install requests. Make sure your venv is activated first if you\'re using one.',
      },
      {
        question: 'IndexError: list index out of range',
        answer:
          'You\'re accessing an index that doesn\'t exist. A list with 3 items has indices 0, 1, 2. Use len(mylist) to check before accessing.',
      },
    ],
  },
  {
    id: 'file-path-issues',
    icon: '📁',
    title: 'File & Path Issues',
    items: [
      {
        question: 'FileNotFoundError when reading a CSV or text file',
        answer:
          'Python looks for the file relative to where your script is. Either put the file in the same folder as your .py file, or use the full path. Print your current directory with: import os; print(os.getcwd())',
      },
      {
        question: 'My CSV has weird characters / UnicodeDecodeError',
        answer:
          'Add an encoding parameter: open("file.csv", "r", encoding="utf-8"). If that fails, try encoding="utf-8-sig" or encoding="latin-1".',
      },
    ],
  },
  {
    id: 'jupyter-notebooks',
    icon: '📓',
    title: 'Jupyter / Notebook Issues',
    items: [
      {
        question: "We're not using Jupyter in this bootcamp",
        answer:
          'All sessions use plain .py files in VS Code with the terminal. If you want to try Jupyter later, install with: pip3 install jupyter',
      },
    ],
  },
]
