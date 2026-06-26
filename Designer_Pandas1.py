import pandas as pd

df = pd.read_csv('/content/swag_gamer_data.csv')
pd.set_option('display.width', 1000)

print(df.head(3))

print("shape:", df.shape, "\n", df.tail(2),"\n") #shape is an attribute, not a function

print("select multiple columns\n",df[['GamerTag','Swag_Score']].tail(3),"\n")

print("slicing using rows and columns \n",df.iloc[0:5, 0:4])

print("categorical columns valu count:\n", df['Game'].value_counts())

print("Filtering\n", df[df['Swag_Score'] > 9.5])
