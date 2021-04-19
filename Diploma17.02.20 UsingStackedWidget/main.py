# !-*-coding:utf-8-*-
import sys

import pandas as pd
from QTableModel import pandasModel  # Импортируем для отображения dataframe
from Final_tample3 import Ui_MainWindow  # Наш шаблон
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from PyQt5 import QtCore
# from Mpv_dataframe_graphic import drow_graphic
from graphics import MyMpvCanvas, NavigationToolbar
import matplotlib


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):  # ---шаблон

        QMainWindow.__init__(self)  # Констукторы от родительких классов    -- - шаблон
        self.setupUi(self)  # Передаем родительскому конструктору настройки    -- -- шаблон

        """======================Пример внедрения графика в интерфейс==================================================================="""
        # Для отрисовки графика
        # Создаем размещение кладем в него виджет
        self.companovka_for_mpv = QtWidgets.QVBoxLayout(self.graphics_widget)
        # Создаем наш объект графика
        self.mycanvas_object = MyMpvCanvas(self, width=5, height=4, dpi=100)

        # Создаем dataframe
        df2 = pd.read_excel('file2.xlsx')  # Читаем файл №2
        df2.plot(ax=self.mycanvas_object.axes)

        # Передаем аргументы
        # кладем  график объект в размещение
        self.companovka_for_mpv.addWidget(self.mycanvas_object)
        # создаем объект панель инструментов для работы с графиком
        # В качесве аргумента передаем объект график
        self.canvastoolbar = NavigationToolbar(self.mycanvas_object, self)
        # Кладем понель инструментов с графиком в размещение
        self.companovka_for_mpv.addWidget(self.canvastoolbar)
        # Отобразить график
        self.graphics_widget.show()
        """==============================================================================================="""

        """Инициализируем пустые датафреймы для дальнейшей работы"""
        self.new_df1 = pd.DataFrame()
        self.new_df2 = pd.DataFrame()

        self.new_df_for_saving = pd.DataFrame()

        """ кнопки выбора каталогов
        Привязка кнопок берем с макета подключить(self.наш метод)"""
        self.pushButton_cat1.clicked.connect(self.insert_dataframe1)
        self.pushButton_cat2.clicked.connect(self.insert_dataframe2)

        # Кнопка Импорт --> в представление
        self.pushButton.clicked.connect(self.comparing_button_clicked)

        """Привязка кнопок для переключения между страницами stacke_dwidget"""
        self.import_data_button.clicked.connect(self.import_data_button_clicked)
        self.comparing_button.clicked.connect(self.comparing_button_clicked)
        self.result_button.clicked.connect(self.result_button_clicked)
        self.graphics_button.clicked.connect(self.graphics_button_clicked)

        """Привязка кнопки сравнить в comparing_cats"""
        self.compare_cats.clicked.connect(self.compare_dataframe)

        """Привязка кнопки(тригера) в меню бар """
        self.action_save_as.triggered.connect(self.saveResult_to_excel)

        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Подключаем двойное нажатие на колонку в TableView для того чтобы поменять название
        # При двойном нажатии будет обработчик self.renameColumn
        self.tableView_1.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_tableview_1)
        self.tableView_2.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_tableview_2)
        self.result_tableView.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_result_tableView)

    """Оброботка кнопки выбора каталога 1"""

    def insert_dataframe1(self):
        """Метод который отображает данные в tableView"""
        """Открывается filedialog и берет путь"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ", "excel")[0]
        if len(file_path) > 0:

            if 'xlsx' in file_path:
                self.new_df1 = pd.read_excel(file_path)  # Читаем файл №1 по пути который получили
                # self.new_df1 = df1  # Записываем в mew_df1 для дальнейшей работы с ним

                """Создаем объект для первой таблицы из pandasModel"""
                self.dataframe1model = pandasModel(self.new_df1)
                self.plainTextEdit_cat1.setPlainText(file_path)  # путь в текстовое поле 1
                self.tableView_cat1.setModel(self.dataframe1model)  # В view  import
                self.tableView_1.setModel(self.dataframe1model)  # Кладем даные в tableview_1


            else:
                self.msgBox_another_file = QtWidgets.QMessageBox()
                self.msgBox_another_file.setWindowTitle('Ошибка')
                self.msgBox_another_file.setText("Вы выбрали не верный формат файла")
                self.msgBox_another_file.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.msgBox_another_file.exec_()
        else:

            pass  # Заглушка

    """Оброботка кнопки выбора каталога 1"""

    def insert_dataframe2(self):
        """Получаем путь к файлу"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ")[0]

        """Проверка на провильность выбронного пути """
        if len(file_path) > 0:  # Если выбрано что-то

            if 'xlsx' in file_path:  # Проверяем есть ли путь к excel
                self.new_df2 = pd.read_excel(file_path)  # Читаем файл №2 по пути который получили
                # self.new_df2 = df2  # Записываем в new_df2 для дальнейшей работы с ним

                """Создаем модель для представления  с помощью класса pandasModel"""
                self.dataframe2model = pandasModel(self.new_df2)
                self.plainTextEdit_cat2.setPlainText(file_path)  # путь в текстовое поле 2

                self.tableView_cat2.setModel(self.dataframe2model)  # В view import
                self.tableView_2.setModel(self.dataframe2model)  # Кладем даные в tableview



            else:
                self.msgBox_another_file = QtWidgets.QMessageBox()
                self.msgBox_another_file.setWindowTitle('Ошибка')
                self.msgBox_another_file.setText("Вы выбрали не верный формат файла")
                self.msgBox_another_file.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.msgBox_another_file.exec_()

        else:
            pass  # Заглушка если нажата отмена или закрыть окно

        """Метод который будет сравнивать каталоги """

    def compare_dataframe(self):
        """При нажатии на кнопку он будет проверять выбраны ли данные """
        if self.new_df1.empty or self.new_df2.empty:  # Проверка на имеющиеяся данные
            self.msgBox_compare_error = QtWidgets.QMessageBox()
            self.msgBox_compare_error.setWindowTitle("Ошибка")
            self.msgBox_compare_error.setText("Вы должны выбрать 2 каталога для сравнения!")
            self.msgBox_compare_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBox_compare_error.exec_()
        else:

            """Если данные выбраны пытаемся их сравнить"""
            try:
                """Произовдим слияние таблиц по столбцам"""
                """Сливаются только те значения кторые есть в обоих таблицах"""
                self.new_df_for_saving = pd.merge(self.new_df1, self.new_df2,
                                                  on=["year", "month", "day", "hour", "min"],
                                                  how="inner")
                self.new_df_for_saving['mpv_difference'] = self.new_df_for_saving['mpv_x'] - self.new_df_for_saving[
                    'mpv_y']

                # self.new_df_for_saving = result_df  # Результат сохраняем в атрибут new_df_for_saving

                """Создаем объект из второй таблицы  с помощью класса pandasModel
                для того чтобы их вывести на result_tableView"""
                self.dataframe_resultmodel = pandasModel(self.new_df_for_saving)
                # self.result_tableView = QTableView()  # Представление для показа результата
                self.result_tableView.setWindowTitle("Результат сравнения")
                self.result_tableView.setModel(self.dataframe_resultmodel)  # Кладем даные в Qtableview
                self.result_tableView.show()

                self.stackedWidget.setCurrentIndex(2)
                # Если успешно переход QStackedWidget   на resultWidget


            except KeyError:  # Если значения столбцов не совпадают
                self.msgBox_compare_error = QtWidgets.QMessageBox()
                self.msgBox_compare_error.setWindowTitle("Ошибка сравнения")
                self.msgBox_compare_error.setText("Название столбцов в 2-х каталогах должны быть одинаковы!")
                self.msgBox_compare_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.msgBox_compare_error.exec_()

        """Для сохранения результата"""

    def saveResult_to_excel(self):
        "Запускаем файл диалог  который возвращяет путь"
        file_path = QFileDialog.getSaveFileName(self, "Сохранить в excel", "table.xlsx",
                                                "Excel(*.xlsx);;"
                                                "All Files (*)")[0]

        if len(file_path) > 0:  # Если есть путь
            writer = pd.ExcelWriter(file_path, engine='xlsxwriter')  # Объявляем путь для сохранения excel

            # Кладем new_df_for_saving dataframe в лист1
            self.new_df_for_saving.to_excel(writer, 'Sheet1')

            # Диалоговое окно об учаешном сохранении результата
            writer.save()
            self.msgBoxSave = QtWidgets.QMessageBox()
            self.msgBoxSave.setWindowTitle("Сохранение файла")
            self.msgBoxSave.setText("Файл успешно сохранен!")
            self.msgBoxSave.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBoxSave.exec()
        else:
            pass

    """ Обработка кнопок для переключения между страницами stacke_dwidget"""

    # self.import_data_button.clicked.connect(self.import_data_button_clicked)
    # self.comparing_button.clicked.connect(self.comparing_button_clicked)
    # self.result_button.clicked.connect(self.result_button_clicked)
    # self.graphics_button.clicked.connect(self.graphics_button_clicked)

    def import_data_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def comparing_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def result_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def graphics_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    '''Обработчик двойного клика столбцов в представлении tableview_1'''

    def renameColumn_tableview_1(self, index):
        oldTitle = self.dataframe1model.headerData(
            index, QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole)

        newTitle, accepted = QtWidgets.QInputDialog.getText(
            self, 'Изменение названия колонки', oldTitle)

        if accepted and oldTitle != newTitle:
            self.dataframe1model.setHeaderData(
                index, QtCore.Qt.Horizontal, newTitle, QtCore.Qt.DisplayRole)

            # Перезапись названий колонок new_df1
            old_name = self.new_df1.columns[index]  # Получаем старое значение
            self.new_df1 = self.new_df1.copy()
            self.new_df1.rename(columns={old_name: newTitle}, inplace=True)  # Заменяем название столбца

    '''Обработчик двойного клика столбцов в представлении tableview_2'''

    def renameColumn_tableview_2(self, index):
        oldTitle = self.dataframe2model.headerData(
            index, QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole)

        newTitle, accepted = QtWidgets.QInputDialog.getText(
            self, 'Изменение названия колонки', oldTitle)

        if accepted and oldTitle != newTitle:
            self.dataframe2model.setHeaderData(
                index, QtCore.Qt.Horizontal, newTitle, QtCore.Qt.DisplayRole)

            # Перезапись названий колонок new_df2
            old_name = self.new_df2.columns[index]  # Получаем старое значение
            self.new_df2 = self.new_df2.copy()  # копируем dataframe чтобы внести изменение
            self.new_df2.rename(columns={old_name: newTitle}, inplace=True)  # Заменяем название

    '''Обработчик двойного клика столбцов в представлении renameColumn_result_tableView'''

    def renameColumn_result_tableView(self, index):
        oldTitle = self.dataframe_resultmodel.headerData(
            index, QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole)

        newTitle, accepted = QtWidgets.QInputDialog.getText(
            self, 'Изменение названия колонки ', oldTitle)

        if accepted and oldTitle != newTitle:
            self.dataframe_resultmodel.setHeaderData(
                index, QtCore.Qt.Horizontal, newTitle, QtCore.Qt.DisplayRole)

            # Перезапись названий колонок self.new_df_for_saving
            old_name = self.new_df_for_saving.columns[index]  # Получаем старое значение
            self.new_df_for_saving = self.new_df_for_saving.copy()  # копируем dataframe чтобы внести изменение

            self.new_df_for_saving.rename(columns={old_name: newTitle}, inplace=True)  # Заменяем название

        # self.widget = QtWidgets.QWidget()
        # self.widget.setLayout(layout)
        # self.widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
