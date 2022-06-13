import time
import os
def clock():
  while True:
    import time

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    time.sleep(1)
    os.system("clear")
clock()