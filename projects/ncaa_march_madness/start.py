# ============================================
# NCAA March Madness Analysis Project
# Team: Lex, Adrian, Kaden
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load March Madness data (pick one or use all three!) ----
# 2023-24 season (original - UConn won back-to-back)
url_2024 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ncaa_march_madness/ncaa_march_madness_stats.csv'
df_2024 = pd.read_csv(url_2024)

# 2024-25 season (Florida won the championship!)
url_2025 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ncaa_march_madness/ncaa_march_madness_stats_2024_25.csv'
df_2025 = pd.read_csv(url_2025)

# 2025-26 season (current tournament - Final Four: UConn, Illinois, Arizona, Michigan)
url_2026 = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ncaa_march_madness/ncaa_march_madness_stats_2025_26.csv'
df_2026 = pd.read_csv(url_2026)

# Use the most recent completed season by default
df = df_2025

# ---- Take a look at your data first! ----
print("2024-25 NCAA Tournament Teams:")
print(df.head())
print()
print("Columns you can use:", list(df.columns))
print()
print("Total teams (2024-25):", len(df_2025))
print("Total teams (2025-26):", len(df_2026))


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# Hint 1: Who won each tournament?
# print("2024 Champion:", df_2024.sort_values('Tournament_Wins', ascending=False).head(1)[['Team', 'Tournament_Wins']])
# print("2025 Champion:", df_2025.sort_values('Tournament_Wins', ascending=False).head(1)[['Team', 'Tournament_Wins']])
# print("2026 (in progress):", df_2026.sort_values('Tournament_Wins', ascending=False).head(4)[['Team', 'Tournament_Wins']])

# Hint 2: Do higher seeds actually win more games?
# plt.scatter(df['Seed'], df['Tournament_Wins'])
# plt.xlabel('Seed (1 = best)')
# plt.ylabel('Tournament Wins')
# plt.title('Does Seed Predict Tournament Success?')
# plt.show()

# Hint 3: Compare across years - combine all three datasets!
# all_years = pd.concat([df_2024, df_2025, df_2026], ignore_index=True)
# print("Total teams across 3 tournaments:", len(all_years))
# avg_by_seed = all_years.groupby('Seed')['Tournament_Wins'].mean()
# plt.bar(avg_by_seed.index, avg_by_seed.values, color='orange')
# plt.title('Average Tournament Wins by Seed (3 Years)')
# plt.xlabel('Seed')
# plt.ylabel('Avg Wins')
# plt.show()

# Hint 4: Filter by conference
# sec_teams = df[df['Conference'] == 'SEC']
# big12_teams = df[df['Conference'] == 'Big 12']
# print("SEC teams:", sec_teams[['Team', 'Seed', 'Tournament_Wins']])

# Hint 5: What makes tournament winners different?
# winners = df[df['Tournament_Wins'] >= 2]
# losers = df[df['Tournament_Wins'] == 0]
# print("Winners avg PPG:", winners['PPG'].mean())
# print("First round exits avg PPG:", losers['PPG'].mean())

# Hint 6: Bar chart comparing conferences
# conf_wins = df.groupby('Conference')['Tournament_Wins'].sum().sort_values(ascending=False).head(10)
# plt.bar(conf_wins.index, conf_wins.values, color='orange')
# plt.title('Which Conference Won the Most Tournament Games?')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# Hint 7: Defense vs Offense - what matters more?
# df['Point_Diff'] = df['PPG'] - df['OPP_PPG']
# plt.scatter(df['Point_Diff'], df['Tournament_Wins'])
# plt.xlabel('Average Point Differential')
# plt.ylabel('Tournament Wins')
# plt.title('Does Point Differential Predict March Madness Success?')
# plt.show()

# Hint 8: Track teams across years - did they improve?
# florida_24 = df_2024[df_2024['Team'] == 'Florida']
# florida_25 = df_2025[df_2025['Team'] == 'Florida']
# print("Florida 2024:", florida_24[['Seed', 'PPG', 'Tournament_Wins']].values)
# print("Florida 2025:", florida_25[['Seed', 'PPG', 'Tournament_Wins']].values)


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
