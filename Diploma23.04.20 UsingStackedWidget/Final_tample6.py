# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_tample6.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 724)
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
        self.import_data_button.setStyleSheet("import_data_button{ color: red; background-color: white }")
        #self.import_data_button.setCheckable(True)
        #self.import_data_button.setAutoExclusive(True)
        self.import_data_button.setObjectName("import_data_button")
        self.horizontalLayout.addWidget(self.import_data_button)
        self.comparing_button = QtWidgets.QToolButton(self.widget)
        #self.comparing_button.setCheckable(True)
        #self.comparing_button.setAutoExclusive(True)
        self.comparing_button.setObjectName("comparing_button")
        self.horizontalLayout.addWidget(self.comparing_button)
        self.result_button = QtWidgets.QToolButton(self.widget)
        #self.result_button.setCheckable(True)
        #self.result_button.setAutoExclusive(True)
        self.result_button.setObjectName("result_button")
        self.horizontalLayout.addWidget(self.result_button)
        self.graphics_button = QtWidgets.QToolButton(self.widget)
        self.graphics_button.setCheckable(True)
        #self.graphics_button.setAutoExclusive(True)
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
        self.tableView_1 = QtWidgets.QTableView(self.frame_3)
        self.tableView_1.setObjectName("tableView_1")
        self.verticalLayout.addWidget(self.tableView_1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.tableView_2 = QtWidgets.QTableView(self.frame_3)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout.addWidget(self.tableView_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_year = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_year.setObjectName("checkBox_year")
        self.gridLayout_3.addWidget(self.checkBox_year, 1, 0, 1, 1)
        self.checkBox_day = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_day.setObjectName("checkBox_day")
        self.gridLayout_3.addWidget(self.checkBox_day, 1, 2, 1, 1)
        self.checkBox_hour = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_hour.setObjectName("checkBox_hour")
        self.gridLayout_3.addWidget(self.checkBox_hour, 2, 2, 1, 1)
        self.checkBox_month = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_month.setObjectName("checkBox_month")
        self.gridLayout_3.addWidget(self.checkBox_month, 2, 0, 1, 1)
        self.checkBox_sec = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_sec.setObjectName("checkBox_sec")
        self.gridLayout_3.addWidget(self.checkBox_sec, 2, 3, 1, 1)
        self.checkBox_min = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_min.setObjectName("checkBox_min")
        self.gridLayout_3.addWidget(self.checkBox_min, 1, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.compare_cats = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.compare_cats.setFont(font)
        self.compare_cats.setObjectName("compare_cats")
        self.gridLayout_4.addWidget(self.compare_cats, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.comparing_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.result_page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.result_page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.result_tableView = QtWidgets.QTableView(self.result_page)
        self.result_tableView.setObjectName("result_tableView")
        self.gridLayout_2.addWidget(self.result_tableView, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.result_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_mpv_diff = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_mpv_diff.setObjectName("checkBox_mpv_diff")
        self.horizontalLayout_2.addWidget(self.checkBox_mpv_diff)
        self.checkBox_depth_diff = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_depth_diff.setObjectName("checkBox_depth_diff")
        self.horizontalLayout_2.addWidget(self.checkBox_depth_diff)
        self.checkBox_lat_lon_diff = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_lat_lon_diff.setObjectName("checkBox_lat_lon_diff")
        self.horizontalLayout_2.addWidget(self.checkBox_lat_lon_diff)
        self.PushButton_build_graphics = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PushButton_build_graphics.setFont(font)
        self.PushButton_build_graphics.setObjectName("PushButton_build_graphics")
        self.horizontalLayout_2.addWidget(self.PushButton_build_graphics)
        self.gridLayout_2.addWidget(self.frame_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.result_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.result_page)
        self.graphics_page = QtWidgets.QWidget()
        self.graphics_page.setObjectName("graphics_page")
        self._2 = QtWidgets.QHBoxLayout(self.graphics_page)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.tabWidget_for_graphics = QtWidgets.QTabWidget(self.graphics_page)
        self.tabWidget_for_graphics.setObjectName("tabWidget_for_graphics")
        self.tab_mpv_diff = QtWidgets.QWidget()
        self.tab_mpv_diff.setObjectName("tab_mpv_diff")
        self.tabWidget_for_graphics.addTab(self.tab_mpv_diff, "")
        self.tab_depth_diff = QtWidgets.QWidget()
        self.tab_depth_diff.setObjectName("tab_depth_diff")
        self.tabWidget_for_graphics.addTab(self.tab_depth_diff, "")
        self.tab_lat_lon_diff = QtWidgets.QWidget()
        self.tab_lat_lon_diff.setObjectName("tab_lat_lon_diff")
        self.tabWidget_for_graphics.addTab(self.tab_lat_lon_diff, "")
        self._2.addWidget(self.tabWidget_for_graphics)
        self.stackedWidget.addWidget(self.graphics_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
       # self.menu = QtWidgets.QMenu(self.menubar)
        #self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.menu_2.addAction(self.action_save_as)
        self.menubar.addAction(self.menu_2.menuAction())
        #self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_for_graphics.setCurrentIndex(0)
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
        self.checkBox_year.setText(_translate("MainWindow", "year"))
        self.checkBox_day.setText(_translate("MainWindow", "day"))
        self.checkBox_hour.setText(_translate("MainWindow", "hour"))
        self.checkBox_month.setText(_translate("MainWindow", "month"))
        self.checkBox_sec.setText(_translate("MainWindow", "sec"))
        self.checkBox_min.setText(_translate("MainWindow", "min"))
        self.compare_cats.setText(_translate("MainWindow", "????????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        self.checkBox_mpv_diff.setText(_translate("MainWindow", "?????????????? mpv"))
        self.checkBox_depth_diff.setText(_translate("MainWindow", "?????????????? depth"))
        self.checkBox_lat_lon_diff.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.PushButton_build_graphics.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.label_6.setText(_translate("MainWindow", "???????????????? ???? ?????????? ???????????????? ?????????????? ????????????"))
        self.tabWidget_for_graphics.setTabText(self.tabWidget_for_graphics.indexOf(self.tab_mpv_diff), _translate("MainWindow", "?????????????? mpv"))
        self.tabWidget_for_graphics.setTabText(self.tabWidget_for_graphics.indexOf(self.tab_depth_diff), _translate("MainWindow", "?????????????? depth"))
        self.tabWidget_for_graphics.setTabText(self.tabWidget_for_graphics.indexOf(self.tab_lat_lon_diff), _translate("MainWindow", "?????????????? ??????????????????"))
        self.menu_2.setTitle(_translate("MainWindow", "????????"))
        self.menu_3.setTitle(_translate("MainWindow", "????????????"))
       # self.menu.setTitle(_translate("MainWindow", "??????????????????"))
        self.action_save_as.setText(_translate("MainWindow", "?????????????????? ??????"))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+S"))

