# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 430))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1026, 646))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1006, 626))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableView_1 = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView_1.setObjectName("tableView_2")
        self.horizontalLayout_6.addWidget(self.tableView_1)
        self.tableView_2 = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView_2.setObjectName("tableView")
        self.horizontalLayout_6.addWidget(self.tableView_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_10 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_10.setObjectName("dockWidget_10")
        self.dockWidgetContents_10 = QtWidgets.QWidget()
        self.dockWidgetContents_10.setObjectName("dockWidgetContents_10")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents_10)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents_10)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        #???????????? ?????????????? ????????????
        # self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents_10)
        # self.pushButton_3.setGeometry(QtCore.QRect(0, 60, 75, 23))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.clean_cat2_button= QtWidgets.QPushButton(self.dockWidgetContents_10)
        # self.pushButton_4.setGeometry(QtCore.QRect(0, 90, 75, 23))
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_5 = QtWidgets.QPushButton(self.dockWidgetContents_10)
        # self.pushButton_5.setGeometry(QtCore.QRect(0, 120, 75, 23))
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_6 = QtWidgets.QPushButton(self.dockWidgetContents_10)
        # self.pushButton_6.setGeometry(QtCore.QRect(0, 150, 75, 23))
        # self.pushButton_6.setObjectName("pushButton_6")

        self.dockWidget_10.setWidget(self.dockWidgetContents_10)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_10)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_new.setObjectName("action_new")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setWhatsThis("")
        self.action_save.setObjectName("action_save")
        self.action_step_back = QtWidgets.QAction(MainWindow)
        self.action_step_back.setObjectName("action_step_back")
        self.action_step_forward = QtWidgets.QAction(MainWindow)
        self.action_step_forward.setObjectName("action_step_forward")
        self.action_recently = QtWidgets.QAction(MainWindow)
        self.action_recently.setObjectName("action_recently")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_cut = QtWidgets.QAction(MainWindow)
        self.action_cut.setObjectName("action_cut")
        self.action_copy = QtWidgets.QAction(MainWindow)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(MainWindow)
        self.action_paste.setObjectName("action_paste")
        self.action_select_ll = QtWidgets.QAction(MainWindow)
        self.action_select_ll.setObjectName("action_select_ll")
        self.action_del = QtWidgets.QAction(MainWindow)
        self.action_del.setObjectName("action_del")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_parsing = QtWidgets.QAction(MainWindow)
        self.action_parsing.setObjectName("action_parsing")
        self.action_compare = QtWidgets.QAction(MainWindow)
        self.action_compare.setObjectName("action_compare")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_recently)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addAction(self.action_exit)

        """?????????? ???????? ??????????????????????????"""
        # self.menuEdit.addAction(self.action_step_forward)
        # self.menuEdit.addAction(self.action_step_back)
        # self.menuEdit.addAction(self.action_cut)
        # self.menuEdit.addAction(self.action_copy)
        # self.menuEdit.addAction(self.action_paste)
        # self.menuEdit.addAction(self.action_del)
        # self.menuEdit.addAction(self.action_select_ll)

        self.menu.addAction(self.action_11)
        self.menu_2.addAction(self.action_parsing)
        self.menu_3.addAction(self.action_compare)
        self.menubar.addAction(self.menu_3.menuAction())

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "????????"))
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ??????????????????"))

        """???????????????? ???????????? ???????? ??????????????????????????"""
        #self.menuEdit.setTitle(_translate("MainWindow", "??????????????????????????"))

        self.menu.setTitle(_translate("MainWindow", "????????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????????????"))
        self.menu_3.setTitle(_translate("MainWindow", "??????????????????"))

        self.pushButton.setText(_translate("MainWindow", "??????????????1"))
        self.pushButton.adjustSize()
        self.pushButton_2.setText(_translate("MainWindow", "??????????????2"))

        #???????????????? ???????????? ?????????????? ???? ????????????????????????
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_6.setText(_translate("MainWindow", "PushButton"))

        self.action_new.setText(_translate("MainWindow", "??????????"))
        self.action_new.setStatusTip(_translate("MainWindow", "?????????????? ?????????? ????????"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_save.setText(_translate("MainWindow", "??????????????????"))
        self.action_save.setStatusTip(_translate("MainWindow", "??????????????????"))

        # self.action_save.setShortcut(_translate("MainWindow", "Ctrl+V"))
        # self.action_step_back.setText(_translate("MainWindow", "?????? ??????????"))
        # self.action_step_back.setToolTip(_translate("MainWindow", "?????????????????????? "))
        # self.action_step_back.setStatusTip(_translate("MainWindow", "??????????????????????  ????????"))
        # self.action_step_back.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        # self.action_step_forward.setText(_translate("MainWindow", "?????? ????????????"))
        # self.action_step_forward.setStatusTip(_translate("MainWindow", "???????????????? ????????"))
        # self.action_step_forward.setShortcut(_translate("MainWindow", "Ctrl+Y"))


        self.action_recently.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.action_open.setText(_translate("MainWindow", "?????????????? "))
        self.action_open.setWhatsThis(_translate("MainWindow", "???????????? ????????"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save_as.setText(_translate("MainWindow", "?????????????????? ??????"))
        self.action_save_as.setStatusTip(_translate("MainWindow", "?????????????????? ??????"))
        self.action_save_as.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.action_exit.setText(_translate("MainWindow", "??????????"))
        self.action_exit.setStatusTip(_translate("MainWindow", "?????????? ???? ????????????????????"))
        self.action_cut.setText(_translate("MainWindow", "????????????????"))
        self.action_cut.setStatusTip(_translate("MainWindow", "????????????????"))
        self.action_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_copy.setText(_translate("MainWindow", "???????????????????? "))
        self.action_copy.setStatusTip(_translate("MainWindow", "????????????????????"))
        self.action_paste.setText(_translate("MainWindow", "????????????????"))
        self.action_paste.setStatusTip(_translate("MainWindow", "????????????????"))
        self.action_paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_select_ll.setText(_translate("MainWindow", "?????????????? ??????"))
        self.action_select_ll.setStatusTip(_translate("MainWindow", "????????????????????"))
        self.action_select_ll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_del.setText(_translate("MainWindow", "??????????????"))
        self.action_del.setStatusTip(_translate("MainWindow", "??????????????"))
        self.action_del.setShortcut(_translate("MainWindow", "Del"))
        self.action_11.setText(_translate("MainWindow", "????????????????????"))
        self.action_parsing.setText(_translate("MainWindow", "?????????????????? ????????????????????"))
        self.action_parsing.setStatusTip(_translate("MainWindow", "?????????????? ???????????? ?? ??????????"))
        self.action_compare.setText(_translate("MainWindow", "???????????????? ????????????????"))

