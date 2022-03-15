# Dans combien de montage apparrait "EL PORTADOR" ?

import pandas as pd
df = pd.read_csv('nodes-officers.csv', usecols=['name']);
df=df[df['name']=='EL PORTADOR'] 
print(len(df)) #comptage du nombre de ligne