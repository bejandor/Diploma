# Этот клас предназначен для создания графика в Pyqt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


# class MyMpvCanvas(FigureCanvasQTAgg):  # Класс представляющий собой , холст для рисования
#     def __init__(self, fig, parent=None):
#         # подаем на вход рисунок (экземпляр класса figure)
#         self.fig = fig
#         # Вызов суперкласса (инизиализация холста)
#         FigureCanvasQTAgg.__init__(self, self.fig)
#         # Определяем характер поведения размеров холста как Expanding
#         FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
#         # Сообщяем системе, что политика геометрии для объекта изменилась
#         FigureCanvasQTAgg.updateGeometry(self)

class MyMpvCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MyMpvCanvas, self).__init__(fig)


