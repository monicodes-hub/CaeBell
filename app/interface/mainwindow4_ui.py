# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow4.ui'
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
import app.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1225, 732)
        icon = QIcon()
        icon.addFile(u":/images/resources/detail_logo.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* 1. Set border-image background on QMainWindow */\n"
"QMainWindow {\n"
"	border-image: url(\":/images/background.png\") 0 0 0 0 stretch stretch;\n"
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
"/* Make mainbody and all children fully transparent */\n"
"#mainbody,\n"
"#mainbody * {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* QPushButtons inside mainbody */\n"
"#mainbody QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: white; /* or any text color "
                        "you prefer */\n"
"}\n"
"\n"
"/* Hover effect for QPushButtons */\n"
"#mainbody QPushButton:hover {\n"
"    background: rgba(255, 255, 255, 40); /* subtle white overlay */\n"
"    border-radius: 4px; /* optional rounding */\n"
"}\n"
"\n"
"\n"
"/* 5. menuleft and contents transparent */\n"
"#menuleft,\n"
"#brand_logo,\n"
"#ml_frame0, #ml_button1,\n"
"#ml_frame1, #ml_frameA, #ml_label1A, #ml_label2A, #ml_label3A,\n"
"#ml_frameB, #ml_label1B, #ml_label2B, #ml_label3B,\n"
"#ml_frameC, #ml_label1C, #ml_label2C, #ml_label3C {\n"
"    background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"/* 5b. EXCEPTION: ml_content and its contents semi-transparent */\n"
"#ml_content,\n"
"#ml_frame0, #ml_button1,\n"
"#ml_frame1, #ml_frameA, #ml_label1A, #ml_label2A, #ml_label3A,\n"
"#ml_frameB, #ml_label1B, #ml_label2B, #ml_label3B,\n"
"#ml_frameC, #ml_label1C, #ml_label2C, #ml_label3C {\n"
"    background-color: rgba(0, 0, 0, 70);\n"
"	border: none;\n"
"}\n"
"\n"
"/* 6. menuright and all its contents semi-transparent */\n"
""
                        "#menuright,\n"
"#mr_content,\n"
"#mr_frame1, #mr_frame2, #mr_frame3, #mr_frame4, #mr_frame5,\n"
"#mr_frame1_a_label1, #mr_frame1_c_label2,\n"
"#mr_frame2_a_label1, #mr_frame2_c_label2,\n"
"#mr_frame3_a_label1, #mr_frame3_c_label2,\n"
"#mr_frame4_a_label1, #mr_frame4_c_label2,\n"
"#mr_frame5_a_label1, #mr_frame5_c_label2,\n"
"#program_name {\n"
"    background-color: rgba(0, 0, 0, 70);\n"
"    border: none;\n"
"}\n"
"\n"
"/* ProgressBars: styled separately, without opaque background */\n"
"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: rgba(255, 255, 255, 40); /* subtle background */\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 6px;\n"
"    background-color: rgba(0, 181, 204, 1); /* blue fill */\n"
"}")
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
        self.brand_logo.setPixmap(QPixmap(u":/images/full_logo_nobg.png"))
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
        self.ml_label1A.setPixmap(QPixmap(u":/icons/device_thermostat.svg"))

        self.horizontalLayout_2.addWidget(self.ml_label1A, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label2A = QLabel(self.ml_frameA)
        self.ml_label2A.setObjectName(u"ml_label2A")

        self.horizontalLayout_2.addWidget(self.ml_label2A, 0, Qt.AlignmentFlag.AlignLeft)

        self.ml_label3A = QLabel(self.ml_frameA)
        self.ml_label3A.setObjectName(u"ml_label3A")

        self.horizontalLayout_2.addWidget(self.ml_label3A)


        self.verticalLayout_3.addWidget(self.ml_frameA, 0, Qt.AlignmentFlag.AlignTop)

        self.ml_frameC = QFrame(self.ml_frame1)
        self.ml_frameC.setObjectName(u"ml_frameC")
        self.ml_frameC.setFrameShape(QFrame.Shape.StyledPanel)
        self.ml_frameC.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ml_frameC)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ml_label1C = QLabel(self.ml_frameC)
        self.ml_label1C.setObjectName(u"ml_label1C")
        self.ml_label1C.setPixmap(QPixmap(u":/icons/humidity.svg"))

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
        self.device_image.setMaximumSize(QSize(650, 16777215))
        self.device_image.setPixmap(QPixmap(u":/images/telescope2nobg.png"))
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
        self.mb_frame2_content = QFrame(self.mb_frame2)
        self.mb_frame2_content.setObjectName(u"mb_frame2_content")
        self.mb_frame2_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2_content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.mb_frame2_content)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.mb_frame2_content)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.Shape.HLine)
        self.scroll_area.setLineWidth(0)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setObjectName(u"scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 567, 143))
        self.horizontalLayout_8 = QHBoxLayout(self.scroll_area_widget_contents)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mb_frame2A = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2A.setObjectName(u"mb_frame2A")
        self.mb_frame2A.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2A.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.mb_frame2A)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.A1_label = QLabel(self.mb_frame2A)
        self.A1_label.setObjectName(u"A1_label")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(11)
        self.A1_label.setFont(font1)
        self.A1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.A1_label)

        self.A2_pushbutton = QPushButton(self.mb_frame2A)
        self.A2_pushbutton.setObjectName(u"A2_pushbutton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.A2_pushbutton.setIcon(icon2)
        self.A2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_24.addWidget(self.A2_pushbutton)

        self.A3_label = QLabel(self.mb_frame2A)
        self.A3_label.setObjectName(u"A3_label")
        self.A3_label.setFont(font1)
        self.A3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.A3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2A)

        self.mb_frame2B = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2B.setObjectName(u"mb_frame2B")
        self.mb_frame2B.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2B.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.mb_frame2B)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.B1_label = QLabel(self.mb_frame2B)
        self.B1_label.setObjectName(u"B1_label")
        self.B1_label.setFont(font1)
        self.B1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.B1_label)

        self.B2_pushbutton = QPushButton(self.mb_frame2B)
        self.B2_pushbutton.setObjectName(u"B2_pushbutton")
        self.B2_pushbutton.setIcon(icon2)
        self.B2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_15.addWidget(self.B2_pushbutton)

        self.B3_label = QLabel(self.mb_frame2B)
        self.B3_label.setObjectName(u"B3_label")
        self.B3_label.setFont(font1)
        self.B3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.B3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2B)

        self.mb_frame2C = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2C.setObjectName(u"mb_frame2C")
        self.mb_frame2C.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2C.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.mb_frame2C)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.C1_label = QLabel(self.mb_frame2C)
        self.C1_label.setObjectName(u"C1_label")
        self.C1_label.setFont(font1)
        self.C1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.C1_label)

        self.C2_pushbutton = QPushButton(self.mb_frame2C)
        self.C2_pushbutton.setObjectName(u"C2_pushbutton")
        self.C2_pushbutton.setIcon(icon2)
        self.C2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_14.addWidget(self.C2_pushbutton)

        self.C3_label = QLabel(self.mb_frame2C)
        self.C3_label.setObjectName(u"C3_label")
        self.C3_label.setFont(font1)
        self.C3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.C3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2C)

        self.mb_frame2D = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2D.setObjectName(u"mb_frame2D")
        self.mb_frame2D.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2D.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mb_frame2D)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.D1_label = QLabel(self.mb_frame2D)
        self.D1_label.setObjectName(u"D1_label")
        self.D1_label.setFont(font1)
        self.D1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.D1_label)

        self.D2_pushbutton = QPushButton(self.mb_frame2D)
        self.D2_pushbutton.setObjectName(u"D2_pushbutton")
        self.D2_pushbutton.setIcon(icon2)
        self.D2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_7.addWidget(self.D2_pushbutton)

        self.D3_label = QLabel(self.mb_frame2D)
        self.D3_label.setObjectName(u"D3_label")
        self.D3_label.setFont(font1)
        self.D3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.D3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2D)

        self.mb_frame2E = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2E.setObjectName(u"mb_frame2E")
        self.mb_frame2E.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2E.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.mb_frame2E)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.E1_label = QLabel(self.mb_frame2E)
        self.E1_label.setObjectName(u"E1_label")
        self.E1_label.setFont(font1)
        self.E1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.E1_label)

        self.E2_pushbutton = QPushButton(self.mb_frame2E)
        self.E2_pushbutton.setObjectName(u"E2_pushbutton")
        self.E2_pushbutton.setIcon(icon2)
        self.E2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_26.addWidget(self.E2_pushbutton)

        self.E3_label = QLabel(self.mb_frame2E)
        self.E3_label.setObjectName(u"E3_label")
        self.E3_label.setFont(font1)
        self.E3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.E3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2E)

        self.mb_frame2F = QFrame(self.scroll_area_widget_contents)
        self.mb_frame2F.setObjectName(u"mb_frame2F")
        self.mb_frame2F.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame2F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.mb_frame2F)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.F1_label = QLabel(self.mb_frame2F)
        self.F1_label.setObjectName(u"F1_label")
        self.F1_label.setFont(font1)
        self.F1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.F1_label)

        self.F2_pushbutton = QPushButton(self.mb_frame2F)
        self.F2_pushbutton.setObjectName(u"F2_pushbutton")
        self.F2_pushbutton.setIcon(icon2)
        self.F2_pushbutton.setIconSize(QSize(64, 64))

        self.verticalLayout_25.addWidget(self.F2_pushbutton)

        self.F3_label = QLabel(self.mb_frame2F)
        self.F3_label.setObjectName(u"F3_label")
        self.F3_label.setFont(font1)
        self.F3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.F3_label)


        self.horizontalLayout_8.addWidget(self.mb_frame2F)

        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        self.horizontalLayout_11.addWidget(self.scroll_area)


        self.horizontalLayout_7.addWidget(self.mb_frame2_content)


        self.verticalLayout_5.addWidget(self.mb_frame2)

        self.mb_frame3 = QFrame(self.mb_content)
        self.mb_frame3.setObjectName(u"mb_frame3")
        self.mb_frame3.setMinimumSize(QSize(0, 125))
        self.mb_frame3.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.mb_frame3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.mb_frame3A = QFrame(self.mb_frame3)
        self.mb_frame3A.setObjectName(u"mb_frame3A")
        self.mb_frame3A.setMinimumSize(QSize(0, 0))
        self.mb_frame3A.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame3A.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.mb_frame3A)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.A1_pushButton = QPushButton(self.mb_frame3A)
        self.A1_pushButton.setObjectName(u"A1_pushButton")
        self.A1_pushButton.setMinimumSize(QSize(0, 0))
        self.A1_pushButton.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/log_monitor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.A1_pushButton.setIcon(icon3)
        self.A1_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_27.addWidget(self.A1_pushButton)

        self.A2_label = QLabel(self.mb_frame3A)
        self.A2_label.setObjectName(u"A2_label")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.A2_label.setFont(font2)
        self.A2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.A2_label)


        self.horizontalLayout_6.addWidget(self.mb_frame3A)

        self.mb_frame3B = QFrame(self.mb_frame3)
        self.mb_frame3B.setObjectName(u"mb_frame3B")
        self.mb_frame3B.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame3B.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.mb_frame3B)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.B1_pushButton = QPushButton(self.mb_frame3B)
        self.B1_pushButton.setObjectName(u"B1_pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/folder_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.B1_pushButton.setIcon(icon4)
        self.B1_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_30.addWidget(self.B1_pushButton)

        self.B2_label = QLabel(self.mb_frame3B)
        self.B2_label.setObjectName(u"B2_label")
        self.B2_label.setFont(font2)
        self.B2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.B2_label)


        self.horizontalLayout_6.addWidget(self.mb_frame3B)

        self.mb_frame3C = QFrame(self.mb_frame3)
        self.mb_frame3C.setObjectName(u"mb_frame3C")
        self.mb_frame3C.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame3C.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.mb_frame3C)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.C1_pushButton = QPushButton(self.mb_frame3C)
        self.C1_pushButton.setObjectName(u"C1_pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/apps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.C1_pushButton.setIcon(icon5)
        self.C1_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_29.addWidget(self.C1_pushButton)

        self.C2_label = QLabel(self.mb_frame3C)
        self.C2_label.setObjectName(u"C2_label")
        self.C2_label.setFont(font2)
        self.C2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.C2_label)


        self.horizontalLayout_6.addWidget(self.mb_frame3C)

        self.mb_frame3D = QFrame(self.mb_frame3)
        self.mb_frame3D.setObjectName(u"mb_frame3D")
        self.mb_frame3D.setFrameShape(QFrame.Shape.StyledPanel)
        self.mb_frame3D.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.mb_frame3D)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.D1_pushButton = QPushButton(self.mb_frame3D)
        self.D1_pushButton.setObjectName(u"D1_pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.D1_pushButton.setIcon(icon6)
        self.D1_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_28.addWidget(self.D1_pushButton)

        self.D2_label = QLabel(self.mb_frame3D)
        self.D2_label.setObjectName(u"D2_label")
        self.D2_label.setFont(font2)
        self.D2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.D2_label)


        self.horizontalLayout_6.addWidget(self.mb_frame3D)


        self.verticalLayout_5.addWidget(self.mb_frame3)


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
        self.verticalLayout_4 = QVBoxLayout(self.mr_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mr_frame1 = QFrame(self.mr_content)
        self.mr_frame1.setObjectName(u"mr_frame1")
        self.mr_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.mr_frame1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.mr_frame1_a_label1 = QLabel(self.mr_frame1)
        self.mr_frame1_a_label1.setObjectName(u"mr_frame1_a_label1")
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.mr_frame1_a_label1.setFont(font3)
        self.mr_frame1_a_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.mr_frame1_a_label1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame1_b_progress_bar = QProgressBar(self.mr_frame1)
        self.mr_frame1_b_progress_bar.setObjectName(u"mr_frame1_b_progress_bar")
        self.mr_frame1_b_progress_bar.setFont(font1)
        self.mr_frame1_b_progress_bar.setValue(90)

        self.verticalLayout_16.addWidget(self.mr_frame1_b_progress_bar, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame1_c_label2 = QLabel(self.mr_frame1)
        self.mr_frame1_c_label2.setObjectName(u"mr_frame1_c_label2")
        self.mr_frame1_c_label2.setFont(font1)

        self.verticalLayout_16.addWidget(self.mr_frame1_c_label2)


        self.verticalLayout_4.addWidget(self.mr_frame1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame2 = QFrame(self.mr_content)
        self.mr_frame2.setObjectName(u"mr_frame2")
        self.mr_frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.mr_frame2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.mr_frame2_a_label1 = QLabel(self.mr_frame2)
        self.mr_frame2_a_label1.setObjectName(u"mr_frame2_a_label1")
        self.mr_frame2_a_label1.setFont(font1)
        self.mr_frame2_a_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.mr_frame2_a_label1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame2_b_progress_bar = QProgressBar(self.mr_frame2)
        self.mr_frame2_b_progress_bar.setObjectName(u"mr_frame2_b_progress_bar")
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setKerning(True)
        self.mr_frame2_b_progress_bar.setFont(font4)
        self.mr_frame2_b_progress_bar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mr_frame2_b_progress_bar.setValue(90)
        self.mr_frame2_b_progress_bar.setOrientation(Qt.Orientation.Horizontal)
        self.mr_frame2_b_progress_bar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_18.addWidget(self.mr_frame2_b_progress_bar, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame2_c_label2 = QLabel(self.mr_frame2)
        self.mr_frame2_c_label2.setObjectName(u"mr_frame2_c_label2")
        self.mr_frame2_c_label2.setFont(font3)

        self.verticalLayout_18.addWidget(self.mr_frame2_c_label2)


        self.verticalLayout_4.addWidget(self.mr_frame2, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame3 = QFrame(self.mr_content)
        self.mr_frame3.setObjectName(u"mr_frame3")
        self.mr_frame3.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.mr_frame3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.mr_frame3_a_label1 = QLabel(self.mr_frame3)
        self.mr_frame3_a_label1.setObjectName(u"mr_frame3_a_label1")
        self.mr_frame3_a_label1.setFont(font1)
        self.mr_frame3_a_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.mr_frame3_a_label1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame3_b_progress_bar = QProgressBar(self.mr_frame3)
        self.mr_frame3_b_progress_bar.setObjectName(u"mr_frame3_b_progress_bar")
        self.mr_frame3_b_progress_bar.setFont(font1)
        self.mr_frame3_b_progress_bar.setValue(90)

        self.verticalLayout_19.addWidget(self.mr_frame3_b_progress_bar, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame3_c_label2 = QLabel(self.mr_frame3)
        self.mr_frame3_c_label2.setObjectName(u"mr_frame3_c_label2")
        self.mr_frame3_c_label2.setFont(font1)

        self.verticalLayout_19.addWidget(self.mr_frame3_c_label2)


        self.verticalLayout_4.addWidget(self.mr_frame3, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame4 = QFrame(self.mr_content)
        self.mr_frame4.setObjectName(u"mr_frame4")
        self.mr_frame4.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.mr_frame4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.mr_frame4_a_label1 = QLabel(self.mr_frame4)
        self.mr_frame4_a_label1.setObjectName(u"mr_frame4_a_label1")
        self.mr_frame4_a_label1.setFont(font1)
        self.mr_frame4_a_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.mr_frame4_a_label1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame4_b_progress_bar = QProgressBar(self.mr_frame4)
        self.mr_frame4_b_progress_bar.setObjectName(u"mr_frame4_b_progress_bar")
        self.mr_frame4_b_progress_bar.setFont(font1)
        self.mr_frame4_b_progress_bar.setValue(90)

        self.verticalLayout_17.addWidget(self.mr_frame4_b_progress_bar, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame4_c_label2 = QLabel(self.mr_frame4)
        self.mr_frame4_c_label2.setObjectName(u"mr_frame4_c_label2")
        font5 = QFont()
        font5.setFamilies([u"Yu Gothic"])
        self.mr_frame4_c_label2.setFont(font5)

        self.verticalLayout_17.addWidget(self.mr_frame4_c_label2)


        self.verticalLayout_4.addWidget(self.mr_frame4, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame5 = QFrame(self.mr_content)
        self.mr_frame5.setObjectName(u"mr_frame5")
        self.mr_frame5.setFrameShape(QFrame.Shape.StyledPanel)
        self.mr_frame5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.mr_frame5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.mr_frame5_a_label1 = QLabel(self.mr_frame5)
        self.mr_frame5_a_label1.setObjectName(u"mr_frame5_a_label1")
        self.mr_frame5_a_label1.setFont(font1)
        self.mr_frame5_a_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.mr_frame5_a_label1, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame5_b_progress_bar = QProgressBar(self.mr_frame5)
        self.mr_frame5_b_progress_bar.setObjectName(u"mr_frame5_b_progress_bar")
        self.mr_frame5_b_progress_bar.setFont(font1)
        self.mr_frame5_b_progress_bar.setValue(90)

        self.verticalLayout_20.addWidget(self.mr_frame5_b_progress_bar, 0, Qt.AlignmentFlag.AlignTop)

        self.mr_frame5_c_label2 = QLabel(self.mr_frame5)
        self.mr_frame5_c_label2.setObjectName(u"mr_frame5_c_label2")
        self.mr_frame5_c_label2.setFont(font1)

        self.verticalLayout_20.addWidget(self.mr_frame5_c_label2)


        self.verticalLayout_4.addWidget(self.mr_frame5, 0, Qt.AlignmentFlag.AlignTop)

        self.program_name = QLabel(self.mr_content)
        self.program_name.setObjectName(u"program_name")
        self.program_name.setMinimumSize(QSize(0, 0))
        self.program_name.setMaximumSize(QSize(16777215, 25))
        self.program_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.program_name)


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
        self.ml_label1C.setText("")
        self.ml_label2C.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.ml_label3C.setText(QCoreApplication.translate("MainWindow", u"...%", None))
        self.ml_button1.setText(QCoreApplication.translate("MainWindow", u" Control Panel", None))
        self.device_image.setText("")
        self.A1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.A2_pushbutton.setText("")
        self.A3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.B1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.B2_pushbutton.setText("")
        self.B3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.C1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.C2_pushbutton.setText("")
        self.C3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.D1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.D2_pushbutton.setText("")
        self.D3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.E1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.E2_pushbutton.setText("")
        self.E3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.F1_label.setText(QCoreApplication.translate("MainWindow", u"Port #", None))
        self.F2_pushbutton.setText("")
        self.F3_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.A1_pushButton.setText("")
        self.A2_label.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.B1_pushButton.setText("")
        self.B2_label.setText(QCoreApplication.translate("MainWindow", u"File Explorer", None))
        self.C1_pushButton.setText("")
        self.C2_label.setText(QCoreApplication.translate("MainWindow", u"Desktop Apps", None))
        self.D1_pushButton.setText("")
        self.D2_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.mr_frame1_a_label1.setText(QCoreApplication.translate("MainWindow", u"Total Power Consumption", None))
        self.mr_frame1_c_label2.setText(QCoreApplication.translate("MainWindow", u"... W", None))
        self.mr_frame2_a_label1.setText(QCoreApplication.translate("MainWindow", u"Port 1 Power", None))
        self.mr_frame2_c_label2.setText(QCoreApplication.translate("MainWindow", u"... W", None))
        self.mr_frame3_a_label1.setText(QCoreApplication.translate("MainWindow", u"Port 2 Power", None))
        self.mr_frame3_c_label2.setText(QCoreApplication.translate("MainWindow", u"... W", None))
        self.mr_frame4_a_label1.setText(QCoreApplication.translate("MainWindow", u"Port 3 Power", None))
        self.mr_frame4_c_label2.setText(QCoreApplication.translate("MainWindow", u"... W", None))
        self.mr_frame5_a_label1.setText(QCoreApplication.translate("MainWindow", u"Port 4 Power", None))
        self.mr_frame5_c_label2.setText(QCoreApplication.translate("MainWindow", u"... W", None))
        self.program_name.setText(QCoreApplication.translate("MainWindow", u"CaeBell\u00ae", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

