from pandas import read_csv
from datetime import datetime
from matplotlib import pyplot
#from pandas.tools.plotting import autocorrelation_plot
from pandas.plotting import autocorrelation_plot
import warnings
warnings.filterwarnings('ignore', message="Blended transforms not yet supported.")

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
autocorrelation_plot(series)
pyplot.show()