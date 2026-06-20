# ============================================================
# SESSION 9: NumPy, Pandas & IPL Dataset
# Day 5 Morning | 10:00 AM – 1:00 PM
# Topics: NumPy arrays, Pandas DataFrames, groupby, sort, clean
# ============================================================
# BEFORE CLASS:
#   pip install numpy pandas
#   Distribute IPL_Data.csv to all students (or point to website)
#   Verify column names: run df.columns on your machine tonight
# ============================================================


# ── PART 1: NumPy — quick intro (20 min max) ────────────────
# Type here live:




# ── PART 2: Pandas — load and inspect ───────────────────────
# Type here live:




# ── PART 3: Filtering rows ──────────────────────────────────
# Type here live:




# ── PART 4: GroupBy ─────────────────────────────────────────
# Type here live:




# ── PART 5: New columns + data cleaning ─────────────────────
# Type here live:




# ── PART 6: Total Runs Per Batsman — guided ─────────────────
# Walk students through this before the problem. It's the
# stepping stone — the problem below builds on it.
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Using the IPL dataset, find the top 5 batsmen by total runs
# who have faced at least 200 balls. Display their name, total
# runs, and calculated strike rate.
# Steps:
#   1. Filter valid rows (no nulls, Balls_Faced > 0)
#   2. groupby Batsman — sum Runs and Balls_Faced
#   3. Calculate strike rate: (runs / balls) * 100
#   4. Keep only batsmen with TotalBalls >= 200
#   5. Sort by runs, take top 5
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: NumPy
import numpy as np
#
arr = np.array([1, 2, 3, 4, 5])
print(arr)          # [1 2 3 4 5] — no commas, unlike a list
print(type(arr))    # <class 'numpy.ndarray'>
print(arr.dtype)    # int64 — data type of elements
print(arr.shape)    # (5,) — tuple: 5 elements, 1 dimension
print(arr * 2)           # [2 4 6 8 10]  — vectorized, no loop
print(arr.mean())        # 3.0
print(arr.sum())         # 15
print(arr.max())         # 5
print(arr ** 2)          # [ 1  4  9 16 25]
print(arr + 10)          # [11 12 13 14 15]
print(arr > 3)           # [False False False True True]
print(arr.std())         # standard deviation
print(arr.min())         # 1



#
# # 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)      # (2, 3)
print(matrix[0])         # [1 2 3]
print(matrix[:, 1])      # [2 5] — column 1
print(matrix[1][2])    # 6 — row 1, column 2
print(matrix.flatten()) # [1 2 3 4 5 6] — 1D array
print(matrix.reshape(3, 2)) # [[1 2] [3 4] [5 6]] — 3 rows, 2 columns
print(matrix.T)            # [[1 4] [2 5] [3 6]] — transpose
print(matrix.dot(matrix.T))   # [[14 32] [32 77]] — matrix multiplication
print(matrix.sum())         # 21 — sum of all elements
print(matrix.mean())        # 3.5 — average of all elements
print(matrix.std())         # standard deviation
print(matrix.min())         # 1
print(matrix.max())         # 6












arr = np.array([1, 2, 3, 4, 5])

# Operation applies to EVERY element — no loop needed
print(arr * 2)        # [2 4 6 8 10]
print(arr ** 2)       # [1 4 9 16 25]
print(arr + 10)       # [11 12 13 14 15]
print(arr > 3)        # [False False False True True]

# Statistics
print(arr.mean())     # 3.0
print(arr.sum())      # 15
print(arr.max())      # 5
print(arr.min())      # 1
print(arr.std())      # standard deviation

# Two arrays — element-wise operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)          # [5 7 9]
print(a * b)          # [4 10 18]

np.zeros(5)           # [0. 0. 0. 0. 0.]
np.ones(3)            # [1. 1. 1.]
np.arange(0, 10, 2)   # [0 2 4 6 8] — like range() but returns array
np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.] — evenly spaced
np.eye(3)            # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]] — identity matrix
np.random.rand(3, 3) # random numbers between 0 and 1
np.random.randint(0, 10, (3, 3)) # random integers between 0 and 10
np.random.choice([1, 2, 3, 4, 5], size=(3, 3)) # random choice from array
np.random.shuffle(arr) # shuffle array in place
np.random.permutation(arr) # return a new shuffled array
np.random.seed(42) # set seed for reproducibility
np.random.randn(3, 3) # random numbers from standard normal distribution


print("---------------pandas---------------")

# # PART 2: Pandas — load and inspect
import pandas as pd
#
df = pd.read_csv("../public/data/IPL_Data.csv")
#
print(type(df))
print(df.head())          # first 5 rows
print(df.tail())          # last 5 rows
print(df.shape)           # (rows, cols)
print(df.columns.tolist())  # column names — check these!
print(df.info())          # dtypes + null counts
print(df.describe())      # stats for numeric columns
print(df.isnull().sum())  # null count per column


# Batsman    Runs    Balls_Faced    Team
# 0    Raj        88      65             MI
# 1    Priya      92      70             CSK
# 2    Amit       61      55             RCB


# # PART 3: Filtering
# # Filter rows where runs > 50
high_scorers = df[df["Runs"] > 50]
print(high_scorers[["Batsman", "Runs"]].head())
#
# # Multiple conditions
boundaries = df[(df["Runs"] > 30) & (df["Balls_Faced"] < 20)]
print(boundaries.shape)
#
# # query() alternative — more readable
result = df.query("Runs > 50 and Balls_Faced > 10")
print(result.head())

# # PART 4: GroupBy
# # Total runs per batsman
batsman_runs = (
    df.groupby("Batsman")["Runs"]
    .sum()
    .reset_index()
)
batsman_runs.columns = ["Batsman", "TotalRuns"]
print(batsman_runs.sort_values("TotalRuns", ascending=False).head(10))


batsman_stats = df.groupby("Batsman").agg(
    TotalRuns   = ("Runs", "sum"),
    TotalBalls  = ("Balls_Faced", "sum"),
    Innings     = ("Runs", "count"),
    HighScore   = ("Runs", "max"),
    Average     = ("Runs", "mean")
).reset_index()

print(batsman_stats.head())

# # PART 5: New columns + cleaning
# # Remove nulls
df = df.dropna(subset=["Balls_Faced", "Runs"])
df["Fours"].fillna(0, inplace=True)
df["StrikeRate"].fillna(df["StrikeRate"].mean(), inplace=True)


# df = df[df["Balls_Faced"] > 0]   # avoid division by zero
#
# # Create strike rate column
df["StrikeRate"] = (df["Runs"] / df["Balls_Faced"]) * 100
print(df[["Batsman", "Runs", "Balls_Faced", "StrikeRate"]].head())
#
# # Type conversion
df["Runs"] = df["Runs"].astype(int)

# # PART 6: Total Runs Per Batsman — guided
# # Just the totals, sorted — no filtering or strike rate yet.
# # This is the stepping stone for the problem below.
# totals = (
#     df.groupby("Batsman")["Runs"]
#     .sum()
#     .reset_index()
#     .rename(columns={"Runs": "TotalRuns"})
# )
# print(totals.sort_values("TotalRuns", ascending=False).head(10))

# # PROBLEM SOLUTION — top 5 batsmen, >=200 balls faced, strike rate
# import pandas as pd
#
# df = pd.read_csv("IPL_Data.csv")
# df = df.dropna(subset=["Runs", "Balls_Faced"])
# df = df[df["Balls_Faced"] > 0]
#
# totals = df.groupby("Batsman").agg(
#     TotalRuns=("Runs", "sum"),
#     TotalBalls=("Balls_Faced", "sum")
# ).reset_index()
#
# totals["StrikeRate"] = (totals["TotalRuns"] / totals["TotalBalls"]) * 100
# qualified = totals[totals["TotalBalls"] >= 200]
# result = qualified.sort_values("TotalRuns", ascending=False).head(5)
# print(result[["Batsman", "TotalRuns", "StrikeRate"]].round(2))

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Find which IPL team has the highest average run rate across
# all matches they batted in. Show your working with groupby.

# # TAKE-HOME SOLUTION
# import pandas as pd
#
# df = pd.read_csv("IPL_Data.csv")
# df = df.dropna(subset=["Runs", "Balls_Faced"])
# df = df[df["Balls_Faced"] > 0]
#
# team_stats = df.groupby("Team").agg(
#     TotalRuns=("Runs", "sum"),
#     TotalBalls=("Balls_Faced", "sum")
# ).reset_index()
#
# team_stats["RunRate"] = (team_stats["TotalRuns"] / team_stats["TotalBalls"]) * 6
# result = team_stats.sort_values("RunRate", ascending=False).head(5)
# print(result[["Team", "TotalRuns", "RunRate"]].round(2))
