from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import pandas as pd

# 用 pd.read_csv 替代 Series.from_csv
df = pd.read_csv('daily-minimum-temperatures.csv', header=0)

# 假设 CSV 文件中包含 'Temperature' 列，可以这样创建一个 Series：
series = df['Daily minimum temperatures in Melbourne, Australia, 1981-1990']


# split dataset
X = series.values
train, test = X[1:len(X)-7], X[len(X)-7:]
# train autoregression
model = AR(train)
model_fit = model.fit()
# 滞后长度
print('Lag: %s' % model_fit.k_ar)
# 系数
print('Coefficients: %s' % model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
for i in range(len(predictions)):
	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot results
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()