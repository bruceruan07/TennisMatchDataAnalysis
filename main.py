import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('atp_data.csv')


print(df.isnull().sum())
df.dropna(subset=['Wsets', 'Lsets', 'PSW', 'PSL', 'B365W', 'B365L'])