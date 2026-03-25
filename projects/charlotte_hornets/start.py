# ============================================
# Charlotte Hornets Analysis Project
# Team: Joy, Victory
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the Charlotte Hornets 2023-24 season data ----
url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/charlotte_hornets/charlotte_hornets_stats.csv'
df = pd.read_csv(url)

# ---- Take a look at your data first! ----
print("Charlotte Hornets Roster:")
print(df.head())
print()
print("Columns you can use:", list(df.columns))
print()
print("Total players:", len(df))


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# Hint 1: The Hornets went 21-61 this season. Can the data explain why?
# Look at who played the most games (GP column)
# print(df.sort_values('GP', ascending=False)[['Player', 'GP', 'PTS']].head(10))

# Hint 2: Some key players barely played (injuries/trades)
# injured = df[df['GP'] < 30]
# healthy = df[df['GP'] >= 30]
# print("Missed a lot of games:", injured[['Player', 'GP', 'PTS']])

# Hint 3: Bar chart - compare points per game
# top = df.sort_values('PTS', ascending=False).head(8)
# plt.bar(top['Player'], top['PTS'], color='teal')
# plt.title('Hornets Scoring Leaders')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 4: Who was the most efficient shooter?
# print(df.sort_values('FG%', ascending=False)[['Player', 'FG%', 'PTS', 'GP']].head(10))

# Hint 5: Scatter plot - minutes vs points
# plt.scatter(df['MIN'], df['PTS'])
# plt.xlabel('Minutes Per Game')
# plt.ylabel('Points Per Game')
# plt.title('Do More Minutes = More Points?')
# plt.show()

# Hint 6: Compare assists - who is the best playmaker?
# df['AST_TO_Ratio'] = df['AST'] / df['TOV']


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
