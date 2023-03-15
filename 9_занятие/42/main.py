"""
	Узнать какая максимальная households в зоне минимального значения population
"""

import pandas as pd

FILE_NAME = '../california_housing_train.csv'

df = pd.read_csv(FILE_NAME)

print(df.loc[df['population'] >= df['population'].min()*1.1,
      ['households']].max())
