# ============================================
# OKC Thunder Analysis Project
# Team: Josiah, Janaiya, Anu
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the OKC Thunder 2023-24 season data ----
url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/okc_thunder/okc_thunder_stats.csv'
df = pd.read_csv(url)

# ---- Take a look at your data first! ----
print("OKC Thunder Roster:")
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

# Hint 2: Who plays the most minutes?
# print(df.sort_values('MIN', ascending=False)[['Player', 'MIN', 'PTS']].head(5))

# Hint 3: Create a bar chart of the top 5 scorers
# top5 = df.sort_values('PTS', ascending=False).head(5)
# plt.bar(top5['Player'], top5['PTS'], color='dodgerblue')
# plt.title('OKC Top 5 Scorers')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 4: Points per minute - who is the most efficient?
# df['PPM'] = df['PTS'] / df['MIN']

# Hint 5: Scatter plot - do players who shoot more score more?
# plt.scatter(df['FGA'], df['PTS'])
# plt.xlabel('Field Goal Attempts')
# plt.ylabel('Points')
# plt.title('Shots vs Points')
# plt.show()

# Hint 6: Filter for players with 20+ minutes (starters vs bench)
# starters = df[df['MIN'] >= 20]
# bench = df[df['MIN'] < 20]


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
