import pandas as pd

df = pd.read_csv('/content/swag_gamer_data.csv')
pd.set_option('display.width', 1000)

print(df.head(3))

print("shape:", df.shape, "\n", df.tail(2),"\n") #shape is an attribute, not a function

print("select multiple columns\n",df[['GamerTag','Swag_Score']].tail(3),"\n")

print("slicing using rows and columns \n",df.iloc[0:5, 0:4])

print("categorical columns valu count:\n", df['Game'].value_counts())

print("Filtering\n", df[df['Swag_Score'] > 9.5])

df['Kills'] = df['Kills'].fillna(df['Kills'].median()) # fill null with median
print(f"Nulls\n {df.isnull().sum()}") # count nulls

df_cleaned = df.dropna() # drop nulls
print(f"Original rows: {len(df)} | Cleaned rows: {len(df_cleaned)}")

df.describe()

len(df)

df_array = df.values # convert a Dataframe into an Array - from np to pd
print(df_array[:2])

df_encoded = pd.get_dummies(df['Game'])
display(df_encoded.head())

df['Criminality'] = df['Kills']/df['Hours_Played']
print(df[df['Criminality']>20])
