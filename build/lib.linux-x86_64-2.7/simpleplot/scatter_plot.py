import matplotlib.pylab as plt


class ScatterPlot:

    def __init__(self, xdata, ydata, color='r', marker='o'):
        self.xdata = xdata
        self.ydata = ydata
        self.fig, self.ax = plt.subplots()
        self.ax.scatter(xdata, ydata, c=color, marker=marker)

    def line_plot(self, xdata, ydata, color='b'):
        self.ax.plot(xdata, ydata, c=color)

    @staticmethod
    def show():
        plt.show()
