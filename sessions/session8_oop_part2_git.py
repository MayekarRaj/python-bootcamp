# ============================================================
# SESSION 8: OOP Part 2 — Inheritance, Polymorphism & Git
# Day 4 Afternoon | 2:00 PM – 5:00 PM
# Topics: inheritance, super(), polymorphism, classmethod,
#         staticmethod, Git basics
# ============================================================
# Extends Session 7's BankAccount — paste or import that class
# at the top before starting, or redefine a minimal version.
# ============================================================


class SavingsAccount(BankAccount):   # SavingsAccount inherits BankAccount
    pass

sa = SavingsAccount("Priya", 5000)
sa.deposit(1000)    # inherited from BankAccount — works immediately
print(sa)           # Account[Priya]: ₹6,000.00 — inherited __str__



class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)   # MUST be first line
        self.interest_rate = interest_rate  # child-specific attribute

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)   # inherited method
        return interest

    def __str__(self):
        return f"SavingsAccount[{self.owner}]: ₹{self._balance:,.2f} @ {self.interest_rate*100:.0f}%"



#broken
class BrokenSavings(BankAccount):
    def __init__(self, owner):
        self.interest_rate = 0.04
        # forgot super().__init__()

bs = BrokenSavings("Raj")
bs.deposit(100)   # AttributeError: '_balance' not found
                  # because BankAccount.__init__ never ran


#Method Overriding
class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=5000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):    # overrides BankAccount.withdraw
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance -= amount    # allows negative balance up to limit

    def __str__(self):
        return f"CurrentAccount[{self.owner}]: ₹{self._balance:,.2f} (limit: ₹{self.overdraft_limit:,})"


ca = CurrentAccount("Raj", 1000, overdraft_limit=5000)
ca.withdraw(4000)   # takes balance to -3000 — allowed
print(ca)           # CurrentAccount[Raj]: ₹-3,000.00 (limit: ₹5,000)



#POLYMORPHISM
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")
    def __str__(self):
        return f"{type(self).__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f"Circle: r={self.radius}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
    def __str__(self):
        return f"Rectangle: {self.w}x{self.h}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for s in shapes:
    print(s)    # each responds differently — same call




# ── BASE CLASS (paste from Session 7 or redefine minimal) ───
# Type here live:

Real World Analogy
Think of a Bank as the class, and your account as the instance:

Regular method → "Check my balance" — specific to your account

@classmethod → "What is the bank's name?" 
— same answer for every account

@staticmethod → "Is this a valid PIN format?" 
— has nothing to do with any account, just a rule

Python's lookup order: instance → class → parent class


class BankAccount:
    bank_name = "HDFC"

    def change_bank(self):
        self.bank_name = "SBI"  # ⚠️ looks like you're changing the class variable

acc1 = BankAccount()
acc2 = BankAccount()

acc1.change_bank()

print(acc1.bank_name)           # "SBI"  — acc1 has its own copy now
print(acc2.bank_name)           # "HDFC" — class variable unchanged!
print(BankAccount.bank_name)    # "HDFC" — class variable unchanged!
class BankAccount:
    bank_name = "HDFC"

    def change_bank(self):
        BankAccount.bank_name = "SBI"   # ✅ actually modifies the class variable

#classmethod
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data_string):
        # "Raj,88" → Student("Raj", 88)
        name, marks = data_string.split(",")
        return cls(name, int(marks))

    @classmethod
    def from_dict(cls, data_dict):
        # {"name": "Raj", "marks": 88} → Student("Raj", 88)
        return cls(data_dict["name"], data_dict["marks"])

s1 = Student("Raj", 88)                    # regular constructor
s2 = Student.from_string("Priya,92")       # alternative constructor
s3 = Student.from_dict({"name":"Amit","marks":74})


class BankAccount:
    bank_name = "HDFC"              # class variable — shared by ALL instances

    @classmethod
    def get_bank(cls):              # cls = the CLASS itself, not an instance
        return cls.bank_name

print(BankAccount.get_bank())       # ✅ "HDFC" — called on class
acc = BankAccount("Raj", 1500)
print(acc.get_bank())               # ✅ also works — called on instance

#staticmethod
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def is_passing(marks):
        return marks >= 40

    @staticmethod
    def get_grade(marks):
        if marks >= 90: return "A"
        elif marks >= 75: return "B"
        elif marks >= 60: return "C"
        elif marks >= 40: return "D"
        else: return "F"

print(Student.is_passing(38))    # False
print(Student.get_grade(88))     # B

# ── PART 1: Inheritance — SavingsAccount ────────────────────
# Type here live:




# ── PART 2: Inheritance — CurrentAccount (with overdraft) ───
# Type here live:




# ── PART 3: Polymorphism — Shape hierarchy ──────────────────
# Type here live:




# ── PART 4: classmethod and staticmethod ────────────────────
# Type here live:




# ── PART 5: GIT — type these commands in your terminal ──────
# (Not Python — open a new terminal window)
#
# git init
# git add .
# git commit -m "Add OOP session code"
# git remote add origin https://github.com/YOUR_USERNAME/python-bootcamp.git
# git push -u origin main


# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Build a Shape base class with area() and perimeter().
# Extend to Circle and Rectangle.
# Use __str__ to print: "Circle: radius=5, area=78.54, perimeter=31.42"
# Create a list of mixed shapes and print each polymorphically.
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # MINIMAL BASE FROM SESSION 7
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance
#         self.transaction_history = []
#     def deposit(self, amount):
#         self._balance += amount
#         self.transaction_history.append(f"+{amount}")
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError("Insufficient funds")
#         self._balance -= amount
#     @property
#     def balance(self): return self._balance
#     def __str__(self): return f"Account[{self.owner}]: ₹{self._balance:,.2f}"

# # PART 1: SavingsAccount
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=0.04):
#         super().__init__(owner, balance)   # MUST call super().__init__()
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         interest = self._balance * self.interest_rate
#         self.deposit(interest)
#         return interest
#
#     def __str__(self):
#         return f"SavingsAccount[{self.owner}]: ₹{self._balance:,.2f} @ {self.interest_rate*100:.0f}%"
#
# sa = SavingsAccount("Priya", 10000)
# print(sa)
# sa.add_interest()
# print(sa)

# # PART 2: CurrentAccount (overdraft allowed)
# class CurrentAccount(BankAccount):
#     def __init__(self, owner, balance=0, overdraft_limit=5000):
#         super().__init__(owner, balance)
#         self.overdraft_limit = overdraft_limit
#
#     def withdraw(self, amount):    # overrides parent method
#         if amount > self._balance + self.overdraft_limit:
#             raise ValueError("Exceeds overdraft limit")
#         self._balance -= amount
#
#     def __str__(self):
#         return f"CurrentAccount[{self.owner}]: ₹{self._balance:,.2f} (limit: ₹{self.overdraft_limit:,})"
#
# ca = CurrentAccount("Raj", 1000, overdraft_limit=5000)
# ca.withdraw(4000)   # takes balance to -3000, allowed
# print(ca)

# # PART 3: Polymorphism — Shape
# import math
#
# class Shape:
#     def area(self): raise NotImplementedError("Subclass must implement area()")
#     def perimeter(self): raise NotImplementedError("Subclass must implement perimeter()")
#     def __str__(self): return f"{type(self).__name__}: area={self.area():.2f}"
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self): return math.pi * self.radius ** 2
#     def perimeter(self): return 2 * math.pi * self.radius
#     def __str__(self):
#         return f"Circle: radius={self.radius}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"
#
# class Rectangle(Shape):
#     def __init__(self, w, h):
#         self.w, self.h = w, h
#     def area(self): return self.w * self.h
#     def perimeter(self): return 2 * (self.w + self.h)
#     def __str__(self):
#         return f"Rectangle: {self.w}x{self.h}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"
#
# shapes = [Circle(5), Rectangle(4, 6), Circle(3), Rectangle(10, 2)]
# for s in shapes:
#     print(s)   # same call, different output — that's polymorphism

# # PART 4: classmethod + staticmethod
# class Student:
#     school = "VPCOE"
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     @classmethod
#     def from_string(cls, data_string):
#         # Alternative constructor: "Raj,88" → Student("Raj", 88)
#         name, marks = data_string.split(",")
#         return cls(name, int(marks))
#
#     @staticmethod
#     def is_passing(marks):
#         # Utility — belongs here but needs no instance or class
#         return marks >= 40
#
# s1 = Student.from_string("Priya,92")
# print(s1.name, s1.marks)
# print(Student.is_passing(38))   # False

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Add a Triangle subclass to Shape with sides a, b, c.
# Use Heron's formula for area.
# Push your entire OOP code (sessions 7 + 8) to a new
# GitHub repo called "python-oop-practice".
