import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
start = datetime.datetime(2015, 4, 1)
end = datetime.datetime(2017, 7,31)
f = web.DataReader(['SNE', 'AAPL'], 'yahoo', start, end)
f['Adj Close']['SNE'] /= f['Adj Close']['SNE'][0]
f['Adj Close']['AAPL'] /= f['Adj Close']['AAPL'][0]
f['Adj Close'].plot(title='SNE vs AAPL', grid=True)
plt.show()
