import pandas as pd
df=pd.read_csv("nodes-addresses.csv")
print(df["countries"].value_counts())