# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1225, 1954)
        icon = QIcon()
        icon.addFile(u":/images/resources/detail_logo.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* 1. Set border-image background on QMainWindow */\n"
"QMainWindow {\n"
"	border-image: url(\":/images/resources/background.png\") 0 0 0 0 stretch stretch;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"}\n"
"\n"
"/* 2. Menubar opaque in black */\n"
"QMenuBar {\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Optional: menu item hover style */\n"
"QMenuBar::item:selected {\n"
"    background: #444;\n"
"}\n"
"\n"
"/* 3. All \"blank_space\" transparent */\n"
"#blank_space_left,\n"
"#blank_space_middle_left,\n"
"#blank_space_middle_right,\n"
"#blank_space_right {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 4. mainbody and all contents transparent */\n"
"#mainbody,\n"
"#mb_content,\n"
"#mb_frame1,\n"
"#mb_frame2,\n"
"#device_image,\n"
"#mb_frame1A, #mb_label1A,\n"
"#mb_frame2A, #mb_label2A,\n"
"#mb_frame3A, #mb_label3A,\n"
"#mb_frame3, #mb_button1, #mb_button2, #mb_button3, #mb_button4 {\n"
"    background-c"
                        "olor: transparent;\n"
"}\n"
"\n"
"/* 4b. EXCEPTION: mb_frameB and mb_frameC and contents semi-transparent */\n"
"#mb_frameB,\n"
"#mb_frameC,\n"
"#mb_frameB1, #mb_label1B, #mb_label2B, #mb_label3B,\n"
"#mb_frameC1, #mb_label1C, #mb_label2C, #mb_label3C {\n"
"    background-color: rgba(0, 0, 0, 70);\n"
"}\n"
"\n"
"/* 5. menuleft and contents transparent */\n"
"#menuleft,\n"
"#brand_logo,\n"
"#ml_frame0, #ml_button1,\n"
"#ml_frame1, #ml_frameA, #ml_label1A, #ml_label2A, #ml_label3A,\n"
"#ml_frameB, #ml_label1B, #ml_label2B, #ml_label3B,\n"
"#ml_frameC, #ml_label1C, #ml_label2C, #ml_label3C {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 5b. EXCEPTION: ml_content and its contents semi-transparent */\n"
"#ml_content,\n"
"#ml_frame0, #ml_button1,\n"
"#ml_frame1, #ml_frameA, #ml_label1A, #ml_label2A, #ml_label3A,\n"
"#ml_frameB, #ml_label1B, #ml_label2B, #ml_label3B,\n"
"#ml_frameC, #ml_label1C, #ml_label2C, #ml_label3C {\n"
"    background-color: rgba(0, 0, 0, 70);\n"
"}\n"
"\n"
"/* 6. menuright and all i"
                        "ts contents semi-transparent */\n"
"#menuright,\n"
"#mr_content,\n"
"#mr_frame1, #progress_bar,\n"
"#mr_frame2,\n"
"#mr_frameA, #mr_frameA1, #mr_buttonA1, #mr_label1A1, #mr_label2A1,\n"
"#mr_frameA2, #mr_buttonA2, #mr_label1A2, #mr_label2A2,\n"
"#mr_frameB, #mr_frameB1, #mr_buttonB1, #mr_label1B1, #mr_label2B1,\n"
"#mr_frameB2, #mr_buttonB2, #mr_label1B2, #mr_label2B2,\n"
"#mr_frameC, #mr_frameC1, #mr_buttonC1, #mr_label1C1, #mr_label2C1,\n"
"#mr_frameC2, #mr_buttonC2, #mr_label1C2, #mr_label2C2,\n"
"#mr_frameD, #mr_frameD1, #mr_buttonD1, #mr_label1D1, #mr_label2D1,\n"
"#mr_frameD2, #mr_buttonD2, #mr_label1D2, #mr_label2D2,\n"
"#mr_frame3, #program_name {\n"
"    background-color: rgba(0, 0, 0, 70);\n"
"}\n"
"")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.blank_space_left = QFrame(self.centralwidget)
        self.blank_space_left.setObjectName(u"blank_space_left")
        self.blank_space_left.setMaximumSize(QSize(25, 16777215))
        self.blank_space_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.blank_space_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.blank_space_left)

        self.menuleft = QFrame(self.centralwidget)
        self.menuleft.setObjectName(u"menuleft")
        self.menuleft.setMaximumSize(QSize(300, 16777215))
        self.menuleft.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuleft.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.menuleft)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.brand_logo = QLabel(self.menuleft)
        self.brand_logo.setObjectName(u"brand_logo")
        self.brand_logo.setMinimumSize(QSize(0, 0))
        self.brand_logo.setMaximumSize(QSize(16777215, 100))
        self.brand_logo.setText(u"")
        self.brand_logo.setTextFormat(Qt.TextFormat.RichText)
        self.brand_logo.setPixmap(QPixmap(u":/images/resources/full_logo_nobg.png"))
        self.brand_logo.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.brand_logo)

        self.ml_content = QFrame(self.menuleft)
        self.ml_content.setObjectName(u"ml_content")
        self.ml_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_content.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ml_content)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ml_frame0 = QFrame(self.ml_content)
        self.ml_frame0.setObjectName(u"ml_frame0")
        self.ml_frame0.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frame0.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.ml_frame0)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.ml_frame1 = QFrame(self.ml_frame0)
        self.ml_frame1.setObjectName(u"ml_frame1")
        self.ml_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ml_frame1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.ml_frameA = QFrame(self.ml_frame1)
        self.ml_frameA.setObjectName(u"ml_frameA")
        self.ml_frameA.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frameA.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ml_frameA)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ml_label1A = QLabel(self.ml_frameA)
        self.ml_label1A.setObjectName(u"ml_label1A")
        self.ml_label1A.setPixmap(QPixmap(u":/icons/resources/device_thermostat.svg"))

        self.horizontalLayout_2.addWidget(self.ml_label1A, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label2A = QLabel(self.ml_frameA)
        self.ml_label2A.setObjectName(u"ml_label2A")

        self.horizontalLayout_2.addWidget(self.ml_label2A, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label3A = QLabel(self.ml_frameA)
        self.ml_label3A.setObjectName(u"ml_label3A")

        self.horizontalLayout_2.addWidget(self.ml_label3A)


        self.verticalLayout_3.addWidget(self.ml_frameA, 0, Qt.AlignmentFlag.AlignTop)

        self.ml_frameB = QFrame(self.ml_frame1)
        self.ml_frameB.setObjectName(u"ml_frameB")
        self.ml_frameB.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frameB.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ml_frameB)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ml_label1B = QLabel(self.ml_frameB)
        self.ml_label1B.setObjectName(u"ml_label1B")
        self.ml_label1B.setPixmap(QPixmap(u":/icons/resources/thermometer.svg"))

        self.horizontalLayout_4.addWidget(self.ml_label1B, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label2B = QLabel(self.ml_frameB)
        self.ml_label2B.setObjectName(u"ml_label2B")

        self.horizontalLayout_4.addWidget(self.ml_label2B, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label3B = QLabel(self.ml_frameB)
        self.ml_label3B.setObjectName(u"ml_label3B")

        self.horizontalLayout_4.addWidget(self.ml_label3B)


        self.verticalLayout_3.addWidget(self.ml_frameB, 0, Qt.AlignmentFlag.AlignTop)

        self.ml_frameC = QFrame(self.ml_frame1)
        self.ml_frameC.setObjectName(u"ml_frameC")
        self.ml_frameC.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frameC.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ml_frameC)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ml_label1C = QLabel(self.ml_frameC)
        self.ml_label1C.setObjectName(u"ml_label1C")
        self.ml_label1C.setPixmap(QPixmap(u":/icons/resources/humidity.svg"))

        self.horizontalLayout_5.addWidget(self.ml_label1C, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label2C = QLabel(self.ml_frameC)
        self.ml_label2C.setObjectName(u"ml_label2C")

        self.horizontalLayout_5.addWidget(self.ml_label2C, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label3C = QLabel(self.ml_frameC)
        self.ml_label3C.setObjectName(u"ml_label3C")

        self.horizontalLayout_5.addWidget(self.ml_label3C)


        self.verticalLayout_3.addWidget(self.ml_frameC, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_22.addWidget(self.ml_frame1)

        self.ml_button1 = QPushButton(self.ml_frame0)
        self.ml_button1.setObjectName(u"ml_button1")
        self.ml_button1.setMaximumSize(QSize(16777215, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/build_edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ml_button1.setIcon(icon1)

        self.verticalLayout_22.addWidget(self.ml_button1)


        self.verticalLayout_6.addWidget(self.ml_frame0)


        self.verticalLayout_21.addWidget(self.ml_content)


        self.horizontalLayout.addWidget(self.menuleft)

        self.blank_space_middle_left = QFrame(self.centralwidget)
        self.blank_space_middle_left.setObjectName(u"blank_space_middle_left")
        self.blank_space_middle_left.setMaximumSize(QSize(25, 16777215))
        self.blank_space_middle_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.blank_space_middle_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.blank_space_middle_left)

        self.mainbody = QFrame(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        font = QFont()
        font.setKerning(False)
        self.mainbody.setFont(font)
        self.mainbody.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainbody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainbody)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.mb_content = QFrame(self.mainbody)
        self.mb_content.setObjectName(u"mb_content")
        self.mb_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_content.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mb_content)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.mb_frame1 = QFrame(self.mb_content)
        self.mb_frame1.setObjectName(u"mb_frame1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mb_frame1.sizePolicy().hasHeightForWidth())
        self.mb_frame1.setSizePolicy(sizePolicy)
        self.mb_frame1.setMinimumSize(QSize(0, 0))
        self.mb_frame1.setMaximumSize(QSize(16777215, 16777215))
        self.mb_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.mb_frame1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.device_image = QLabel(self.mb_frame1)
        self.device_image.setObjectName(u"device_image")
        sizePolicy.setHeightForWidth(self.device_image.sizePolicy().hasHeightForWidth())
        self.device_image.setSizePolicy(sizePolicy)
        self.device_image.setMaximumSize(QSize(550, 16777215))
        self.device_image.setPixmap(QPixmap(u":/images/resources/telescope_nobg.png"))
        self.device_image.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.device_image)


        self.verticalLayout_5.addWidget(self.mb_frame1)

        self.mb_frame2 = QFrame(self.mb_content)
        self.mb_frame2.setObjectName(u"mb_frame2")
        sizePolicy.setHeightForWidth(self.mb_frame2.sizePolicy().hasHeightForWidth())
        self.mb_frame2.setSizePolicy(sizePolicy)
        self.mb_frame2.setMinimumSize(QSize(0, 175))
        self.mb_frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mb_frame2)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.mr_frameA = QFrame(self.mb_frame2)
        self.mr_frameA.setObjectName(u"mr_frameA")
        self.mr_frameA.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameA.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.mr_frameA)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.mr_frameA)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.HLine)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 858, 144))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_7)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_13)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(64, 64))

        self.verticalLayout_24.addWidget(self.pushButton_7)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_14)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(64, 64))

        self.verticalLayout_15.addWidget(self.pushButton_6)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_12)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(64, 64))

        self.verticalLayout_14.addWidget(self.pushButton_5)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_7.addWidget(self.pushButton)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_8.addWidget(self.frame)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_9)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_17)

        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(64, 64))

        self.verticalLayout_26.addWidget(self.pushButton_9)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_18)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_8)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_15)

        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(64, 64))

        self.verticalLayout_25.addWidget(self.pushButton_8)

        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(64, 64))

        self.verticalLayout_10.addWidget(self.pushButton_4)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)


        self.horizontalLayout_8.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(64, 64))

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(64, 64))

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_11.addWidget(self.scrollArea)


        self.horizontalLayout_7.addWidget(self.mr_frameA)


        self.verticalLayout_5.addWidget(self.mb_frame2)

        self.frame_10 = QFrame(self.mb_content)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 125))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/log_monitor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(64, 64))

        self.verticalLayout_27.addWidget(self.pushButton_10)

        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_19)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.pushButton_13 = QPushButton(self.frame_14)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/folder_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(64, 64))

        self.verticalLayout_30.addWidget(self.pushButton_13)

        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_22)


        self.horizontalLayout_6.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.pushButton_12 = QPushButton(self.frame_13)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/apps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(64, 64))

        self.verticalLayout_29.addWidget(self.pushButton_12)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_21)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon6 = QIcon()
        icon6.addFile(u":/icons/resources/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QSize(64, 64))

        self.verticalLayout_28.addWidget(self.pushButton_11)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_20)


        self.horizontalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.mb_content)


        self.horizontalLayout.addWidget(self.mainbody)

        self.blank_space_middle_right = QFrame(self.centralwidget)
        self.blank_space_middle_right.setObjectName(u"blank_space_middle_right")
        self.blank_space_middle_right.setMaximumSize(QSize(25, 16777215))
        self.blank_space_middle_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.blank_space_middle_right.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.blank_space_middle_right)

        self.menuright = QFrame(self.centralwidget)
        self.menuright.setObjectName(u"menuright")
        self.menuright.setMaximumSize(QSize(300, 16777215))
        self.menuright.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuright.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.menuright)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.mr_content = QFrame(self.menuright)
        self.mr_content.setObjectName(u"mr_content")
        self.mr_content.setMinimumSize(QSize(0, 0))
        self.mr_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_content.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.mr_content)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.mr_frame1 = QFrame(self.mr_content)
        self.mr_frame1.setObjectName(u"mr_frame1")
        self.mr_frame1.setMaximumSize(QSize(16777215, 35))
        self.mr_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.mr_frame1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.progress_bar = QProgressBar(self.mr_frame1)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(90)

        self.verticalLayout_20.addWidget(self.progress_bar)


        self.verticalLayout_23.addWidget(self.mr_frame1)

        self.mr_frame2 = QFrame(self.mr_content)
        self.mr_frame2.setObjectName(u"mr_frame2")
        self.mr_frame2.setMinimumSize(QSize(0, 600))
        self.mr_frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.mr_frame2)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.mr_frameA1 = QFrame(self.mr_frame2)
        self.mr_frameA1.setObjectName(u"mr_frameA1")
        self.mr_frameA1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameA1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.mr_frameA1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.mr_label1A1 = QLabel(self.mr_frameA1)
        self.mr_label1A1.setObjectName(u"mr_label1A1")

        self.verticalLayout_12.addWidget(self.mr_label1A1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.mr_buttonA1 = QPushButton(self.mr_frameA1)
        self.mr_buttonA1.setObjectName(u"mr_buttonA1")
        self.mr_buttonA1.setIcon(icon2)
        self.mr_buttonA1.setIconSize(QSize(64, 64))

        self.verticalLayout_12.addWidget(self.mr_buttonA1)

        self.mr_label2A1 = QLabel(self.mr_frameA1)
        self.mr_label2A1.setObjectName(u"mr_label2A1")

        self.verticalLayout_12.addWidget(self.mr_label2A1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_11.addWidget(self.mr_frameA1)

        self.mr_frameC = QFrame(self.mr_frame2)
        self.mr_frameC.setObjectName(u"mr_frameC")
        self.mr_frameC.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameC.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.mr_frameC)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.mr_frameC1 = QFrame(self.mr_frameC)
        self.mr_frameC1.setObjectName(u"mr_frameC1")
        self.mr_frameC1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameC1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.mr_frameC1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.mr_label1C1 = QLabel(self.mr_frameC1)
        self.mr_label1C1.setObjectName(u"mr_label1C1")

        self.verticalLayout_16.addWidget(self.mr_label1C1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.mr_buttonC1 = QPushButton(self.mr_frameC1)
        self.mr_buttonC1.setObjectName(u"mr_buttonC1")
        self.mr_buttonC1.setIcon(icon2)
        self.mr_buttonC1.setIconSize(QSize(64, 64))

        self.verticalLayout_16.addWidget(self.mr_buttonC1)

        self.mr_label2C1 = QLabel(self.mr_frameC1)
        self.mr_label2C1.setObjectName(u"mr_label2C1")

        self.verticalLayout_16.addWidget(self.mr_label2C1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_13.addWidget(self.mr_frameC1)

        self.mr_frameC2 = QFrame(self.mr_frameC)
        self.mr_frameC2.setObjectName(u"mr_frameC2")
        self.mr_frameC2.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameC2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.mr_frameC2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.mr_label1C2 = QLabel(self.mr_frameC2)
        self.mr_label1C2.setObjectName(u"mr_label1C2")

        self.verticalLayout_17.addWidget(self.mr_label1C2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.mr_buttonC2 = QPushButton(self.mr_frameC2)
        self.mr_buttonC2.setObjectName(u"mr_buttonC2")
        self.mr_buttonC2.setIcon(icon2)
        self.mr_buttonC2.setIconSize(QSize(64, 64))

        self.verticalLayout_17.addWidget(self.mr_buttonC2)

        self.mr_label2C2 = QLabel(self.mr_frameC2)
        self.mr_label2C2.setObjectName(u"mr_label2C2")

        self.verticalLayout_17.addWidget(self.mr_label2C2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_13.addWidget(self.mr_frameC2)


        self.verticalLayout_11.addWidget(self.mr_frameC)

        self.mr_frameD = QFrame(self.mr_frame2)
        self.mr_frameD.setObjectName(u"mr_frameD")
        self.mr_frameD.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameD.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.mr_frameD)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.mr_frameD1 = QFrame(self.mr_frameD)
        self.mr_frameD1.setObjectName(u"mr_frameD1")
        self.mr_frameD1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameD1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.mr_frameD1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.mr_label1D1 = QLabel(self.mr_frameD1)
        self.mr_label1D1.setObjectName(u"mr_label1D1")

        self.verticalLayout_18.addWidget(self.mr_label1D1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.mr_buttonD1 = QPushButton(self.mr_frameD1)
        self.mr_buttonD1.setObjectName(u"mr_buttonD1")
        self.mr_buttonD1.setIcon(icon2)
        self.mr_buttonD1.setIconSize(QSize(64, 64))

        self.verticalLayout_18.addWidget(self.mr_buttonD1)

        self.mr_label2D1 = QLabel(self.mr_frameD1)
        self.mr_label2D1.setObjectName(u"mr_label2D1")

        self.verticalLayout_18.addWidget(self.mr_label2D1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_14.addWidget(self.mr_frameD1)

        self.mr_frameD2 = QFrame(self.mr_frameD)
        self.mr_frameD2.setObjectName(u"mr_frameD2")
        self.mr_frameD2.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frameD2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.mr_frameD2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.mr_label1D2 = QLabel(self.mr_frameD2)
        self.mr_label1D2.setObjectName(u"mr_label1D2")

        self.verticalLayout_19.addWidget(self.mr_label1D2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.mr_buttonD2 = QPushButton(self.mr_frameD2)
        self.mr_buttonD2.setObjectName(u"mr_buttonD2")
        self.mr_buttonD2.setIcon(icon2)
        self.mr_buttonD2.setIconSize(QSize(64, 64))

        self.verticalLayout_19.addWidget(self.mr_buttonD2)

        self.mr_label2D2 = QLabel(self.mr_frameD2)
        self.mr_label2D2.setObjectName(u"mr_label2D2")

        self.verticalLayout_19.addWidget(self.mr_label2D2, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_14.addWidget(self.mr_frameD2)


        self.verticalLayout_11.addWidget(self.mr_frameD)


        self.verticalLayout_23.addWidget(self.mr_frame2)

        self.mr_frame3 = QFrame(self.mr_content)
        self.mr_frame3.setObjectName(u"mr_frame3")
        self.mr_frame3.setMaximumSize(QSize(16777215, 35))
        self.mr_frame3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mr_frame3.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mr_frame3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.program_name = QLabel(self.mr_frame3)
        self.program_name.setObjectName(u"program_name")

        self.verticalLayout_4.addWidget(self.program_name, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_23.addWidget(self.mr_frame3)


        self.verticalLayout.addWidget(self.mr_content)


        self.horizontalLayout.addWidget(self.menuright)

        self.blank_space_right = QFrame(self.centralwidget)
        self.blank_space_right.setObjectName(u"blank_space_right")
        self.blank_space_right.setMaximumSize(QSize(25, 16777215))
        self.blank_space_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.blank_space_right.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.blank_space_right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1225, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CaeBell 1.0", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About CaeBell", None))
#if QT_CONFIG(statustip)
        self.brand_logo.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.ml_label1A.setText("")
        self.ml_label2A.setText(QCoreApplication.translate("MainWindow", u"Telescope:", None))
        self.ml_label3A.setText(QCoreApplication.translate("MainWindow", u"...C\u00ba", None))
        self.ml_label1B.setText("")
        self.ml_label2B.setText(QCoreApplication.translate("MainWindow", u"Guidescope:", None))
        self.ml_label3B.setText(QCoreApplication.translate("MainWindow", u"...C\u00ba", None))
        self.ml_label1C.setText("")
        self.ml_label2C.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.ml_label3C.setText(QCoreApplication.translate("MainWindow", u"...%", None))
        self.ml_button1.setText(QCoreApplication.translate("MainWindow", u" Control Panel", None))
        self.device_image.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_7.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_6.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_5.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_9.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_8.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Add more...", None))
        self.pushButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_10.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.pushButton_13.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"File Explorer", None))
        self.pushButton_12.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Astro Apps", None))
        self.pushButton_11.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.mr_label1A1.setText(QCoreApplication.translate("MainWindow", u"Port 1", None))
        self.mr_buttonA1.setText("")
        self.mr_label2A1.setText(QCoreApplication.translate("MainWindow", u"Element 1", None))
        self.mr_label1C1.setText(QCoreApplication.translate("MainWindow", u"Port 3", None))
        self.mr_buttonC1.setText("")
        self.mr_label2C1.setText(QCoreApplication.translate("MainWindow", u"Element 5", None))
        self.mr_label1C2.setText(QCoreApplication.translate("MainWindow", u"Port 3", None))
        self.mr_buttonC2.setText("")
        self.mr_label2C2.setText(QCoreApplication.translate("MainWindow", u"Element 6", None))
        self.mr_label1D1.setText(QCoreApplication.translate("MainWindow", u"Port 4", None))
        self.mr_buttonD1.setText("")
        self.mr_label2D1.setText(QCoreApplication.translate("MainWindow", u"Element 7", None))
        self.mr_label1D2.setText(QCoreApplication.translate("MainWindow", u"Add more...", None))
        self.mr_buttonD2.setText("")
        self.mr_label2D2.setText("")
        self.program_name.setText(QCoreApplication.translate("MainWindow", u"CaeBell\u00ae", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

