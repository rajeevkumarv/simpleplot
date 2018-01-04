import threading
from time import sleep

import numpy as np

from simpleplot.lineplot import MultiLinePlot

'''
This test draws multi line plot and keeps updating a few lines in it
'''

a = MultiLinePlot(np.reshape(np.arange(0, 100), (20, 5)), np.reshape(np.arange(0, 100), (20, 5)), blit=False)
t = threading.Thread(target=a.runAnim)
t.start()
print 'hello'
s = 1
while (True):
    sleep(0.1)
    a.set_xydata_for_index(np.random.uniform(0, 100, size=20), np.random.uniform(0, 100, size=20), 0)
    a.set_xydata_for_index(np.random.uniform(0, 100, size=20), np.random.uniform(0, 100, size=20), 1)
    if (s > 20):
        a.set_xylimit(s - 20, s, s - 20, s)
    s += 1
