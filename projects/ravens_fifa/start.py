# ============================================
# Ravens / FIFA France / FIFA Nigeria Project
# Team: David, Sarah
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load ALL THREE datasets ----
# You have 3 CSV files to explore - pick one to start, or compare them all!

# Baltimore Ravens 2023 NFL Season
ravens_url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ravens_fifa/baltimore_ravens_stats.csv'
ravens = pd.read_csv(ravens_url)

# France National Soccer Team (Euro 2024 Squad)
france_url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ravens_fifa/france_stats.csv'
france = pd.read_csv(france_url)

# Nigeria National Soccer Team (AFCON 2024 Squad)
nigeria_url = 'https://raw.githubusercontent.com/DavidAdade/data-science-project/main/projects/ravens_fifa/nigeria_stats.csv'
nigeria = pd.read_csv(nigeria_url)

# ---- Take a look at each dataset ----
print("=== BALTIMORE RAVENS ===")
print(ravens.head())
print("Columns:", list(ravens.columns))
print()

print("=== FRANCE ===")
print(france.head())
print("Columns:", list(france.columns))
print()

print("=== NIGERIA ===")
print(nigeria.head())
print("Columns:", list(nigeria.columns))
print()


# ============================================
# HINTS TO GET STARTED (delete these as you go)
# ============================================

# ---- RAVENS HINTS ----

# Hint 1: Filter offense vs defense
# offense = ravens[(ravens['Position'] == 'QB') | (ravens['Position'] == 'RB') | (ravens['Position'] == 'WR') | (ravens['Position'] == 'TE') | (ravens['Position'] == 'K')]
# defense = ravens[(ravens['Position'] == 'LB') | (ravens['Position'] == 'S') | (ravens['Position'] == 'DT') | (ravens['Position'] == 'CB')]

# Hint 2: Who scored the most touchdowns?
# print(ravens.sort_values('Total_TD', ascending=False)[['Player', 'Position', 'Total_TD']].head(5))

# Hint 3: Bar chart of receiving yards
# receivers = ravens[ravens['Rec_YDS'] > 0].sort_values('Rec_YDS', ascending=False)
# plt.bar(receivers['Player'], receivers['Rec_YDS'], color='purple')
# plt.title('Ravens Receiving Yards')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# ---- FIFA HINTS ----

# Hint 4: Compare France vs Nigeria by position
# france_fwd = france[france['Position'] == 'FWD']
# nigeria_fwd = nigeria[nigeria['Position'] == 'FWD']
# print("France FWD avg goals:", france_fwd['Goals'].mean())
# print("Nigeria FWD avg goals:", nigeria_fwd['Goals'].mean())

# Hint 5: Who has the most international experience?
# print(france.sort_values('Caps', ascending=False)[['Player', 'Caps', 'Goals']].head(5))
# print(nigeria.sort_values('Caps', ascending=False)[['Player', 'Caps', 'Goals']].head(5))

# Hint 6: Scatter plot - do more caps = more goals?
# plt.scatter(france['Caps'], france['Goals'], color='blue', label='France')
# plt.scatter(nigeria['Caps'], nigeria['Goals'], color='green', label='Nigeria')
# plt.xlabel('Caps (Games Played)')
# plt.ylabel('Goals')
# plt.title('Experience vs Goals: France vs Nigeria')
# plt.legend()
# plt.show()

# Hint 7: Goals per cap (efficiency!)
# france['Goals_Per_Cap'] = france['Goals'] / france['Caps']
# nigeria['Goals_Per_Cap'] = nigeria['Goals'] / nigeria['Caps']


# ============================================
# YOUR ANALYSIS GOES BELOW - have fun!
# ============================================
