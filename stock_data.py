import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline

from pandas_datareader.data import DataReader
from datetime import datetime

end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
toyota = DataReader('TM', 'google', start, end)

toyota.head()
