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
        self.new_df1=pd.DataFrame()
        self.new_df2 = pd.DataFrame()
        self.new_df_for_saving = pd.DataFrame()


        self.setupUi(self)  # Передаем ему настройки    -- -- шаблон





        """Привязка кнопок берем с макета подключить(self.наш метод)"""
        self.pushButton.clicked.connect(self.insert_dataframe1)
        self.pushButton_2.clicked.connect(self.insert_dataframe2)

        """Привязка кнопки(тригера) в меню бар """
        self.action_compare.triggered.connect(self.compare_dataframe)
        self.action_save_as.triggered.connect(self.saveResult_to_excel)

        self.pushButton_3.clicked.connect(self.clicked_btn3)
        self.pushButton_4.clicked.connect(self.clicked_btn4)
        self.pushButton_5.clicked.connect(self.clicked_btn5)
        self.pushButton_6.clicked.connect(self.clicked_btn6)

    """Оброботки кнопок"""
    def insert_dataframe1(self):
        """Метод который отображает данные в tableView"""
        """Открывается filedialog и берет путь"""
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ", "excel")[0]
        df1 = pd.read_excel(file_path)  # Читаем файл №1 по пути который получили

        self.new_df1 = df1 # Записываем в mew_df1 для дальнейшей работы с ним

        """Создаем объект для первой таблицы из pandasModel"""
        self.dataframe1 = pandasModel(df1)
        self.tableView_1.setModel(self.dataframe1) # Кладем даные в tableview



    def insert_dataframe2(self):
        file_path = QFileDialog.getOpenFileName(self, "Выбрать каталог excel ", "excel")[0]
        df2 = pd.read_excel(file_path)  # Читаем файл №2 по пути который получили

        self.new_df2 = df2 # Записываем в mew_df2 для дальнейшей работы с ним

        """Создаем объект из второй таблицы  с помощью класса pandasModel"""
        self.dataframe2 = pandasModel(df2)
        self.tableView_2.setModel(self.dataframe2) # Кладем даные в tableview



        """Метод который будет сравнивать каталоги """
    def compare_dataframe(self):
        result_df = pd.merge(self.new_df1, self.new_df2, on=["year", "month", "day", "hour", "min"], how="inner")
        self.new_df_for_saving = result_df

        """Создаем объект из второй таблицы  с помощью класса pandasModel"""
        self.dataframe_result = pandasModel(result_df)
        self.result_tableView = QTableView()
        self.result_tableView.setModel(self.dataframe_result)  # Кладем даные в Qtableview
        self.result_tableView.show()



        """Для сохранения результата"""
    def saveResult_to_excel(self):

        self.filename = QFileDialog.getSaveFileName(self, "Сохранить в excel", "table.xlsx",
                                               "Excel(*.xlsx);;"
                                               "All Files (*)")[0]

        writer = pd.ExcelWriter(self.filename, engine='xlsxwriter')

        # Записать result1 dataframe в лист1
        self.new_df_for_saving.to_excel(writer, 'Sheet1')

        # Сохранение результата
        writer.save()
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setText("Файл успешно сохранен!")
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec()




    def clicked_btn3(self):
        print("Нажата кнопка 3")

    def clicked_btn4(self):
        print("Нажата кнопка 4")

    def clicked_btn5(self):
        print("Нажата кнопка 5")

    def clicked_btn6(self):
        print("Нажата кнопка 6")





if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
