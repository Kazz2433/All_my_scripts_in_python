import datetime
import time

newyear = datetime.datetime(2022, 1, 1, 0, 0, 0)
while datetime.datetime.now() <newyear:
    time.sleep(1)
    print('2')
print('tamo la')