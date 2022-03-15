# Combien de pays ont été déclarés dans les offshore leaks ? 
import pandas as pd
df = pd.read_csv('nodes-addresses.csv', usecols=['countries']); #selectionne les pays
df.drop_duplicates(subset ="countries", keep = 'first', inplace=True) #supprime les doublons
print(len(df)) #comptage du nombre de ligne