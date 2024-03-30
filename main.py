import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('atp_data.csv')


df.dropna(subset=['Wsets', 'Lsets', 'PSW', 'PSL', 'B365W', 'B365L'], inplace=True)
df['Winner'] = df['Winner'].str.lower().str.strip()
df['Loser'] = df['Loser'].str.lower().str.strip()

print(df['Winner'])