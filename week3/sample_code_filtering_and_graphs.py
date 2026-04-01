# ============================================
# NBA Data Science - Filtering & Graphing
# Week 3-4 Combined Sample Code
# Created by David Adade for Rise in STEM
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


# ---- STEP 4: BAR CHART - Top 10 Scorers ----
# Chart Type: BAR CHART - best for comparing quantities across categories

print("--- CHART: Bar Chart ---")
top_scorers = df.sort_values('PTS', ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_scorers['Player'], top_scorers['PTS'], color='dodgerblue')
plt.xlabel('Player')
plt.ylabel('Points Per Game')
plt.title('Top 10 NBA Scorers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ---- STEP 5: FILTERED BAR CHART - Filter THEN Graph ----
# Chart Type: BAR CHART - but we filter the data first before graphing

print("--- CHART: Filtered Bar Chart ---")
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


# ---- STEP 6: SCATTER PLOT - Points vs Assists ----
# Chart Type: SCATTER PLOT - best for showing relationships between two variables

print("--- CHART: Scatter Plot ---")
plt.figure(figsize=(8, 5))
plt.scatter(df['PTS'], df['AST'], alpha=0.5, color='purple')
plt.xlabel('Points Per Game')
plt.ylabel('Assists Per Game')
plt.title('Do High Scorers Also Get Assists?')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ---- STEP 7: HORIZONTAL BAR CHART - Compare Teams ----
# Chart Type: HORIZONTAL BAR CHART - best when labels are long (like team names)

print("--- CHART: Horizontal Bar Chart ---")
team_avg_pts = df.groupby('Team')['PTS'].mean().sort_values(ascending=True).tail(10)

plt.figure(figsize=(8, 5))
plt.barh(team_avg_pts.index, team_avg_pts.values, color='orange')
plt.xlabel('Average Points Per Game')
plt.ylabel('Team')
plt.title('Top 10 Highest Scoring Teams (Average)')
plt.tight_layout()
plt.show()


# ---- STEP 8: LINE GRAPH - Compare Stats Across Players ----
# Chart Type: LINE GRAPH - best for showing trends or comparing multiple stats at once

print("--- CHART: Line Graph ---")
# Line graphs are great for showing trends or comparing across a group
top5 = df.sort_values('PTS', ascending=False).head(5)

plt.figure(figsize=(10, 5))
plt.plot(top5['Player'], top5['PTS'], marker='o', color='red', label='Points')
plt.plot(top5['Player'], top5['REB'], marker='s', color='blue', label='Rebounds')
plt.plot(top5['Player'], top5['AST'], marker='^', color='green', label='Assists')
plt.xlabel('Player')
plt.ylabel('Per Game')
plt.title('Top 5 Scorers - Points vs Rebounds vs Assists')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ---- STEP 9: SIDE-BY-SIDE BAR CHART - Compare Two Groups ----
# Chart Type: SIDE-BY-SIDE BAR CHART - best for comparing two groups across categories

print("--- CHART: Side-by-Side Bar Chart ---")
# Compare starters vs bench players
starters = df[df['MIN'] >= 25]
bench = df[df['MIN'] < 25]

categories = ['PTS', 'REB', 'AST']
starter_avgs = [starters['PTS'].mean(), starters['REB'].mean(), starters['AST'].mean()]
bench_avgs = [bench['PTS'].mean(), bench['REB'].mean(), bench['AST'].mean()]

x = range(len(categories))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - width/2 for i in x], starter_avgs, width, label='Starters (25+ MIN)', color='dodgerblue')
plt.bar([i + width/2 for i in x], bench_avgs, width, label='Bench (< 25 MIN)', color='lightcoral')
plt.xlabel('Stat')
plt.ylabel('Average Per Game')
plt.title('Starters vs Bench Players')
plt.xticks(x, categories)
plt.legend()
plt.tight_layout()
plt.show()


# ---- STEP 10: BAR CHART WITH VALUE LABELS ----
# Chart Type: BAR CHART (with numbers on top) - best for presentations

print("--- CHART: Bar Chart with Value Labels ---")
# Adding numbers on top of bars makes presentations look clean
top5_scorers = df.sort_values('PTS', ascending=False).head(5)

plt.figure(figsize=(10, 5))
bars = plt.bar(top5_scorers['Player'], top5_scorers['PTS'], color='gold', edgecolor='black')

# Add the value on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3,
             f'{height:.1f}', ha='center', fontsize=12, fontweight='bold')

plt.xlabel('Player')
plt.ylabel('Points Per Game')
plt.title('Top 5 Scorers (with labels)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ---- STEP 11: PIE CHART - Team Scoring Breakdown ----
# Chart Type: PIE CHART - best for showing how parts make up a whole (percentages)

print("--- CHART: Pie Chart ---")
# How is scoring distributed on a team?
lakers = df[df['Team'] == 'LAL'].sort_values('PTS', ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(lakers['PTS'], labels=lakers['Player'], autopct='%1.0f%%', startangle=90)
plt.title('Lakers Scoring Distribution - Who Carries the Load?')
plt.tight_layout()
plt.show()
