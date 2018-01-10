import threading
from time import sleep

import numpy as np

from simpleplot.lineplot import MultiLinePlot

'''
This test draws multi line plot and keeps updating a all lines in it separately
'''
data_value_min = 0
data_value_max = 100
rs = (2, 50)


def update_chart(line_chart, data_min, data_max, data_shape):
    print('continuing showing')
    s = 1
    data_length, lines = data_shape
    while True:
        sleep(0.1)
        for l in range(0, lines):
            line_chart.set_xydata_for_index(np.random.uniform(data_min, data_max, size=data_length),
                                            np.random.uniform(data_min, data_max, size=data_length), l)
        if s > data_max:
            data_max += 1
            data_min += 1
            line_chart.set_xylimit(data_min, data_max, data_min, data_max)
        s += 1


chart = MultiLinePlot(np.reshape(np.arange(data_value_min, data_value_max), rs),
                      np.reshape(np.arange(data_value_min, data_value_max), rs), blit=False)

compute_thread = threading.Thread(target=update_chart, args=(chart, data_value_min, data_value_max, rs))
compute_thread.start()

chart.run_anim()
compute_thread.join()
