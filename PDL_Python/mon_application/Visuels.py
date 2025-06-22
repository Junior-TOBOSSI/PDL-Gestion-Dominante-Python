from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

class Visuels(FigureCanvas):

    def __init__(self, parent = None):
        fig = Figure(figsize=(16,9))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
