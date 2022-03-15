import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nodes-addresses.csv")
sns.countplot(x="countries", data=df, order=df.countries.value_counts().head(20).index)
# sns.histplot(x="countries", data=df)
plt.show()