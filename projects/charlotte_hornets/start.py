# ============================================
# Charlotte Hornets Analysis Project
# Team: Joy, Victory
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the Charlotte Hornets data (3 seasons!) ----
# 2023-24 season
url_2024 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/charlotte_hornets/charlotte_hornets_stats.csv'
df_2024 = pd.read_csv(url_2024)

# 2024-25 season
url_2025 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/charlotte_hornets/charlotte_hornets_stats_2024_25.csv'
df_2025 = pd.read_csv(url_2025)

# 2025-26 season (current season, still in progress)
url_2026 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/charlotte_hornets/charlotte_hornets_stats_2025_26.csv'
df_2026 = pd.read_csv(url_2026)

# Use the most recent completed season by default
df = df_2025

# ---- Take a look at your data first! ----
print("Charlotte Hornets 2024-25 Roster:")
print(df.head())
print()
print("Columns you can use:", list(df.columns))
print()
print("Total players (2023-24):", len(df_2024))
print("Total players (2024-25):", len(df_2025))
print("Total players (2025-26):", len(df_2026))


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# Hint 1: Who are the top scorers?
# top = df.sort_values('PTS', ascending=False).head(5)
# print(top[['Player', 'PTS', 'FG%', 'GP']])

# Hint 2: Injuries have been a big problem for the Hornets. Who missed games?
# injured = df[df['GP'] < 30]
# healthy = df[df['GP'] >= 30]
# print("Missed a lot of games:", injured[['Player', 'GP', 'PTS']])

# Hint 3: Track LaMelo Ball's stats across all 3 seasons!
# lm_24 = df_2024[df_2024['Player'] == 'LaMelo Ball']
# lm_25 = df_2025[df_2025['Player'] == 'LaMelo Ball']
# lm_26 = df_2026[df_2026['Player'] == 'LaMelo Ball']
# print("LaMelo 2023-24:", lm_24[['GP', 'PTS', 'AST', 'REB']].values)
# print("LaMelo 2024-25:", lm_25[['GP', 'PTS', 'AST', 'REB']].values)
# print("LaMelo 2025-26:", lm_26[['GP', 'PTS', 'AST', 'REB']].values)

# Hint 4: Bar chart - compare scoring leaders
# top = df.sort_values('PTS', ascending=False).head(8)
# plt.bar(top['Player'], top['PTS'], color='teal')
# plt.title('Hornets Scoring Leaders (2024-25)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 5: How has the roster changed over 3 years?
# players_24 = set(df_2024['Player'])
# players_25 = set(df_2025['Player'])
# players_26 = set(df_2026['Player'])
# print("On all 3 rosters:", players_24 & players_25 & players_26)
# print("New in 2025-26:", players_26 - players_25)
# print("Left after 2024-25:", players_25 - players_26)

# Hint 6: Scatter plot - minutes vs points
# plt.scatter(df['MIN'], df['PTS'])
# plt.xlabel('Minutes Per Game')
# plt.ylabel('Points Per Game')
# plt.title('Do More Minutes = More Points?')
# plt.show()

# Hint 7: Combine all 3 seasons for a bigger analysis
# all_seasons = pd.concat([df_2024, df_2025, df_2026], ignore_index=True)
# print("Total player-seasons:", len(all_seasons))

# Hint 8: Compare team averages across seasons
# print("2023-24 team avg PTS:", df_2024['PTS'].mean())
# print("2024-25 team avg PTS:", df_2025['PTS'].mean())
# print("2025-26 team avg PTS:", df_2026['PTS'].mean())

# Hint 9: Who is the best playmaker?
# df['AST_TO_Ratio'] = df['AST'] / df['TOV']
# print(df.sort_values('AST_TO_Ratio', ascending=False)[['Player', 'AST', 'TOV', 'AST_TO_Ratio']].head(5))


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
