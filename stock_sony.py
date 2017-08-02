import pandas_datareader.data as web
import datetime
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 7, 31)
f = web.DataReader('SNE', 'yahoo', start, end)
print(f)
