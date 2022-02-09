# quintofsteel/typing-speed-test

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 556)
        MainWindow.setMinimumSize(QtCore.QSize(800, 556))
        MainWindow.setMaximumSize(QtCore.QSize(800, 556))
        MainWindow.setBaseSize(QtCore.QSize(800, 556))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(143, 197, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 371, 61))
        font = QtGui.QFont()
        font.setFamily("MathJax_Caligraphic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(85, 0, 127)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(329, 372, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(146, 159, 171);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 270, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 90, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 120, 701, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(70, 104, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.textBrowser.raise_()
        self.frame.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        global inputText, t0, t1, phrase, lengthOfInput, timeTaken, accuracy, wordsperminute
        inputText = self.lineEdit.text()

        if self.pushButton.clicked:
            t0 = time.time()
        if self.lineEdit.returnPressed:
            inputText = self.lineEdit.text()

    def test(self):
        phrase = "Full fathom five thy father lies, of his bones are coral made. Those are pearls that were his eyes. Nothing of him that doth fade, but doth suffer a sea-change into something rich and strange"
        word_count = len(phrase.split())
        #t0 = time.time()
        inputText = self.lineEdit.text()
        t1 = time.time()
        lengthOfInput = len(inputText.split())
        accuracy = len(set(inputText.split()) & set(phrase.split()))
        accuracy = (accuracy / word_count)
        timeTaken = (t1 - t0)
        wordsperminute = (lengthOfInput / timeTaken) * 60

        def show_results():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Total words \t : {lengthOfInput}"
                        f"\nTime used \t\t : {round(timeTaken, 2)} seconds"
                        f"\nYour accuracy \t : {round(accuracy, 3) * 100} %"
                        f"\nSpeed is \t\t : {round(wordsperminute, 2)} words per minute")

            msg.setWindowTitle("Test Results")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

        show_results()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Speed Test"))
        self.label.setText(_translate("MainWindow", "Typing Speed Test"))
        self.pushButton.setText(_translate("MainWindow", "Results"))
        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter the text above with accuracy, Press Enter when you are done."))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Full fathom five thy father lies, of his bones are coral made. Those are pearls that were his eyes. Nothing of him that doth fade, but doth suffer a sea-change into something rich and strange</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
