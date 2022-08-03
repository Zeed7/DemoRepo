import csv
import os
from Haykal import doMagic
from styling import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit, QFileDialog, QDialog,
    QMainWindow, QPushButton, QCheckBox,
    QWidget)
import sys
from time import sleep



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        

        self.setFixedSize(QSize(394, 626))
        self.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setGeometry(QRect(40, 170, 311, 351))
        self.mainframe.setStyleSheet(st_mainframe)
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.ed_host = QLineEdit(self.mainframe)
        self.ed_host.setObjectName(u"ed_host")
        self.ed_host.setGeometry(QRect(20, 40, 271, 31))
        self.ed_host.setStyleSheet(st_lineEdit)

        self.label = QLabel(self.mainframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(29, 20, 111, 20))
        self.label.setStyleSheet(u"font: 11pt \"Segoe UI\";\n"
        "border: 0px solid #000000;")
        self.label_2 = QLabel(self.mainframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(29, 80, 111, 20))
        self.label_2.setStyleSheet(u"\n"
        "border: 0px solid #000000;\n"
        "font: 11pt \"Segoe UI\";")
        
        self.ed_user = QLineEdit(self.mainframe)
        self.ed_user.setObjectName(u"ed_user")
        self.ed_user.setGeometry(QRect(20, 100, 271, 31))
        self.ed_user.setStyleSheet(st_lineEdit)

        self.label_3 = QLabel(self.mainframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(28, 140, 111, 20))
        self.label_3.setStyleSheet(u"\n"
        "border: 0px solid #000000;\n"
        "font: 11pt \"Segoe UI\";")
        self.ed_password = QLineEdit(self.mainframe)
        self.ed_password.setObjectName(u"ed_password")
        self.ed_password.setGeometry(QRect(19, 160, 271, 31))
        self.ed_password.setStyleSheet(st_lineEdit)
        self.ed_password.setEchoMode(QLineEdit.Password)
        
        self.box_multi = QCheckBox(self.mainframe)
        self.box_multi.setGeometry(QRect(100, 195, 100, 30))
        self.box_multi.setText("multiple files")
        self.box_multi.setEnabled(False)

        self.lbl_csv_name = QLabel(self.mainframe)
        self.lbl_csv_name.setObjectName(u"lbl_csv_name")
        self.lbl_csv_name.setGeometry(QRect(10, 220, 300, 30))
        self.lbl_csv_name.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
        "border: 0px solid #000000;")
        self.lbl_csv_name.setAlignment(Qt.AlignCenter)
        self.btn_browse = QPushButton(self.mainframe)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setGeometry(QRect(80, 240, 141, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.btn_browse.setFont(font)
        self.btn_browse.setStyleSheet(st_btn_browse)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setKerning(True)

        self.btn_browse.setFont(font2)
        self.btn_browse.setCheckable(True)
        
        self.btn_create_btn = QPushButton(self.mainframe)
        self.btn_create_btn.setObjectName(u"btn_create_btn")
        self.btn_create_btn.setGeometry(QRect(80, 290, 141, 41))
        
        self.btn_create_btn.setFont(font2)
        self.btn_create_btn.setStyleSheet(st_btn_start)
        self.btn_create_btn.setEnabled(False)
        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setGeometry(QRect(40, 540, 315, 30))
        
        self.lbl_result.setAlignment(Qt.AlignCenter)
        
        self.lbl_result_e = QLabel(self.centralwidget)
        self.lbl_result_e.setObjectName(u"lbl_result")
        self.lbl_result_e.setGeometry(QRect(40, 560, 315, 40))
        self.lbl_result_e.setAlignment(Qt.AlignCenter)

        '''
        self.frame_image = QFrame(self.centralwidget)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setGeometry(QRect(130, 40, 131, 121))
        self.frame_image.setStyleSheet(u"background-color: rgb(139, 139, 139);\n"
        "border-radius: 50px;"
        )
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)

        self.imagelbl = QLabel(self.centralwidget)
        self.image = QPixmap("pic.png")
        self.imagelbl.setPixmap(self.image)
        self.imagelbl.setScaledContents(True)
        self.imagelbl.setGeometry(QRect(130, 40, 131, 121))
        '''

        self.titlea = QLabel(self.centralwidget)
        self.titlea.setText("CSV to MySQL")
        self.titlea.setGeometry(QRect(100, 40, 200, 121))
        self.titlea.setStyleSheet(u"border-radius: 50px;")

        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setKerning(True)
        

        self.titlea.setFont(font3)
        self.titlea.setAlignment(Qt.AlignCenter)

        # texts
        
        self.btn_browse.clicked.connect(self.browseCSV)
        self.label.setText("Host")
        self.label_2.setText("Username")
        self.label_3.setText("Password")
        self.lbl_csv_name.setText("")
        self.btn_browse.setText("browse")
        self.btn_create_btn.setText("Start")
        self.lbl_result.setText("")
        self.btn_create_btn.clicked.connect(self.startCreating)
        self.setCentralWidget(self.centralwidget)

        # FOR NOW
        self.ed_host.setText("localhost")
        self.ed_user.setText("root")
        self.ed_password.setText("Zakaria1551ZikoX*")

    # FUCNTIONING 
    def browseCSV(self):
        with open("D:\\60 DAYS\\MySQL Python\\CSV TO SQL\\a.txt", 'r') as f:
            lastpath = f.read().strip()

        filepath = QFileDialog.getOpenFileName(self, 'open file', lastpath, 'CSV files (*.csv)')
        self.csv_path = filepath[0]

        self.csv_name = str(os.path.basename(self.csv_path)).strip()
        self.lbl_csv_name.setText(self.csv_name)


        with open("D:\\60 DAYS\\MySQL Python\\CSV TO SQL\\a.txt", 'w') as f:
            f.write(self.csv_path)
        
        self.btn_create_btn.setEnabled(True)
        
    def startCreating(self):
        with open(self.csv_path) as csvf:
            data = list(csv.reader(csvf, delimiter=','))
        
        user = self.ed_user.text()
        password = self.ed_password.text()
        host = self.ed_host.text()

        isDone = doMagic(self.csv_name, data, host, user, password)
        if isDone == 1:
            
            self.lbl_result.setStyleSheet(u"font: 11pt \"Segoe UI\";"
            "color: #0C8323;")
            self.lbl_result.setText("Database was created successfully")
        else:
            self.lbl_result.setText("ERROR FOUND\n")
            self.lbl_result_e.setText(str(isDone[1]))
            self.lbl_result.setStyleSheet(u"font: 11pt \"Segoe UI\";"
            "color: #FB3F3F;")
            self.lbl_result_e.setStyleSheet(u"font: 8pt \"Segoe UI\";"
            "color: #FB3F3F;")
            self.lbl_result_e.setWordWrap(True)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()
