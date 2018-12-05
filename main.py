from tsl2561 import TSL2561
import matplotlib.pyplot as plt
import time


tsl = TSL2561(debug=True)
n = 100
time_interval = 0.1


def do_measurements(n, time_interval):
    data = []
    plt.ylabel('Lux')
    plt.xlabel('time in s')
    for i in range(n):
        data.append(tsl.lux())
        time.sleep(time_interval)
    plt.plot(data)
    plt.show()
        

do_measurements(n, time_interval)
        
    




