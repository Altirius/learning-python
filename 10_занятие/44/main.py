import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
print(data.head())

dummyData = pd.DataFrame({'whoAmI': lst})
dummyData.loc[dummyData['whoAmI'] == "robot", 'robot'] = '1'
dummyData.loc[dummyData['whoAmI'] != "robot", 'robot'] = '0'
dummyData.loc[dummyData['whoAmI'] == "human", 'human'] = '1'
dummyData.loc[dummyData['whoAmI'] != "human", 'human'] = '0'

print(dummyData.drop('whoAmI', axis=1).head())
