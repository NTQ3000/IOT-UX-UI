# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_mo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mo.setGeometry(QtCore.QRect(390, 460, 93, 28))
        self.btn_mo.setObjectName("btn_mo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 40, 151, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.xoa = QtWidgets.QPushButton(self.centralwidget)
        self.xoa.setGeometry(QtCore.QRect(60, 460, 93, 28))
        self.xoa.setObjectName("xoa")
        self.thoat = QtWidgets.QPushButton(self.centralwidget)
        self.thoat.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.thoat.setObjectName("thoat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_mo.clicked.connect(self.show_diagram)
        self.thoat.clicked.connect(QtWidgets.QApplication.quit)
        self.xoa.clicked.connect(self.clear_diagram)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_mo.setText(_translate("MainWindow", "open"))
        self.xoa.setText(_translate("MainWindow", "clear"))
        self.thoat.setText(_translate("MainWindow", "exit"))
    def show_diagram(self):
        thang = [1, 2 , 3, 4, 5]
        tien = [200, 400, 124, 600, 879]
        fig, ax = plt.subplots(figsize=(1.51, 1.31))
        ax.plot(thang, tien)
        ax.set_xlabel('Tháng')
        ax.set_ylabel('Tiền')
        ax.set_title('Biểu đồ tiền điện theo tháng')
        canvas = FigureCanvas(fig)
        self.verticalLayout.addWidget(canvas)
    def clear_diagram(self):
        # Xóa tất cả widget trong layout
        for i in reversed(range(self.verticalLayout.count())):
            widget = self.verticalLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
