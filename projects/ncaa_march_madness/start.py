# ============================================
# NCAA March Madness 2024 Analysis Project
# Team: Lex, Adrian, Kaden
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the 2024 March Madness data (all 64 teams!) ----
url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ncaa_march_madness/ncaa_march_madness_stats.csv'
df = pd.read_csv(url)

# ---- Take a look at your data first! ----
print("2024 NCAA Tournament Teams:")
print(df.head())
print()
print("Columns you can use:", list(df.columns))
print()
print("Total teams:", len(df))


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# Hint 1: Arkansas didn't make the 2024 tournament, but you have all 64 teams!
# See all team names: print(df[['Team', 'Conference', 'Seed']])
# Filter SEC teams (Arkansas's conference): sec = df[df['Conference'] == 'SEC']
# print(sec[['Team', 'Seed', 'Tournament_Wins']])

# Hint 2: Who won the tournament? Look at Tournament_Wins
# print(df.sort_values('Tournament_Wins', ascending=False).head(10))

# Hint 3: Do higher seeds actually win more games?
# plt.scatter(df['Seed'], df['Tournament_Wins'])
# plt.xlabel('Seed (1 = best)')
# plt.ylabel('Tournament Wins')
# plt.title('Does Seed Predict Tournament Success?')
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


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
