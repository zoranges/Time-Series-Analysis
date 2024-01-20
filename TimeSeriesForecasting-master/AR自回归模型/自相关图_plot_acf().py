from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
import pandas as pd

# 用 pd.read_csv 替代 Series.from_csv
df = pd.read_csv('daily-minimum-temperatures.csv', header=0)

# 假设 CSV 文件中包含 'Temperature' 列，可以这样创建一个 Series：
series = df['Daily minimum temperatures in Melbourne, Australia, 1981-1990']


plot_acf(series, lags=31)
pyplot.show()