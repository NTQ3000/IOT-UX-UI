# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testtoggle.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(220, 240, 61, 31))
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    width:50px;\n"
"    height:50px;\n"
"    image: url(:/toggle/left.png)\n"
"}")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 190, 121, 91))
        self.label.setStyleSheet("image: url(:/ac/ac_off.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.checkBox.clicked.connect(self.toggle)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def toggle(self):
        if self.checkBox.isChecked():
            self.label.setStyleSheet("image: url(:/ac/ac_on.png);")
            self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    width:50px;\n"
"    height:50px;\n"
"    image: url(:/toggle/right.png)\n"
"}")
        elif (self.checkBox.isChecked()==False):
            self.label.setStyleSheet("image: url(:/ac/ac_off.png);")
            self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    width:50px;\n"
"    height:50px;\n"
"    image: url(:/toggle/left.png)\n"
"}")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
