import numpy as np
from simpleplot.scatter_plot import ScatterPlot

xdata = np.random.uniform(0,100,100)
ydata = np.random.uniform(0,100,100)
scatterPlot = ScatterPlot(xdata,ydata,marker='x')
scatterPlot.runAsyncShow()
scatterPlot.line_plot(np.arange(0,100),np.arange(0,100))
scatterPlot.line_plot(np.sqrt(np.arange(0,100)),np.arange(0,100),'y')
scatterPlot.wait()

