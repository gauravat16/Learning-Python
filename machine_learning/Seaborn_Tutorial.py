# Learning SEABORN

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/Pokemon.csv',index_col=0,encoding='cp1252')
# print(data)

# sns.lmplot(y='Defense', x='Attack', data=data, fit_reg=False, hue='Stage')
# plt.show()

data=data.drop(['Total','Stage','Legendary'], axis=1)
sns.boxplot(data=data)

plt.show()
