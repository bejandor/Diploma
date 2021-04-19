# !-*-coding:utf-8-*-
# Основной класс MainWindow
import sys

import pandas as pd
from QTableModel import pandasModel  # Импортируем для отображения dataframe
from Final_tample6 import Ui_MainWindow  # Наш шаблон
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from graphics import MyMpvCanvas, NavigationToolbar

tableView_1 = """

QTableView
{
    alternate-background-color: #1F1F1F;
    background-color: gray;
    gridline-color: gray;
    color: gray;
    border-color:white;
    
}
QTableView::item 
{   
    color: white;        
}

QTableView::item:focus
{   
    color: gray;
    background: #0063cd;            
}        
QTableView::item:selected
{   
    color:black;
    background: white;            
}


"""

tableView_2="""QTableView
{
    alternate-background-color: #1F1F1F;
    background-color: blue;
    gridline-color: white;
    color: gray;
    border-color:white;
    
}
QTableView::item 
{   
    color: white;        
}

QTableView::item:focus
{   
    color: gray;
    background: #0063cd;            
}        
QTableView::item:selected
{   
    color: black;
    background: white;            
}


"""


# Вункция для изменения вида кнопки принимает 2 параметра
def button_appearence(ToolButton=None, icon=None):
    ToolButton.setAutoExclusive(True)
    ToolButton.setCheckable(True)
    ToolButton.setIcon(QtGui.QIcon(icon))
    ToolButton.setIconSize(QtCore.QSize(60, 50))
    ToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

    """Стили для кнопок"""
    style_for_toolbuttons = """
    QToolButton{background-color:transparent;
                border:none}
    QToolButton::hover{background-color: rgb(224,232,246)}
    QToolButton::checked{background-color: rgb(139,210,238);border:1px}            
    """
    ToolButton.setStyleSheet(style_for_toolbuttons)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):  # ---шаблон

        QMainWindow.__init__(self)  # Констукторы от родительких классов    -- - шаблон
        self.setupUi(self)  # Передаем родительскому конструктору настройки    -- -- шаблон
        self.tableView_1.setStyleSheet(tableView_1)
        self.tableView_2.setStyleSheet(tableView_2)


        """Инициализируем пустые датафреймы для дальнейшей работы"""
        self.new_df1 = pd.DataFrame()
        self.new_df2 = pd.DataFrame()

        self.new_df_for_saving = pd.DataFrame()

        """ кнопки выбора каталогов
        Привязка кнопок берем с макета подключить(self.наш метод)"""
        self.pushButton_cat1.clicked.connect(self.insert_dataframe1)
        self.pushButton_cat2.clicked.connect(self.insert_dataframe2)

        # Кнопка Импорт --> в сравнение
        self.pushButton.clicked.connect(self.go_to_comparing_page_clicked)

        """Привязка кнопок для переключения между страницами stacke_dwidget
        а так же применение функции для изменения вида кнопок"""
        self.import_data_button.clicked.connect(self.import_data_button_clicked)
        button_appearence(ToolButton=self.import_data_button, icon="Icons/xlsx.png")

        self.comparing_button.clicked.connect(self.comparing_button_clicked)
        button_appearence(ToolButton=self.comparing_button, icon="Icons/green arrows.png")

        self.result_button.clicked.connect(self.result_button_clicked)
        button_appearence(ToolButton=self.result_button, icon="Icons/woodworking-icon-64.png")

        self.graphics_button.clicked.connect(self.graphics_button_clicked)
        button_appearence(ToolButton=self.graphics_button, icon="Icons/graphics.png")

        """Привязка кнопки сравнить в comparing_cats"""
        self.compare_cats.clicked.connect(self.compare_dataframe)

        """Привязка кнопки(тригера) в меню бар """
        self.action_save_as.triggered.connect(self.saveResult_to_excel)

        """Привязка кнопок в результат сравнения -->  график"""
        self.PushButton_build_graphics.clicked.connect(lambda: self.building_graphics())

        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Подключаем двойное нажатие на колонку в TableView для того чтобы поменять название
        # При двойном нажатии будет обработчик self.renameColumn
        self.tableView_1.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_tableview_1)
        self.tableView_2.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_tableview_2)
        self.result_tableView.horizontalHeader().sectionDoubleClicked.connect(self.renameColumn_result_tableView)

        headers = self.tableView_1.horizontalHeader()
        self.tableView_1.horizontalHeader().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        headers.customContextMenuRequested.connect(self.contextMenuEvent)

    """Оброботка кнопки выбора каталога 1"""

    def insert_dataframe1(self):
        """Метод который отображает данные в tableView"""
        """Открывается filedialog и берет путь"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ", "excel")[0]
        if len(file_path) > 0:

            if 'xlsx' in file_path:
                self.new_df1 = pd.read_excel(file_path)  # Читаем файл №1 по пути который получили
                # self.new_df1 = df1  # Записываем в mew_df1 для дальнейшей работы с ним
                # конвертируем названия столбцов в нижний регистр
                self.new_df1.columns = map(str.lower, self.new_df1.columns)

                """Создаем объект для первой таблицы из pandasModel"""
                self.dataframe1model = pandasModel(self.new_df1)
                self.plainTextEdit_cat1.setPlainText(file_path)  # путь в текстовое поле 1
                self.tableView_cat1.setModel(self.dataframe1model)  # В tableView_cat1  import
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
                # конвертируем названия столбцов в нижний регистр
                self.new_df2.columns = map(str.lower, self.new_df2.columns)

                """Создаем модель для представления  с помощью класса pandasModel"""
                self.dataframe2model = pandasModel(self.new_df2)
                self.plainTextEdit_cat2.setPlainText(file_path)  # путь в текстовое поле 2

                self.tableView_cat2.setModel(self.dataframe2model)  # В tableView_cat2 import
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
            if self.checkBox_year.isChecked() == True:

                """Если данные выбраны пытаемся их сравнить"""
                try:
                    """Произовдим слияние таблиц по столбцам"""
                    """Сливаются только те значения кторые есть в обоих таблицах"""
                    self.new_df_for_saving = pd.merge(self.new_df1, self.new_df2,
                                                      on=["year", "month", "day", "hour", "min"],
                                                      how="inner")
                    self.new_df_for_saving['mpv_difference'] = self.new_df_for_saving['mpv_x'] - self.new_df_for_saving[
                        'mpv_y']

                    self.new_df_for_saving['depth_difference'] = self.new_df_for_saving['depth_x'] - self.new_df_for_saving[
                        'depth_y']

                    # self.new_df_for_saving = result_df  # Результат сохраняем в атрибут new_df_for_saving

                    """Создаем объект из второй таблицы  с помощью класса pandasModel
                    для того чтобы их вывести на result_tableView"""
                    self.dataframe_resultmodel = pandasModel(self.new_df_for_saving)
                    # self.result_tableView = QTableView()  # Представление для показа результата
                    self.result_tableView.setWindowTitle("Результат сравнения")
                    self.result_tableView.setModel(self.dataframe_resultmodel)  # Кладем даные в Qtableview
                    self.result_tableView.show()
                    msgBox_compare_success = QtWidgets.QMessageBox()
                    msgBox_compare_success.setWindowTitle("Уведомление")
                    msgBox_compare_success.setText("Сравнение успешно!")
                    msgBox_compare_success.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msgBox_compare_success.exec_()

                    # Если успешно переход QStackedWidget   на resultWidget
                    self.stackedWidget.setCurrentIndex(2)

                    # Изменения фона кнопок для переключения между страницами
                    self.comparing_button.setAutoExclusive(False)
                    self.comparing_button.setChecked(False)

                    self.result_button.setAutoExclusive(True)
                    self.result_button.setChecked(True)


                except KeyError:  # Если значения столбцов не совпадают
                    self.msgBox_compare_error = QtWidgets.QMessageBox()
                    self.msgBox_compare_error.setWindowTitle("Ошибка сравнения")
                    self.msgBox_compare_error.setText("Название столбцов в 2-х каталогах должны быть одинаковы!")
                    self.msgBox_compare_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.msgBox_compare_error.exec_()
            else:
                msgBox_notChecked_error = QtWidgets.QMessageBox()
                msgBox_notChecked_error.setWindowTitle("Ошибка не выбраны столбцы")
                msgBox_notChecked_error.setText("Выберите по каким столбцам сравнивать!!!")
                msgBox_notChecked_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox_notChecked_error.exec_()



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

    def import_data_button_clicked(self):
        self.import_data_button.setAutoExclusive(True)
        self.import_data_button.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)

    def comparing_button_clicked(self):
        self.comparing_button.setAutoExclusive(True)
        self.comparing_button.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)

    def result_button_clicked(self):
        self.result_button.setAutoExclusive(True)
        self.result_button.setChecked(True)
        self.stackedWidget.setCurrentIndex(2)

    def graphics_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    # Кнопка котора якобы ведет к импорту каталогов в сравнение
    def go_to_comparing_page_clicked(self):
        """При нажатии на кнопку он будет проверять выбраны ли данные """
        if self.new_df1.empty or self.new_df2.empty:  # Проверка на имеющиеяся данные
            self.msgBox_compare_error = QtWidgets.QMessageBox()
            self.msgBox_compare_error.setWindowTitle("Ошибка")
            self.msgBox_compare_error.setText("Вы должны импортировать 2 каталога для сравнения !")
            self.msgBox_compare_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBox_compare_error.exec_()
        else:
            msgBox_import_success = QtWidgets.QMessageBox()
            msgBox_import_success.setWindowTitle("Уведомление")
            msgBox_import_success.setText("Импортирование успешно!")
            msgBox_import_success.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox_import_success.exec_()

            self.stackedWidget.setCurrentIndex(1)
            self.import_data_button.setAutoExclusive(False)
            self.import_data_button.setChecked(False)

            self.comparing_button.setAutoExclusive(True)
            self.comparing_button.setChecked(True)

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

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAction = contextMenu.addAction('New')
        openAction = contextMenu.addAction('Open')
        quitAction = contextMenu.addAction('Quit')

        # action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        #
        # if action == quitAction:
        #     self.close()
        #
        # if action == newAction:
        #     print('New Action was pressed!')

        """Обработчик для построния графика"""

    def building_graphics(self):
        # Проверка на завершения сравнения, и есть ли какие либо данные
        if self.new_df_for_saving.empty:
            msgBox_empty_data_error = QtWidgets.QMessageBox()
            msgBox_empty_data_error.setWindowTitle("Ошибка построения графика")
            msgBox_empty_data_error.setText("нет данных , вы не завершили сравнение!!!")
            msgBox_empty_data_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox_empty_data_error.exec_()

        # Строим график если выбран self.checkBox_mpv_diff
        if self.checkBox_mpv_diff.isChecked() == True:
            self.companovka_for_mpv = QtWidgets.QVBoxLayout(self.tab_mpv_diff)
            self.mycanvas_mpv = MyMpvCanvas(self, width=5, height=4, dpi=100)
            self.companovka_for_mpv.addWidget(self.mycanvas_mpv)
            # создаем объект панель инструментов для работы с графиком
            # В качесве аргумента передаем объект график
            self.canvastoolbar = NavigationToolbar(self.mycanvas_mpv, self)
            # Кладем понель инструментов с графиком в размещение
            self.companovka_for_mpv.addWidget(self.canvastoolbar)
            # кладем  график объект в размещение
            self.mycanvas_mpv.axes.set_title("Разница mpv catalog 1 & catalog2 ")

            # генерация номеров для xaxis
            generated_numbers = list([i for i in range(0, len(self.new_df_for_saving['mpv_difference']))])

            self.mycanvas_mpv.axes.set_xticks(generated_numbers)
            self.new_df_for_saving.plot(ax=self.mycanvas_mpv.axes, kind='line', y='mpv_difference', color='red',
                                        marker='o')

            msgBox_import_success = QtWidgets.QMessageBox()
            msgBox_import_success.setWindowTitle("Уведомление")
            msgBox_import_success.setText("Построение графика успешно!")
            msgBox_import_success.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox_import_success.exec_()

            # Если все успешно то переключаемся на страницу графика
            self.stackedWidget.setCurrentIndex(3)

            # Так же меняем фокус кнопок
            self.result_button.setAutoExclusive(False)
            self.result_button.setChecked(False)

            self.graphics_button.setAutoExclusive(True)
            self.graphics_button.setChecked(True)

        # Строим график если выбран self.checkBox_depth_diff
        if self.checkBox_depth_diff.isChecked() == True:

            self.companovka_for_depth = QtWidgets.QVBoxLayout(self.tab_depth_diff)
            self.mycanvas_depth = MyMpvCanvas(self, width=5, height=4, dpi=100)
            # создаем объект панель инструментов для работы с графиком
            # В качесве аргумента передаем объект график
            self.canvastoolbar = NavigationToolbar(self.mycanvas_depth, self)
            # кладем  график объект в размещение
            self.companovka_for_depth.addWidget(self.mycanvas_depth)

            # Кладем понель инструментов с графиком в размещение
            self.companovka_for_depth.addWidget(self.canvastoolbar)

            self.mycanvas_depth.axes.set_title("Разница depth catalog 1 & catalog2 ")
            # генерация номеров для xaxis
            generated_numbers = list([i for i in range(0, len(self.new_df_for_saving['depth_difference']))])

            self.mycanvas_depth.axes.set_xticks(generated_numbers)
            self.new_df_for_saving.plot(ax=self.mycanvas_depth.axes, kind='line', y='depth_difference', color='blue',
                                        marker='o')
            self.stackedWidget.setCurrentIndex(3)

        else:
            msgBox_notChecked_error = QtWidgets.QMessageBox()
            msgBox_notChecked_error.setWindowTitle("Ошибка построения графика")
            msgBox_notChecked_error.setText("Выберите по каким столбцам строить график!!!")
            msgBox_notChecked_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox_notChecked_error.exec_()

        #

        #
        # if self.radioButton_depth_diff.isChecked():
        #     print('Выбран depth')

        #
        # if self.radioButton_lat_lon_diff.isChecked():
        #     print('вы выбрали lat lon diff')
        """==============================================================================================="""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
