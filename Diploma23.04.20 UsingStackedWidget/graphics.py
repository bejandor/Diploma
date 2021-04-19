# Этот клас предназначен для создания отрисовки графика в Pyqt5
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

class MyMpvCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Вызов суперкласса (инизиализация холста)
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111) # Разметка холста
        super(MyMpvCanvas, self).__init__(fig)


