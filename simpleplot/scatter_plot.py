import numpy as np
import matplotlib.pylab as plt
from threading import Thread

class ScatterPlot:

    def __init__(self,xdata,ydata,color='r',marker='o'):
        self.xdata=xdata
        self.ydata=ydata
        self.fig,self.ax = plt.subplots()
        self.ax.scatter(xdata,ydata,c=color,marker=marker)

    def line_plot(self,xdata,ydata,color='b'):
        self.ax.plot(xdata,ydata,c=color)

    def runAsyncShow(self):
        self.t = Thread(target=plt.show)
        self.t.start()

    def wait(self):
        self.t.join()

    def show(self):
        plt.show()