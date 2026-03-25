# ============================================
# NBA Data Science - Filtering & Graphing
# Week 3-4 Combined Sample Code
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- STEP 1: Load the data ----
url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/files/nba_stats.csv'
df = pd.read_csv(url)

# Quick look at the data
print("First 5 rows:")
print(df.head())
print()
print("All columns:", list(df.columns))
print()


# ---- STEP 2: Basic Filtering ----

# Filter players who score more than 20 points per game
high_scorers = df[df['PTS'] > 20]
print("Players scoring over 20 PPG:")
print(high_scorers[['Player', 'Team', 'PTS']].head(10))
print()

# Filter by team
raptors = df[df['Team'] == 'TOR']
print("Toronto Raptors players:")
print(raptors[['Player', 'PTS', 'REB', 'AST']])
print()

# Filter with TWO conditions (use & for AND)
stars = df[(df['PTS'] > 20) & (df['MIN'] > 30)]
print("Stars: 20+ PPG and 30+ minutes:")
print(stars[['Player', 'PTS', 'MIN']].head(10))
print()