from PyQt5 import QtCore, QtGui, QtWidgets
from time import localtime

# year , month , day , hour
y = int(str(localtime()[0])[2:]) 
m = localtime()[1]
d = localtime()[2]
h = localtime()[3]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(465)
        MainWindow.setFixedHeight(273)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plainText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainText.setGeometry(QtCore.QRect(2, 30, 461, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainText.setFont(font)
        self.plainText.setObjectName("plainText")

        self.change_language = QtWidgets.QPushButton(self.centralwidget)
        self.change_language.setGeometry(QtCore.QRect(2, 0, 187, 28))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.change_language.setFont(font)
        self.change_language.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_language.setObjectName("change_language")

        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(282, 0, 181, 28))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert.setObjectName("convert")

        self.language = QtWidgets.QLabel(self.centralwidget)
        self.language.setGeometry(QtCore.QRect(202, 0, 71, 31))
        font.setPointSize(12)
        self.language.setFont(font)
        self.language.setAlignment(QtCore.Qt.AlignCenter)
        self.language.setObjectName("language")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.convert.clicked.connect(self.convert_f)
        self.change_language.clicked.connect(self.change_language_f)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    start_line = 0
    state = 0
    eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    fa = "ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو۱۲۳۴۵۶۷۸۹۰0123456789 "



    def change_language_f(self):
        global h , d , m , y
        if self.start_line==180:
            self.language.setText('English')
            self.start_line=0
        else :
            self.language.setText('Persian')
            self.start_line=180
        y = int(str(localtime()[0])[2:]) 
        m = localtime()[1]
        d = localtime()[2]
        h = localtime()[3]
        self.set_rotors(self.start_line)



    def set_rotors(self,start):
        global R1 , R2 , R3 , R4 , R5
        try :
            f = open('./rotors','r')
        except :
            f = open(r'.\rotors','r')
        file = f.readlines()
        R1 = file[start + m*m + h].replace('\n', '')
        R2 = file[start + m*m + d].replace('\n', '')
        R3 = file[start + m*m + m].replace('\n', '')
        R4 = file[start + m*m + m + h].replace('\n', '')
        R5 = file[start + y + 2*m + d + h].replace('\n', '')
        f.close()



    def encrypt(self,c,String,length):
        c1 = r1[String.find(c)]
        c2 = r2[String.find(c1)]
        c3 = r3[String.find(c2)]
        c4 = r4[String.find(c3)]
        c5 = r5[String.find(c4)]
        reflected = String[length-String.find(c5)]
        c5 = String[r5.find(reflected)]
        c4 = String[r4.find(c5)]
        c3 = String[r3.find(c4)]
        c2 = String[r2.find(c3)]
        c1 = String[r1.find(c2)]
        return c1



    def rotate(self):
        global r1 , r2 , r3 , r4 , r5
        r1 = r1[1:] + r1[0]
        if self.state % 15 :
            r2 = r2[1:] + r2[0]
        if self.state % 50 :
            r3 = r3[1:] + r3[0]
        if self.state % 200 :
            r4 = r4[1:] + r4[0]
        if self.state % 500 :
            r5 = r5[1:] + r5[0]



    def reset(self):
        global r1 , r2 , r3 , r4 , r5
        r1 , r2 , r3 , r4 , r5 = R1 , R2 , R3 , R4 , R5
        self.state = 0



    def convert_f(self):
        self.reset()
        plain = self.plainText.toPlainText()
        cipher = ''
        for c in plain:
            self.state += 1
            if self.start_line==0:
                cipher += self.encrypt(c,self.eng,61)
            else:
                cipher += self.encrypt(c,self.fa,50)
            self.rotate()
        self.plainText.clear()
        self.plainText.appendPlainText(cipher)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enigma"))
        self.plainText.setPlainText(_translate("MainWindow", ""))
        self.plainText.setPlaceholderText(_translate("MainWindow", " text"))
        self.change_language.setText(_translate("MainWindow", "Change language"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.language.setText(_translate("MainWindow", "English"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.change_language_f()
    MainWindow.show()
    sys.exit(app.exec_())