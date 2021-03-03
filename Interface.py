# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'INTERFACE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 486)
        MainWindow.setMaximumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(1000, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.Top_Bar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(70, 0))
        self.frame_toggle.setMaximumSize(QSize(110, 40))
        self.frame_toggle.setStyleSheet(u"#QPushButton{\n"
"border: 0px;\n"
"color: orange;\n"
"}\n"
"\n"
"#QPushButton{\n"
"background-color: qlineargradient(spread:repeat, x1:0.914299, y1:0.92, x2:1, y2:1, stop:0 rgba(11, 185, 107, 255), stop:1 rgba(120, 221, 176, 255))\n"
"}")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QSize(70, 0))
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(11, 122, 5);\n"
"border: 0px;")
        icon = QIcon()
        icon.addFile(u"everyday_health-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(40, 44))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(930, 16777215))
        self.frame_top.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(110, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(100, 300))
        self.frame_top_menus.setMaximumSize(QSize(1300, 16777215))
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_menu_1 = QPushButton(self.frame_top_menus)
        self.Btn_menu_1.setObjectName(u"Btn_menu_1")
        self.Btn_menu_1.setMinimumSize(QSize(0, 40))
        self.Btn_menu_1.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	font: 75 9pt \"Nirmala UI\";\n"
"	background-color: rgb(35,35,35);\n"
"	border: 0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.0511364, y2:0, stop:0.420455 rgba(16, 149, 115, 207), stop:0.914773 rgba(23, 255, 147, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_1)

        self.Btn_menu_3 = QPushButton(self.frame_top_menus)
        self.Btn_menu_3.setObjectName(u"Btn_menu_3")
        self.Btn_menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_menu_3.setMaximumSize(QSize(16777215, 40))
        self.Btn_menu_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	font: 75 9pt \"Nirmala UI\";\n"
"	background-color: rgb(35,35,35);\n"
"	border: 0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.0511364, y2:0, stop:0.420455 rgba(16, 149, 115, 207), stop:0.914773 rgba(23, 255, 147, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_3)

        self.Btn_menu_2 = QPushButton(self.frame_top_menus)
        self.Btn_menu_2.setObjectName(u"Btn_menu_2")
        self.Btn_menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_menu_2.setMaximumSize(QSize(16777215, 40))
        self.Btn_menu_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	\n"
"	\n"
"	font: 75 9pt \"Nirmala UI\";\n"
"	background-color: rgb(35,35,35);\n"
"	border: 0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.0511364, y2:0, stop:0.420455 rgba(16, 149, 115, 207), stop:0.914773 rgba(23, 255, 147, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_2)

        self.Btn_menu_4 = QPushButton(self.frame_top_menus)
        self.Btn_menu_4.setObjectName(u"Btn_menu_4")
        self.Btn_menu_4.setMinimumSize(QSize(0, 40))
        self.Btn_menu_4.setMaximumSize(QSize(16777215, 40))
        self.Btn_menu_4.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	font: 75 9pt \"Nirmala UI\";\n"
"	background-color: rgb(35,35,35);\n"
"	border: 0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.0511364, y2:0, stop:0.420455 rgba(16, 149, 115, 207), stop:0.914773 rgba(23, 255, 147, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.frame_pages)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.914299, y1:0.92, x2:1, y2:1, stop:0 rgba(11, 185, 107, 255), stop:1 rgba(120, 221, 176, 255));")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Pages.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.Pages)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.Btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"Search For a Meal", None))
        self.Btn_menu_3.setText(QCoreApplication.translate("MainWindow", u"Suggest a Meal", None))
        self.Btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"Build a Meal Plan", None))
        self.Btn_menu_4.setText(QCoreApplication.translate("MainWindow", u"Check Progress", None))
    # retranslateUi

