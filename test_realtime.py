from wallstreet import Stock, Call, Put
from forex_python.converter import CurrencyRates
import time
import sys

s = Stock('AAPL')
c = CurrencyRates()

print("AAPL")
while True:
    money = c.convert('USD','JPY',s.price)
    sys.stdout.write('\r' + str(int(money)))
    time.sleep(10)
