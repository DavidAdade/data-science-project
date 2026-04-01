# ============================================
# Golden State Warriors Analysis Project
# Team: [Your Names Here]
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the Golden State Warriors 2025-26 season data ----
url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/golden_state_warriors/golden_state_warriors_stats.csv'
df = pd.read_csv(url)

# ---- Take a look at your data first! ----
print("Golden State Warriors Roster:")
print(df.head())
print()
print("Columns you can use:", list(df.columns))
print()
print("Total players:", len(df))


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# Hint 1: Who are the top scorers on the team?
# top_scorers = df.sort_values('PTS', ascending=False).head(5)
# print(top_scorers[['Player', 'PTS', 'FG%']])

# Hint 2: Steph Curry only played 39 games - how does his production compare?
# print(df.sort_values('GP')[['Player', 'GP', 'PTS', 'MIN']].head(10))

# Hint 3: Create a bar chart of the top 5 scorers
# top5 = df.sort_values('PTS', ascending=False).head(5)
# plt.bar(top5['Player'], top5['PTS'], color='gold')
# plt.title('Warriors Top 5 Scorers (2025-26)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 4: Who is the best 3-point shooter? (min 30 games played)
# regulars = df[df['GP'] >= 30]
# print(regulars.sort_values('3P%', ascending=False)[['Player', '3P%', '3PA', 'GP']])

# Hint 5: Scatter plot - do players who shoot more score more?
# plt.scatter(df['FGA'], df['PTS'])
# plt.xlabel('Field Goal Attempts')
# plt.ylabel('Points Per Game')
# plt.title('Shots vs Points')
# plt.show()

# Hint 6: Filter for starters vs bench players
# starters = df[df['MIN'] >= 20]
# bench = df[df['MIN'] < 20]
# print("Starters avg PTS:", starters['PTS'].mean())
# print("Bench avg PTS:", bench['PTS'].mean())

# Hint 7: Who is the best all-around player? Create a combined stat
# df['Impact'] = df['PTS'] + df['REB'] + df['AST'] + df['STL'] + df['BLK']
# print(df.sort_values('Impact', ascending=False)[['Player', 'Impact', 'PTS', 'REB', 'AST']].head(5))


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
