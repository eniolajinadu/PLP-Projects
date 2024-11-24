import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'Name': ['Alice','Bob','Charlie'], 'Age': [23,33,12], 'Town': ['Madripoor', 'Lagos', 'Kentucky']}
df = pd.DataFrame(data)


df_age_filtered= df[df['Age'] < 30]
#print (df_age_filtered)

ra = pd.read_csv('/home/eniolajinadu/GitHub/PLP-Projects/Python/data.csv')

df['Country'] = ['India', 'Nigeria', 'US']
print(df)

df.to_csv ('/home/eniolajinadu/GitHub/PLP-Projects/Python/data.csv', index=False)
#re = pd.read_csv('/home/eniolajinadu/GitHub/PLP-Projects/Python/data.csv')

sum_age = df['Age'].sum()
print(sum_age)

df.loc[len(df.index)] = ['David', 45, 'Kentucky', 'US']
print(df)
df.to_csv ('/home/eniolajinadu/GitHub/PLP-Projects/Python/data.csv', index=False)


grouped = df.groupby('Town').agg({'Age': 'mean', 'Name': 'count'})
print(grouped)

plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.show()

df.plot(kind='scatter', x='Town', y='Age')
plt.title('town v. age')
plt.show()