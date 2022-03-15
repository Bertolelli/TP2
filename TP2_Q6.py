#20 les plus declares
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("nodes-addresses.csv")
df=(df["countries"].value_counts())
print(df.head(20))
sns.countplot(x="countries", data=df, order=df.countries.value_counts().head(20).index)
plt.show()