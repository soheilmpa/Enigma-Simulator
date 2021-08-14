from PyQt5 import QtCore, QtGui, QtWidgets

String = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}[]()<>/\!@#$%^&_-=+* '

r1 = r'okE(5PW{!wn^3 L/Gi2m]081h=CdA\JQ+eF%Bt9&UxYl6>c-uZs)fr#ypNSgOX7V$IK@M*Tz_4aHD[<Rjqb}v'
r2 = r'nI 9b1{ChxmOjDSWBJy<7Q6#@cs3V>dlt*80zeuk[]H4)PKRgNM&o_G2va!(pY+T/A$qXf=^%i\E-}5LUZrFw'
r3 = r'aG(m\UMIqS*t9]0 h$AF%ONR2D_1vd5[^VieP)f8Hw3o/CzKZ-}EL={sQWJr6!7kTpu@ncgx+#jBlYyX><b4&'
r4 = r'1>)ocE#/TZJOi+*db}mhn@U2ws=y4^GjWp!BFYSfP&H6k<V{_5RKAx% rgMI-9$eX\utz(lCv[L73NQ0q8aD]'
r5 = r'L2ap/nk$q<^7XKlGUYWr@o{\He+Owx>Iz#Mf-0]Z&usEdP3NB9J)mtVjc_[6* !b1RyT%QihACF=(Dgv54S}8'


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
        c5 = r5[String.find(c4)]
        reflected = String[85-String.find(c5)]
        c5 = String[r5.find(reflected)]
        c4 = String[r4.find(c5)]
        c3 = String[r3.find(c4)]
        c2 = String[r2.find(c3)]
        c1 = String[r1.find(c2)]
        return c1

    def rotate(self):
        pass

    def convert(self):
        cipher = ''
        plain = self.plainTextEdit.toPlainText()
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