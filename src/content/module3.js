export const module3 = {
  title: 'Module 3 — Object-Oriented Programming',
  subtitle: 'Sessions 7–8: Classes, objects, inheritance, and Git basics',
  sessions: [
    {
      sessionNumber: 7,
      title: 'OOP Part 1',
      topics: [
        'Classes & objects',
        '__init__',
        'self',
        'Instance variables',
        'Encapsulation',
        '__str__ & __repr__',
      ],
      cheatsheet: [
        {
          concept: 'Class definition',
          description:
            'class BankAccount: def __init__(self, owner, balance=0): self.owner = owner; self._balance = balance',
        },
        {
          concept: 'self',
          description:
            'Refers to the current instance — always the first parameter of instance methods',
        },
        {
          concept: '__str__',
          description:
            'Controls print(obj) output. Example: def __str__(self): return f"Account({self.owner}: ₹{self._balance})"',
        },
        {
          concept: 'Encapsulation',
          description:
            'Prefix with _ to signal "private". Use @property for controlled access.',
        },
        {
          concept: '@property',
          description:
            'Lets you access a method like an attribute. Example: @property def balance(self): return self._balance',
        },
      ],
      problem:
        'Build a BankAccount class with deposit(amount), withdraw(amount) with overdraft protection, and a __str__ that prints owner name and balance.',
      takehome:
        'Add a transaction_history list to BankAccount that records every deposit and withdrawal with the amount and running balance.',
    },
    {
      sessionNumber: 8,
      title: 'OOP Part 2 + Git',
      topics: [
        'Inheritance',
        'super()',
        'Polymorphism',
        'classmethod',
        'staticmethod',
        'Git basics',
      ],
      cheatsheet: [
        {
          concept: 'Inheritance',
          description:
            'class SavingsAccount(BankAccount): def __init__(self, owner): super().__init__(owner)',
        },
        {
          concept: 'super()',
          description:
            'Calls parent class method. Always call in child __init__ to initialize parent attributes.',
        },
        {
          concept: 'Polymorphism',
          description:
            'Same method name, different behavior per class. Example: each Shape subclass has its own area()',
        },
        {
          concept: '@classmethod',
          description:
            'Takes cls as first arg, can create alternative constructors. Example: @classmethod def from_dict(cls, data)',
        },
        {
          concept: '@staticmethod',
          description:
            'No self or cls — utility function that lives in the class namespace',
        },
        {
          concept: 'Git basics',
          description:
            'git init → git add . → git commit -m "message" → git remote add origin URL → git push',
        },
      ],
      problem:
        'Build a Shape base class with area() and perimeter(). Extend to Circle and Rectangle. Use __str__ via dunder to print shape description with calculated area.',
      takehome:
        'Add a Triangle subclass to Shape. Push your entire OOP session code to a new GitHub repo.',
    },
  ],
}
