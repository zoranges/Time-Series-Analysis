from pandas import Series
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

import pandas as pd

# 用 pd.read_csv 替代 Series.from_csv
df = pd.read_csv('daily-minimum-temperatures.csv', header=0)

# 假设 CSV 文件中包含 'Temperature' 列，可以这样创建一个 Series：
series = df['Daily minimum temperatures in Melbourne, Australia, 1981-1990']


autocorrelation_plot(series)
pyplot.show()