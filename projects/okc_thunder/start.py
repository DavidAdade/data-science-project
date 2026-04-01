# ============================================
# OKC Thunder Analysis Project
# Team: Josiah, Janaiya, Anu
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the OKC Thunder data (3 seasons!) ----
# 2023-24 season
url_2024 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/okc_thunder/okc_thunder_stats.csv'
df_2024 = pd.read_csv(url_2024)

# 2024-25 season
url_2025 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/okc_thunder/okc_thunder_stats_2024_25.csv'
df_2025 = pd.read_csv(url_2025)

# 2025-26 season (current season, still in progress)
url_2026 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/okc_thunder/okc_thunder_stats_2025_26.csv'
df_2026 = pd.read_csv(url_2026)

# Use the most recent completed season by default
df = df_2025

# ---- Take a look at your data first! ----
print("OKC Thunder 2024-25 Roster:")
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
# top_scorers = df.sort_values('PTS', ascending=False).head(5)
# print(top_scorers[['Player', 'PTS', 'FG%']])

# Hint 2: Track SGA's growth across all 3 seasons!
# sga_24 = df_2024[df_2024['Player'] == 'Shai Gilgeous-Alexander']
# sga_25 = df_2025[df_2025['Player'] == 'Shai Gilgeous-Alexander']
# sga_26 = df_2026[df_2026['Player'] == 'Shai Gilgeous-Alexander']
# print("SGA 2023-24:", sga_24[['PTS', 'AST', 'REB', 'FG%']].values)
# print("SGA 2024-25:", sga_25[['PTS', 'AST', 'REB', 'FG%']].values)
# print("SGA 2025-26:", sga_26[['PTS', 'AST', 'REB', 'FG%']].values)

# Hint 3: Create a bar chart of the top 5 scorers
# top5 = df.sort_values('PTS', ascending=False).head(5)
# plt.bar(top5['Player'], top5['PTS'], color='dodgerblue')
# plt.title('OKC Top 5 Scorers (2024-25)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 4: How has the roster changed over 3 years?
# players_24 = set(df_2024['Player'])
# players_25 = set(df_2025['Player'])
# players_26 = set(df_2026['Player'])
# print("On all 3 rosters:", players_24 & players_25 & players_26)
# print("Added in 2025-26:", players_26 - players_25)
# print("Left after 2024-25:", players_25 - players_26)

# Hint 5: Scatter plot - do players who shoot more score more?
# plt.scatter(df['FGA'], df['PTS'])
# plt.xlabel('Field Goal Attempts')
# plt.ylabel('Points Per Game')
# plt.title('Shots vs Points (2024-25)')
# plt.show()

# Hint 6: Combine all 3 seasons for a bigger analysis
# all_seasons = pd.concat([df_2024, df_2025, df_2026], ignore_index=True)
# print("Total player-seasons:", len(all_seasons))
# print(all_seasons[['Season', 'Player', 'PTS']].head(10))

# Hint 7: Compare team averages across seasons
# print("2023-24 team avg PTS:", df_2024['PTS'].mean())
# print("2024-25 team avg PTS:", df_2025['PTS'].mean())
# print("2025-26 team avg PTS:", df_2026['PTS'].mean())

# Hint 8: Filter for starters vs bench (20+ minutes)
# starters = df[df['MIN'] >= 20]
# bench = df[df['MIN'] < 20]


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
