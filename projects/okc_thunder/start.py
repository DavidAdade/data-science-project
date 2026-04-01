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

# Hint 1: Who are the top scorers this season?
# top_scorers = df.sort_values('PTS', ascending=False).head(5)
# print(top_scorers[['Player', 'PTS', 'FG%']])

# Hint 2: Compare SGA's stats across seasons!
# sga_old = df_old[df_old['Player'] == 'Shai Gilgeous-Alexander']
# sga_new = df[df['Player'] == 'Shai Gilgeous-Alexander']
# print("SGA 2023-24:", sga_old[['PTS', 'AST', 'REB']].values)
# print("SGA 2025-26:", sga_new[['PTS', 'AST', 'REB']].values)

# Hint 3: Create a bar chart of the top 5 scorers
# top5 = df.sort_values('PTS', ascending=False).head(5)
# plt.bar(top5['Player'], top5['PTS'], color='dodgerblue')
# plt.title('OKC Top 5 Scorers (2025-26)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 4: Who are the new players this season vs 2023-24?
# old_players = set(df_old['Player'])
# new_players = set(df['Player'])
# added = new_players - old_players
# gone = old_players - new_players
# print("New this year:", added)
# print("No longer on team:", gone)

# Hint 5: Scatter plot - do players who shoot more score more?
# plt.scatter(df['FGA'], df['PTS'])
# plt.xlabel('Field Goal Attempts')
# plt.ylabel('Points Per Game')
# plt.title('Shots vs Points (2025-26)')
# plt.show()

# Hint 6: Combine both seasons for a bigger analysis
# df_old['Season_Label'] = '2023-24'
# df['Season_Label'] = '2025-26'
# both = pd.concat([df_old, df], ignore_index=True)
# print(both[['Season_Label', 'Player', 'PTS']].head(10))

# Hint 7: Filter for starters vs bench (20+ minutes)
# starters = df[df['MIN'] >= 20]
# bench = df[df['MIN'] < 20]


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
