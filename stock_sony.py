import pandas_datareader.data as web
import datetime
start = datetime.datetime(2017, 8, 4)
end = datetime.datetime(2017, 8, 5)
f = web.DataReader('SNE', 'yahoo', start, end)
print(f)
