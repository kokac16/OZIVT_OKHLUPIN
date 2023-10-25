import datetime
import time

for _ in range(5):
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(1)
