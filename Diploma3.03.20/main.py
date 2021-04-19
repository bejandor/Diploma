# !-*-coding:utf-8-*-
import sys

import pandas as pd
from TableView import pandasModel  # Импортируем для отображения dataframe
from Main_temp import Ui_MainWindow  # Наш шаблон
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QFileDialog,QDialog
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *arg, **kwargs):    # ---шаблон


        super().__init__()  # Констукторы от родительких классов    -- - шаблон

        """Инициализируем пустые датафреймы для дальнейшей работы"""
        self.new_df1 = pd.DataFrame()
        self.new_df2 = pd.DataFrame()

        self.new_df_for_saving = pd.DataFrame()


        self.setupUi(self)  # Передаем ему настройки    -- -- шаблон





        """Привязка кнопок берем с макета подключить(self.наш метод)"""
        self.pushButton.clicked.connect(self.insert_dataframe1)
        self.pushButton_2.clicked.connect(self.insert_dataframe2)

        """Привязка кнопки(тригера) в меню бар """
        self.action_compare.triggered.connect(self.compare_dataframe)
        self.action_save_as.triggered.connect(self.saveResult_to_excel)


        # self.pushButton_3.clicked.connect(self.clicked_btn3)
        # self.pushButton_4.clicked.connect(self.clicked_btn4)
        # self.pushButton_5.clicked.connect(self.clicked_btn5)
        # self.pushButton_6.clicked.connect(self.clicked_btn6)


    """Оброботки кнопки выбора каталога 1"""
    def insert_dataframe1(self):
        """Метод который отображает данные в tableView"""
        """Открывается filedialog и берет путь"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ", "excel")[0]
        if len(file_path)>0:

           if 'xlsx' in file_path:
                df1 = pd.read_excel(file_path)  # Читаем файл №1 по пути который получили
                self.new_df1 = df1 # Записываем в mew_df1 для дальнейшей работы с ним
                """Создаем объект для первой таблицы из pandasModel"""
                self.dataframe1 = pandasModel(df1)
                self.tableView_1.setModel(self.dataframe1) # Кладем даные в tableview
           else:
               self.msgBox_another_file = QtWidgets.QMessageBox()
               self.msgBox_another_file.setWindowTitle('Ошибка')
               self.msgBox_another_file.setText("Вы выбрали не верный формат файла")
               self.msgBox_another_file.setStandardButtons(QtWidgets.QMessageBox.Ok)
               self.msgBox_another_file.exec_()
        else:

            pass # Заглушка





    def insert_dataframe2(self):
        """Получаем путь к файлу"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ")[0]


        """Проверка на провильность выбронного пути """
        if len(file_path)>0: # Если выбрано что-то

            if 'xlsx' in file_path: # Проверяем есть ли путь к excel
                df2 = pd.read_excel(file_path)  # Читаем файл №2 по пути который получили
                self.new_df2 = df2 # Записываем в mew_df2 для дальнейшей работы с ним

                """Создаем объект из второй таблицы  с помощью класса pandasModel"""
                self.dataframe2 = pandasModel(df2)
                self.tableView_2.setModel(self.dataframe2) # Кладем даные в tableview

            else:
                self.msgBox_another_file = QtWidgets.QMessageBox()
                self.msgBox_another_file.setWindowTitle('Ошибка')
                self.msgBox_another_file.setText("Вы выбрали не верный формат файла")
                self.msgBox_another_file.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.msgBox_another_file.exec_()

        else:
            pass # Заглушка если нажата отмена или закрыть окно


        """Метод который будет сравнивать каталоги """
    def compare_dataframe(self):
        """При нажатии на кнопку он будет проверять выбраны ли данные """
        if self.new_df1.empty or self.new_df2.empty:
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
                result_df = pd.merge(self.new_df1, self.new_df2, on=["year", "month", "day", "hour", "min"], how="inner")
                result_df['mpv_difference'] = result_df['mpv_x'] - result_df['mpv_y']

                self.new_df_for_saving = result_df # Результат сохраняем в атрибут new_df_for_saving

                """Создаем объект из второй таблицы  с помощью класса pandasModel
                для того чтобы их вывести на tableView"""
                self.dataframe_result = pandasModel(result_df)
                self.result_tableView = QTableView()
                self.result_tableView.setWindowTitle("Результат сравнения")
                self.result_tableView.setModel(self.dataframe_result)  # Кладем даные в Qtableview
                self.result_tableView.show()
            except KeyError:
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

        if len(file_path)>0:# Если есть путь
            writer = pd.ExcelWriter(self.file_path, engine='xlsxwriter') # Объявляем путь для сохранения excel

            # Кладем new_df_for_saving dataframe в лист1
            self.new_df_for_saving.to_excel(writer, 'Sheet1')

            # Сохранение результата
            writer.save()
            self.msgBoxSave = QtWidgets.QMessageBox()
            self.msgBoxSave.setWindowTitle("Сохранение файла")
            self.msgBoxSave.setText("Файл: " + self.saving_file + " успешно сохранен!")
            self.msgBoxSave.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBoxSave.exec()
        else:
            pass



    # Обработчики  не используемых кнопок
    #
    # def clicked_btn3(self):
    #     print("Нажата кнопка 3")
    #
    # def clicked_btn4(self):
    #     print("Нажата кнопка 4")
    #
    # def clicked_btn5(self):
    #     print("Нажата кнопка 5")
    #
    # def clicked_btn6(self):
    #     print("Нажата кнопка 6")





if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
