# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_tample3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 787)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_data_button = QtWidgets.QToolButton(self.widget)
        self.import_data_button.setStyleSheet("import_data_button{ color: red; background-color: green }")
        self.import_data_button.setCheckable(True)
        self.import_data_button.setAutoExclusive(True)
        self.import_data_button.setObjectName("import_data_button")
        self.horizontalLayout.addWidget(self.import_data_button)
        self.comparing_button = QtWidgets.QToolButton(self.widget)
        self.comparing_button.setCheckable(True)
        self.comparing_button.setAutoExclusive(True)
        self.comparing_button.setObjectName("comparing_button")
        self.horizontalLayout.addWidget(self.comparing_button)
        self.result_button = QtWidgets.QToolButton(self.widget)
        self.result_button.setCheckable(True)
        self.result_button.setAutoExclusive(True)
        self.result_button.setObjectName("result_button")
        self.horizontalLayout.addWidget(self.result_button)
        self.graphics_button = QtWidgets.QToolButton(self.widget)
        self.graphics_button.setCheckable(True)
        self.graphics_button.setAutoExclusive(True)
        self.graphics_button.setObjectName("graphics_button")
        self.horizontalLayout.addWidget(self.graphics_button)
        self.verticalLayout_2.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.import_data_page = QtWidgets.QWidget()
        self.import_data_page.setObjectName("import_data_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.import_data_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.import_data_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView_cat2 = QtWidgets.QTableView(self.frame)
        self.tableView_cat2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tableView_cat2.setObjectName("tableView_cat2")
        self.gridLayout.addWidget(self.tableView_cat2, 5, 0, 1, 1)
        self.tableView_cat1 = QtWidgets.QTableView(self.frame)
        self.tableView_cat1.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tableView_cat1.setObjectName("tableView_cat1")
        self.gridLayout.addWidget(self.tableView_cat1, 3, 0, 1, 1)
        self.plainTextEdit_cat1 = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_cat1.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_cat1.setSizePolicy(sizePolicy)
        self.plainTextEdit_cat1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.plainTextEdit_cat1.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_cat1.setPlainText("")
        self.plainTextEdit_cat1.setObjectName("plainTextEdit_cat1")
        self.gridLayout.addWidget(self.plainTextEdit_cat1, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.plainTextEdit_cat2 = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_cat2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_cat2.setSizePolicy(sizePolicy)
        self.plainTextEdit_cat2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.plainTextEdit_cat2.setPlainText("")
        self.plainTextEdit_cat2.setObjectName("plainTextEdit_cat2")
        self.gridLayout.addWidget(self.plainTextEdit_cat2, 4, 0, 1, 1)
        self.pushButton_cat1 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cat1.setFont(font)
        self.pushButton_cat1.setObjectName("pushButton_cat1")
        self.gridLayout.addWidget(self.pushButton_cat1, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_cat2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cat2.setFont(font)
        self.pushButton_cat2.setObjectName("pushButton_cat2")
        self.gridLayout.addWidget(self.pushButton_cat2, 4, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.stackedWidget.addWidget(self.import_data_page)
        self.comparing_page = QtWidgets.QWidget()
        self.comparing_page.setObjectName("comparing_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.comparing_page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.comparing_page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.tableView_2 = QtWidgets.QTableView(self.frame_3)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout.addWidget(self.tableView_2)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.tableView_1 = QtWidgets.QTableView(self.frame_3)
        self.tableView_1.setObjectName("tableView_1")
        self.verticalLayout.addWidget(self.tableView_1)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.comparing_page)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.compare_cats = QtWidgets.QPushButton(self.comparing_page)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.compare_cats.setFont(font)
        self.compare_cats.setObjectName("compare_cats")
        self.verticalLayout_6.addWidget(self.compare_cats)
        self.stackedWidget.addWidget(self.comparing_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.result_page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.result_tableView = QtWidgets.QTableView(self.result_page)
        self.result_tableView.setObjectName("result_tableView")
        self.horizontalLayout_4.addWidget(self.result_tableView)
        self.stackedWidget.addWidget(self.result_page)
        self.graphics_page = QtWidgets.QWidget()
        self.graphics_page.setObjectName("graphics_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.graphics_page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphics_widget = QtWidgets.QWidget(self.graphics_page)
        self.graphics_widget.setObjectName("graphics_widget")

        # self.label_2 = QtWidgets.QLabel(self.graphics_widget)
        # self.label_2.setGeometry(QtCore.QRect(260, -20, 444, 667))
        # self.label_2.setObjectName("label_2")

        self.horizontalLayout_5.addWidget(self.graphics_widget)
        self.stackedWidget.addWidget(self.graphics_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.menu_2.addAction(self.action_save_as)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_data_button.setText(_translate("MainWindow", "???????????? ????????????"))
        self.comparing_button.setText(_translate("MainWindow", "??????????????????"))
        self.result_button.setText(_translate("MainWindow", "??????????????????"))
        self.graphics_button.setText(_translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????? --> ?? ??????????????????"))
        self.pushButton_cat1.setText(_translate("MainWindow", "?????????????? 1"))
        self.label_3.setText(_translate("MainWindow", "???????????????? Excel ?????????? ?????? ????????????????????????????"))
        self.pushButton_cat2.setText(_translate("MainWindow", "?????????????? 2"))
        self.label.setText(_translate("MainWindow", "?????????????? 1"))
        self.label_4.setText(_translate("MainWindow", "?????????????? 2"))
        self.label_5.setText(_translate("MainWindow", "???????????????? ???? ?????????? ???????????????? ????????????????????"))
        self.checkBox_2.setText(_translate("MainWindow", "year"))
        self.checkBox.setText(_translate("MainWindow", "month"))
        self.checkBox_3.setText(_translate("MainWindow", "day"))
        self.checkBox_4.setText(_translate("MainWindow", "hour"))
        self.checkBox_5.setText(_translate("MainWindow", "min"))
        self.checkBox_6.setText(_translate("MainWindow", "sec"))
        self.compare_cats.setText(_translate("MainWindow", "????????????????"))
        # self.label_2.setText(_translate("MainWindow", "Graphics_page"))
        self.menu_2.setTitle(_translate("MainWindow", "????????"))
        self.menu_3.setTitle(_translate("MainWindow", "????????????"))
        self.menu.setTitle(_translate("MainWindow", "??????????????????"))
        self.action_save_as.setText(_translate("MainWindow", "?????????????????? ??????"))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+S"))

