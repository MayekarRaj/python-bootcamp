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




# ── PART 6: Top Batsmen — walkthrough (guided) ──────────────
# Walk students through this before the problem.
# Type here live:




# ── PROBLEM OF THE SESSION ──────────────────────────────────
# Using the IPL dataset, find which IPL team has the highest
# average run rate across all their batting innings.
# Steps:
#   1. Filter valid rows (no nulls, Balls_Faced > 0)
#   2. groupby Batting_Team
#   3. Compute total runs and total balls
#   4. Calculate run rate: (runs / balls) * 6
#   5. Sort and display top 5 teams
# Students attempt independently. Type your solution here:




# ============================================================
# REFERENCE SOLUTION — DO NOT SHOW UNTIL AFTER DEBRIEF
# ============================================================

# # PART 1: NumPy
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
# print(arr * 2)           # [2 4 6 8 10]  — vectorized, no loop
# print(arr.mean())        # 3.0
# print(arr.sum())         # 15
# print(arr.max())         # 5
# print(arr ** 2)          # [ 1  4  9 16 25]
#
# # 2D array
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix.shape)      # (2, 3)
# print(matrix[0])         # [1 2 3]
# print(matrix[:, 1])      # [2 5] — column 1

# # PART 2: Pandas — load and inspect
# import pandas as pd
#
# df = pd.read_csv("IPL_Data.csv")
#
# print(df.head())          # first 5 rows
# print(df.shape)           # (rows, cols)
# print(df.columns.tolist())  # column names — check these!
# print(df.info())          # dtypes + null counts
# print(df.describe())      # stats for numeric columns
# print(df.isnull().sum())  # null count per column

# # PART 3: Filtering
# # Filter rows where runs > 50
# high_scorers = df[df["Runs"] > 50]
# print(high_scorers[["Batsman", "Runs"]].head())
#
# # Multiple conditions
# boundaries = df[(df["Runs"] > 30) & (df["Balls_Faced"] < 20)]
# print(boundaries.shape)
#
# # query() alternative — more readable
# result = df.query("Runs > 50 and Balls_Faced > 10")
# print(result.head())

# # PART 4: GroupBy
# # Total runs per batsman
# batsman_runs = (
#     df.groupby("Batsman")["Runs"]
#     .sum()
#     .reset_index()
# )
# batsman_runs.columns = ["Batsman", "TotalRuns"]
# print(batsman_runs.sort_values("TotalRuns", ascending=False).head(10))

# # PART 5: New columns + cleaning
# # Remove nulls
# df = df.dropna(subset=["Balls_Faced", "Runs"])
# df = df[df["Balls_Faced"] > 0]   # avoid division by zero
#
# # Create strike rate column
# df["StrikeRate"] = (df["Runs"] / df["Balls_Faced"]) * 100
# print(df[["Batsman", "Runs", "Balls_Faced", "StrikeRate"]].head())
#
# # Type conversion
# df["Runs"] = df["Runs"].astype(int)

# # PART 6: Top Batsmen walkthrough
# totals = df.groupby("Batsman").agg(
#     TotalRuns=("Runs", "sum"),
#     TotalBalls=("Balls_Faced", "sum")
# ).reset_index()
#
# totals["StrikeRate"] = (totals["TotalRuns"] / totals["TotalBalls"]) * 100
# qualified = totals[totals["TotalBalls"] >= 200]
# result = qualified.sort_values("TotalRuns", ascending=False).head(5)
# print(result[["Batsman", "TotalRuns", "StrikeRate"]].round(2))

# # PROBLEM SOLUTION
# import pandas as pd
#
# df = pd.read_csv("IPL_Data.csv")
# df = df.dropna(subset=["Runs", "Balls_Faced"])
# df = df[df["Balls_Faced"] > 0]
#
# team_stats = df.groupby("Batting_Team").agg(
#     TotalRuns=("Runs", "sum"),
#     TotalBalls=("Balls_Faced", "sum")
# ).reset_index()
#
# team_stats["RunRate"] = (team_stats["TotalRuns"] / team_stats["TotalBalls"]) * 6
# result = team_stats.sort_values("RunRate", ascending=False).head(5)
# print(result[["Batting_Team", "TotalRuns", "RunRate"]].round(2))

# ── TAKE-HOME PROBLEM ────────────────────────────────────────
# Find which player has the highest boundary percentage
# (fours + sixes as % of total runs).
# Show your groupby and calculation steps.
