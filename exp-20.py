import pandas as pd
import numpy as np

df=pd.read_csv('ab-data.csv')

A = df[df['group']=='control']['converted']
B = df[df['group']=='treatment']['converted']
p1, p2 = A.mean(), B.mean()
p = (A.sum()+B.sum())/(len(A)+len(B))
z = (p2-p1)/np.sqrt(p*(1-p)*(1/len(A)+1/len(B)))
print("Statistically significant" if abs(z)>1.96 else "Not statistically significant")
