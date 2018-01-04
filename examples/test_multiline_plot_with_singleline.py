import threading
from time import sleep

import numpy as np

from simpleplot.lineplot import MultiLinePlot

'''
This test draws multi line plot and keeps updating a all lines in it separately
'''

dataMin = 0
dataMax = 100
rs = (2, 50)

a = MultiLinePlot(np.reshape(np.arange(dataMin, dataMax), rs), np.reshape(np.arange(dataMin, dataMax), rs), blit=False)
t = threading.Thread(target=a.runAnim)
t.start()
print 'hello'
s = 1
data_length, lines = rs
while (True):
    sleep(0.1)
    for l in range(0, lines):
        a.set_xydata_for_index(np.random.uniform(dataMin, dataMax, size=data_length),
                               np.random.uniform(dataMin, dataMax, size=data_length), l)
    if (s > dataMax):
        dataMax += 1
        dataMin += 1
        a.set_xylimit(dataMin, dataMax, dataMin, dataMax)
    s += 1
