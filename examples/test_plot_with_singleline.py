import threading
from time import sleep

import numpy as np

from simpleplot.lineplot import LinePlot

'''
This test draws multi line plot and keeps updating a all lines in it separately
'''
data_value_min = 0
data_value_max = 100
num_of_plots = 20


def update_chart(line_chart, data_min, data_max, data_size):
    print('continuing showing')
    s = 1
    while True:
        sleep(0.1)
        line_chart.set_xydata(np.random.uniform(data_min, data_max, size=data_size),
                              np.random.uniform(data_min, data_max, size=data_size))
        if s > data_max:
            data_max += 1
            data_min += 1
            line_chart.set_xylimit(data_min, data_max, data_min, data_max)
        s += 1


chart = LinePlot(np.random.uniform(data_value_min, data_value_max, size=num_of_plots),
                 np.random.uniform(data_value_min, data_value_max, size=num_of_plots), blit=False)

computation_thread = threading.Thread(target=update_chart, args=(chart, data_value_min, data_value_max, num_of_plots))
computation_thread.start()

chart.run_anim()
computation_thread.join()
