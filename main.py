import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('atp_data.csv')


df.dropna(subset=['Wsets', 'Lsets', 'PSW', 'PSL', 'B365W', 'B365L'], inplace=True)
df['Winner'] = df['Winner'].str.lower().str.strip()
df['Loser'] = df['Loser'].str.lower().str.strip()

df['Date'] = pd.to_datetime(df['Date'])
df['Surface']= df['Surface'].astype('category')


def calculate_win_rates(data):
    # Count wins and losses
    wins = df['Winner'].value_counts()
    losses = df['Loser'].value_counts()

    # Convert Series to DataFrame
    wins_df = wins.to_frame(name='Wins')
    losses_df = losses.to_frame(name='Losses')

    # Merge wins and losses DataFrames
    stats = wins_df.merge(losses_df, left_index=True, right_index=True, how='outer').fillna(0)

    # Calculate win rate
    stats['Win Rate'] = stats['Wins'] / (stats['Wins'] + stats['Losses'])

    return stats


player_stats = calculate_win_rates(df)
print(player_stats)