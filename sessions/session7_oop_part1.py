# ============================================================
# SESSION 7: OOP Part 1 — Classes, Encapsulation & Dunders
# Day 4 Morning | 10:00 AM – 1:00 PM
# Topics: class, __init__, self, @property, __str__, __repr__
# ============================================================
# Build BankAccount incrementally — add one piece at a time.
# Do NOT write the full class at once. Students follow each step.
# ============================================================


# ── STEP 1: Empty class + __init__ ──────────────────────────
# Type here live:




# -- STEP 1 REFERENCE --
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance   # _underscore = convention for "private"
#
# acc = BankAccount("Raj", 1000)
# print(acc.owner)      # Raj
# print(acc._balance)   # 1000


# ── STEP 2: deposit() method ────────────────────────────────
# Type here live:




# -- STEP 2 REFERENCE --
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self._balance += amount
#         return self._balance
#
# acc = BankAccount("Raj", 1000)
# acc.deposit(500)
# print(acc._balance)   # 1500
# acc.deposit(-100)     # raises ValueError


# ── STEP 3: withdraw() with overdraft protection ─────────────
# Type here live:




# -- STEP 3 REFERENCE --
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self._balance += amount
#         return self._balance
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError(
#                 f"Cannot withdraw Rs.{amount}. Balance: Rs.{self._balance}"
#             )
#         self._balance -= amount
#         return self._balance
#
# acc = BankAccount("Raj", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc._balance)   # 1300
# acc.withdraw(5000)    # raises ValueError


# ── STEP 4: @property for read-only balance ─────────────────
# Type here live:




# -- STEP 4 REFERENCE --
# (Add this inside the class, after withdraw)
#
#     @property
#     def balance(self):
#         return self._balance
#
# acc = BankAccount("Raj", 1000)
# acc.deposit(500)
# print(acc.balance)    # 1500 — accessed like attribute, not method
# acc.balance = 9999    # raises AttributeError — read-only, good!


# ── STEP 5: __str__ and __repr__ ────────────────────────────
# Type here live:




# -- STEP 5 REFERENCE --
# (Add these inside the class, after balance property)
#
#     def __str__(self):
#         # Controls what print(acc) shows — human readable
#         return f"Account[{self.owner}]: Rs.{self._balance:,.2f}"
#
#     def __repr__(self):
#         # Controls what the REPL shows — developer readable
#         return f"BankAccount(owner={self.owner!r}, balance={self._balance})"
#
# acc = BankAccount("Raj", 1000)
# print(acc)       # Account[Raj]: Rs.1,000.00   <- uses __str__
# repr(acc)        # BankAccount(owner='Raj', balance=1000) <- uses __repr__
#
# # Show the difference: without __str__, print() shows something like:
# # <__main__.BankAccount object at 0x10f3a2d90>


# ── STEP 6: transaction_history ─────────────────────────────
# Type here live:




# -- STEP 6 REFERENCE --
# IMPORTANT: transaction_history MUST be initialised in __init__,
# not as a class variable. Show the BrokenAccount bug here.
#
# (Update __init__ and deposit/withdraw inside the class)
#
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance
#         self.transaction_history = []   # <- instance variable, not class variable
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self._balance += amount
#         self.transaction_history.append(f"+{amount}")
#         return self._balance
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError(
#                 f"Cannot withdraw Rs.{amount}. Balance: Rs.{self._balance}"
#             )
#         self._balance -= amount
#         self.transaction_history.append(f"-{amount}")
#         return self._balance
#
# acc = BankAccount("Raj", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc.transaction_history)   # ['+500', '-200']
#
# --- THE CLASS VARIABLE BUG — show this to the class ---
# class BrokenAccount:
#     history = []   # <- WRONG: shared across ALL instances
#     def __init__(self, owner):
#         self.owner = owner
#
# a1 = BrokenAccount("Raj")
# a2 = BrokenAccount("Priya")
# a1.history.append("deposit")
# print(a2.history)   # ['deposit'] <- Priya sees Raj's history — BUG


# ── TEST YOUR CLASS ─────────────────────────────────────────
# Type test calls here as you build each step:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Build a BankAccount class with:
#   - __init__(owner, initial_balance=0)
#   - deposit(amount): adds money, raises ValueError if amount <= 0
#   - withdraw(amount): raises ValueError if insufficient funds
#   - balance property (read-only)
#   - __str__ that prints: "Account[Raj]: Rs.1,500.00"
#   - transaction_history list recording every deposit/withdrawal
# Students attempt independently. Type your solution here:




# ============================================================
# FULL REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# class BankAccount:
#
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance
#         self.transaction_history = []
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self._balance += amount
#         self.transaction_history.append(f"+{amount}")
#         return self._balance
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError(
#                 f"Cannot withdraw Rs.{amount}. Balance: Rs.{self._balance}"
#             )
#         self._balance -= amount
#         self.transaction_history.append(f"-{amount}")
#         return self._balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def __str__(self):
#         return f"Account[{self.owner}]: Rs.{self._balance:,.2f}"
#
#     def __repr__(self):
#         return f"BankAccount(owner={self.owner!r}, balance={self._balance})"
#
#
# # Test it
# acc = BankAccount("Raj", 1000)
# print(acc)                      # Account[Raj]: Rs.1,000.00
# acc.deposit(500)
# print(acc.balance)              # 1500
# acc.withdraw(200)
# print(acc)                      # Account[Raj]: Rs.1,300.00
# print(acc.transaction_history)  # ['+500', '-200']
#
# # These should raise:
# # acc.withdraw(5000)
# # acc.deposit(-100)

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Add a transfer(other_account, amount) method to BankAccount
# that withdraws from self and deposits into another
# BankAccount instance. Handle the case where the withdrawal
# fails gracefully.