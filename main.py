from PyQt5 import QtCore, QtGui, QtWidgets

String = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]()<>/!@#$^&_-=+* '

R1 = '[ZuO(/#azs_hiTe]X<vrM)!SAQ^y6I3kFmU$EYj*N> 2l7t&1BR9fgw@5VDJn-K4L8Cq=oGbxpdcHP0W+'
R2 = 'TMkJXwIZlh5)Wj=uB_sLo1@f*FDHS4Ctr&Q-2RAd0KqmcV>8!GNzaU(/x[ep9+ n6PvYOyb]i3g$<7#E^'
R3 = 'XoQ9*SDr_1]JGdgZi0w>OheMRq@E2lmzpxv#f7VF4!cLYj38[W($CA5-^sPI+/a)HNKky<6BbnUut =&T'
R4 = '<4K=f)a(jkCTIHn-g3ov8lqbPXVzNOLc/FmruYJ!yZ[s6d1p25*tB&h]GR_D$9i^>@70 WxQ#wAUS+EeM'
R5 = '<4K=f)a(jkCTIHn-g3ov8lqbPXVzNOLc/FmruYJ!yZ[s6d1p25*tB&h]GR_D$9i^>@70 WxQ#wAUS+EeM'

# String='ظطزرذدپو./گکمنتالبیسشضصثقفغع هخحجچ'
# r11 = 'ضصشسظطثقیبزرفغلاذدعهتنپوخحمک./جچ گ'
# r22 = 'چجحخهعغفقثصضشسیبلاتنمکگ/.وپدذ رزطظ'
# r33 = 'گکمنتالبیسشضصثقفغعدذرزطظپهوخ. ح/جچ'

print(len(String))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(580)
        MainWindow.setFixedHeight(300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 580, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 580, 270))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.convert)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        

    state = 0

    def encrypt(self,c):
        c1 = r1[String.find(c)]
        c2 = r2[String.find(c1)]
        c3 = r3[String.find(c2)]
        c4 = r4[String.find(c3)]
        c5 = r5[String.find(c5)]
        reflected = String[81-String.find(c5)]
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

    def convert(self):
        self.reset()
        plain = self.plainTextEdit.toPlainText()
        cipher = ''
        for c in plain:
            self.state += 1
            cipher += self.encrypt(c)
            self.rotate()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(cipher)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enigma"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", " text"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())