import pandas as pd

df = pd.read_csv('/content/swag_gamer_data.csv')
pd.set_option('display.width', 1000)

game_stats = df.groupby('Game')[['Kills', 'Hours_Played']].mean() # groupby name and calc means of kills and hrs_played
print(game_stats)

df['Avg_hrs_of_Game'] = df.groupby('Game')['Hours_Played'].transform('mean')# add columns rel hrs of Game for each player
df['Rel_hrs_of_Game'] = df['Hours_Played'] - df['Avg_hrs_of_Game']
df.drop('Avg_hrs_of_Game', axis=1, inplace=True)
print(df.head(3))

publisher_data = pd.DataFrame({         # Print data with merged column Publisher form df- publisher_data
    'Game': ['GTA V', 'COD Mobile', 'Minecraft', 'Apex Legends', 'Valorant', 'Fortnite'],
    'Publisher': ['Rockstar', 'Activision', 'Mojang', 'EA', 'Riot Games', 'Epic Games']
})
df_merged = pd.merge(df, publisher_data, on='Game', how='left')
print("\n",df_merged[['GamerTag','Game','Publisher']].head(3))
