"""
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""

import pandas as pd

FILE_NAME = '../california_housing_train.csv'
MAX_POPULATION = 500

df = pd.read_csv(FILE_NAME)

print(df.loc[df['population'] <= MAX_POPULATION,
      ['median_house_value']].median())
