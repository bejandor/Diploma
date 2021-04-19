from PyQt5 import QtCore


# Создаем свой клас для модели, которая будет работать с dataframe объектами
class pandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__data = data

        # Возможность значения столбцов редактируемыми в представлении==================================

    def setHeaderData(self, section, orientation, value, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal:  # Если есть заголовки
            columns_arr = self.__data.columns.values  # Получаем все индексы столбцов
            columns_arr[section] = value  # Перезаписываем значение
            return True  # Успешно
        return QtCore.QAbstractTableModel.setHeaderData(self, section, orientation, value, role)
        # Возвращяем значение в представление True

    # Задаем параметры заголовков строк и столбцов
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__data.columns[section]  # Значение для столбцов
            else:
                return section + 1  # Значение для строк

    # Количество строк
    def rowCount(self, parent):
        return self.__data.shape[0]

    # Количество столбцов
    def columnCount(self, parent):
        return self.__data.shape[1]

    # Системный метод который мы перезаписываем чтобы повлиять на поведение моделей
    def data(self, index, role=QtCore.Qt.DisplayRole):

        # При двойном нажатии на ячейку элемент полностью стирается чтобы предотвратить нужно прменить метод-----------
        if role == QtCore.Qt.EditRole:
            return str(self.__data.iloc[index.row(), index.column()]) # Определяем позицию элемента в массиве
            # Возвращяем значение из массива в отображение

        # Отображение данных в представлении ========================================
        if role == QtCore.Qt.DisplayRole:
            return str(self.__data.iloc[index.row(), index.column()])
            # Определяем позицию элемента в dataframe при помощи метода iloc

    # Определяем состояния ячеек для возможности редактирования ==================

    # Метод flags для определения состояния ячеек ав представлении
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    # Метод setData для изменения значения в ячейке
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:  # если поле редактируемое то
            row = index.row()  # Получаем индекс элемента в строке
            column = index.column()  # Индекс элемента в столбце
            new_element = value  # Новое значение
            if new_element:  # Проверка нового элемента
                self.__data.iloc[row, column] = new_element  # Перезапись значения
                return True  # Успешно
            else:
                return False  # Не успешно
