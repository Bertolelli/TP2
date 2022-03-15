# Dans combien d'entrée le mot "Irlande" est présent ? 

import pandas as pd
df = pd.read_csv('nodes-addresses.csv', usecols=['countries']);
df=df[df['countries']=='Ireland']
print(len(df)) #comptage du nombre de ligne