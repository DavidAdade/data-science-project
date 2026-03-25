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


# ---- STEP 3: Create a Calculated Column ----

# Points Per Minute - who is the most efficient?
df['PPM'] = df['PTS'] / df['MIN']

print("Top 10 by Points Per Minute:")
top_ppm = df.sort_values('PPM', ascending=False).head(10)
print(top_ppm[['Player', 'PTS', 'MIN', 'PPM']])
print()


# ---- STEP 4: Bar Chart - Top 10 Scorers ----

top_scorers = df.sort_values('PTS', ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_scorers['Player'], top_scorers['PTS'], color='dodgerblue')
plt.xlabel('Player')
plt.ylabel('Points Per Game')
plt.title('Top 10 NBA Scorers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ---- STEP 5: Filter THEN Graph ----

# Only look at players with 25+ minutes, then graph top rebounders
starters = df[df['MIN'] >= 25]
top_rebounders = starters.sort_values('REB', ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_rebounders['Player'], top_rebounders['REB'], color='green')
plt.xlabel('Player')
plt.ylabel('Rebounds Per Game')
plt.title('Top 10 Rebounders (Starters Only - 25+ MIN)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ---- STEP 6: Scatter Plot - Points vs Assists ----

plt.figure(figsize=(8, 5))
plt.scatter(df['PTS'], df['AST'], alpha=0.5, color='purple')
plt.xlabel('Points Per Game')
plt.ylabel('Assists Per Game')
plt.title('Do High Scorers Also Get Assists?')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ---- STEP 7: Compare Teams with a Horizontal Bar Chart ----

team_avg_pts = df.groupby('Team')['PTS'].mean().sort_values(ascending=True).tail(10)

plt.figure(figsize=(8, 5))
plt.barh(team_avg_pts.index, team_avg_pts.values, color='orange')
plt.xlabel('Average Points Per Game')
plt.ylabel('Team')
plt.title('Top 10 Highest Scoring Teams (Average)')
plt.tight_layout()
plt.show()
