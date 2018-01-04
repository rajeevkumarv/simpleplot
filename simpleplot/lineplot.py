'''
Created on 03-Jan-2018

@author: rajeevv
'''
import threading
from threading import Lock

import matplotlib.animation as animation
import matplotlib.pylab as plt
import numpy as np


class MultiLinePlot:

    def __init__(self, xdata, ydata, blit=True):
        self.blit = blit
        self.fig, self.ax = plt.subplots()
        self.line = []
        self.lock = Lock()
        self.x = xdata
        self.y = ydata
        self.line = self.ax.plot(self.x, self.y)
        print len(self.x), len(self.line)
        self.init()

    def set_xylimit(self, xmin, xmax, ymin, ymax):
        self.lock.acquire()
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(ymin, ymax)
        self.lock.release()

    def set_xlimit(self, xmin, xmax):
        self.lock.acquire()
        self.ax.set_xlim(xmin, xmax)
        self.lock.release()

    def set_ylimit(self, ymin, ymax):
        self.lock.acquire()
        self.ax.set_ylim(ymin, ymax)
        self.lock.release()

    def set_ydata(self, ydata):
        self.lock.acquire()
        self.y = ydata
        self.lock.release()

    def set_xdata(self, xdata):
        self.lock.acquire()
        self.x = xdata
        self.lock.release()

    def set_ydata_for_index(self, ydata, index):
        self.lock.acquire()
        self.y[:, index] = ydata
        self.lock.release()

    def set_xdata_for_index(self, xdata, index):
        self.lock.acquire()
        self.x[:, index] = xdata
        self.lock.release()

    def set_xydata(self, xdata, ydata):
        assert len(xdata) == len(ydata)
        self.lock.acquire()
        self.x = xdata
        self.y = ydata
        self.lock.release()

    def set_xydata_for_index(self, xdata, ydata, index):
        assert len(xdata) == len(ydata)
        self.lock.acquire()
        self.x[:, index] = xdata
        self.y[:, index] = ydata
        self.lock.release()

    def animate(self, x):
        self.lock.acquire()
        for i in range(0, len(self.line)):
            self.line[i].set_xdata(self.x[:, i])
            self.line[i].set_ydata(self.y[:, i])
        self.lock.release()
        return self.line

    # Init only required for blitting to give a clean slate.
    def init(self):
        for i in range(0, len(self.line)):
            print i, len(self.line)
            # self.line[i].set_ydata(self.y[0,:])
        return self.line,

    def run_anim(self):
        ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200),
                                      interval=25, blit=self.blit)
        self.plotthread = threading.Thread(target=plt.show)
        self.plotthread.start()
        self.plotthread.join()
        print 'start plotting thread'

    @staticmethod
    def show_plot(self):
        plt.show()


class LinePlot:

    def __init__(self, xdata, ydata, blit=True):
        self.blit = blit
        self.fig, self.ax = plt.subplots()
        self.x = xdata
        self.y = ydata
        self.line, = self.ax.plot(self.x, self.y)
        self.init()
        self.lock = Lock()

    def set_xylimit(self, xMin, xMax, yMin, yMax):
        self.lock.acquire()
        self.ax.set_xlim(xMin, xMax)
        self.ax.set_ylim(yMin, yMax)
        self.lock.release()

    def set_xlimit(self, xMin, xMax):
        self.lock.acquire()
        self.ax.set_xlim(xMin, xMax)
        self.lock.release()

    def set_ylimit(self, yMin, yMax):
        self.lock.acquire()
        self.ax.set_ylim(yMin, yMax)
        self.lock.release()

    def set_ydata(self, ydata):
        self.lock.acquire()
        self.y = ydata
        self.lock.release()

    def set_xdata(self, xdata):
        self.lock.acquire()
        self.x = xdata
        self.lock.release()

    def set_xydata(self, xdata, ydata):
        assert len(xdata) == len(ydata)
        self.lock.acquire()
        self.x = xdata
        self.y = ydata
        self.lock.release()

    def animate(self, i):
        self.lock.acquire()
        self.line.set_ydata(self.y)  # update the data
        self.line.set_xdata(self.x)  # update the data
        self.lock.release()
        return self.line,

    # Init only required for blitting to give a clean slate.
    def init(self):
        self.line.set_ydata(np.ma.array(self.x, mask=True))
        return self.line,

    def run_anim(self):
        ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200),
                                      interval=25, blit=self.blit)
        self.plotthread = threading.Thread(target=plt.show)
        self.plotthread.start()
        self.plotthread.join()
        print 'start plotting thread'

    @staticmethod
    def show_plot(self):
        plt.show()
