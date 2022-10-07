import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dt.csv')

df['dt'].plot(kind='hist',bins=100)
#plt.hist(df['dt'],bins=100)
#plt.show()

sns.distplot(df['dt'],bins=100)
plt.show()