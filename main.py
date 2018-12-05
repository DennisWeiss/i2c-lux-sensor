from tsl2561 import TSL2561
import matplotlib.pyplot as plt
import time


tsl = TSL2561(debug=True)
n = 10
time_interval = 1


def do_measurements(n, time_interval):
    data = []
    plt.ylabel('Lux')
    plt.xlabel('time in s')
    for i in range(n):
        data.append(tsl.lux())
        plt.plot(data)
        plt.show()
        time.sleep(1)
        

do_measurements(n, time_interval)
        
    




