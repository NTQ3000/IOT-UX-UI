
from PyQt5 import QtCore, QtGui, QtWidgets
import image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pyrebase
 ####### ####### ####### ####### ####### ####### ####### ####### #######
firebaseConfig = {
  'apiKey': "AIzaSyAI8YUuPTR-_b6nfwt8_dRu3WO66QewiBc",
  'authDomain': "iot1-a2347.firebaseapp.com",
  'databaseURL': "https://nhet-9909b-default-rtdb.firebaseio.com",
  'projectId': "iot1-a2347",
  'storageBucket': "iot1-a2347.appspot.com",
  'messagingSenderId': "812756037992",
  'appId': "1:812756037992:web:61471e9d7530c6a56fa6dd",
  'measurementId': "G-S3F707CFML"
};
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
doam=db.child("doam").get().val()
nhietdo=db.child("nhietdo").get().val()
 ####### ####### ####### ####### ####### ####### ####### ####### #######
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QCheckBox::indicator {\n"
                "    width: 50px;\n"
                "    height: 50px;\n"
                "}\n"
                "\n"
                "QCheckBox::indicator:checked {\n"
                "    background-image: url(:/toggle/right.png);\n"
                "}\n"           
                "\n"
                "QCheckBox::indicator:unchecked {\n"
                "    background-image: url(:/toggle/left.png);\n"
                "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.on_tv = QtWidgets.QPushButton(self.centralwidget)
        self.on_tv.setGeometry(QtCore.QRect(180, 120, 51, 51))
        self.on_tv.setStyleSheet("QPushButton{\n"
                                 "border: none;\n"
                                 "background-image: url(:/onandoff/power-button.png);\n""}")
        self.on_tv.setText("")
        self.on_tv.setObjectName("on_tv")
        self.maylanh = QtWidgets.QCheckBox(self.centralwidget)
        self.maylanh.setGeometry(QtCore.QRect(140, 290, 51, 31))
        self.maylanh.setStyleSheet("QCheckBox::indicator{\n"
                                   "width:50px;\n"
                                   "height:50px;\n"
                                   "image: url(:/toggle/left.png)\n""}")
        self.maylanh.setText("")
        self.maylanh.setObjectName("maylanh")
        self.off_tv = QtWidgets.QPushButton(self.centralwidget)
        self.off_tv.setGeometry(QtCore.QRect(110, 120, 51, 51))
        self.off_tv.setStyleSheet("QPushButton{\n"
                                  "border: none;\n"
                                  "background-image: url(:/onandoff/power-on.png);\n"
                                  "}")
        self.off_tv.setText("")
        self.off_tv.setObjectName("off_tv")
        self.keosang = QtWidgets.QSlider(self.centralwidget)
        self.keosang.setGeometry(QtCore.QRect(110, 220, 121, 22))
        self.keosang.setOrientation(QtCore.Qt.Horizontal)
        self.keosang.setObjectName("keosang")
        self.keosang.setMaximum(3)
        self.keosang.setPageStep(1)
        self.keosang.setSliderPosition(0)
        self.keosang.setTracking(True)
        self.keosang.setOrientation(QtCore.Qt.Horizontal)
        self.keosang.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(690, 0, 101, 101))
        self.textBrowser.setStyleSheet("background-image: url(:/logo/logo.png);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_ac = QtWidgets.QLabel(self.centralwidget)
        self.label_ac.setGeometry(QtCore.QRect(290, 80, 161, 91))
        self.label_ac.setStyleSheet("image: url(:/ac/ac_off.png);")
        self.label_ac.setText("")
        self.label_ac.setObjectName("label_ac")
        self.label_lamp = QtWidgets.QLabel(self.centralwidget)
        self.label_lamp.setGeometry(QtCore.QRect(440, 80, 131, 81))
        self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_off - Copy.png);")
        self.label_lamp.setText("")
        self.label_lamp.setObjectName("label_lamp")
        self.label_tv = QtWidgets.QLabel(self.centralwidget)
        self.label_tv.setGeometry(QtCore.QRect(440, 300, 151, 151))
        self.label_tv.setStyleSheet("image: url(:/tv/tv_off.png);")
        self.label_tv.setText("")
        self.label_tv.setObjectName("label_tv")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, -40, 351, 591))
        self.label_5.setStyleSheet("image: url(:/background/images.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 500, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sleep = QtWidgets.QPushButton(self.centralwidget)
        self.sleep.setGeometry(QtCore.QRect(20, 120, 71, 61))
        self.sleep.setStyleSheet("QPushButton{\n"
                                 "border: none;\n"
                                 "background-image: url(:/mode/sleeping.png);\n""}\n"
                                        "\n"
                                "")
        self.sleep.setText("")
        self.sleep.setObjectName("sleep")
        self.hot = QtWidgets.QPushButton(self.centralwidget)
        self.hot.setGeometry(QtCore.QRect(20, 240, 71, 71))
        self.hot.setStyleSheet("QPushButton{\n"
                                "border: none;\n"
                                "background-image: url(:/mode/hot-deal.png);\n"
                                "}")
        self.hot.setText("")
        self.hot.setObjectName("hot")
        self.relax = QtWidgets.QPushButton(self.centralwidget)
        self.relax.setGeometry(QtCore.QRect(20, 360, 71, 71))
        self.relax.setStyleSheet("QPushButton{\n"
                                 "border: none;\n"
                                 "background-image: url(:/mode/game-controller.png);\n"
                                 "}\n"
                                "")
        self.relax.setText("")
        self.relax.setObjectName("relax")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.textBrowser_2.setStyleSheet("background-image: url(:/background/130-hinh-nen-may-tinh-4k-89-1024x640.jpg);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.sensor = QtWidgets.QTextBrowser(self.centralwidget)
        self.sensor.setGeometry(QtCore.QRect(630, 390, 131, 71))
        self.sensor.setStyleSheet("QTextBrowser{\n"
                                  "border: none;\n"
                                  "background:transparent;\n"
                                  "}")
        self.sensor.setObjectName("sensor")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 100, 201, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_chart = QtWidgets.QPushButton(self.centralwidget)
        self.open_chart.setGeometry(QtCore.QRect(650, 340, 93, 28))
        self.open_chart.setStyleSheet("QPushButton {\n"
                                      "padding: 5px 5px;      /* Khoảng cách bên trong */\n"
                                      "border: none;                   /* Không có viền */\n" 
                                      "border-radius: 10px;           /* Đường viền bo tròn */\n"
                                      "background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, \n"
                                      "stop: 0 #ff0000, stop: 1 #0000ff);       /* Màu nền đen */\n"
                                      "color: #fff;                    /* Màu chữ trắng */\n"
                                                "}\n"
                                        "")
        self.open_chart.setObjectName("open_chart")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(40, 460, 71, 71))
        self.clear.setStyleSheet("QPushButton{\n"
                                "border: none;\n"
                                "background-image: url(:/clear/cleaning.png);\n"
                                "}")
        self.clear.setText("")
        self.clear.setObjectName("clear")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(660, 470, 71, 61))
        self.exit.setStyleSheet("QPushButton{\n"
                                "border: none;\n"
                                "background-image: url(:/exit/exit.png);\n"
                                "}")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.textBrowser_2.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.on_tv.raise_()
        self.maylanh.raise_()
        self.off_tv.raise_()
        self.keosang.raise_()
        self.textBrowser.raise_()
        self.label_ac.raise_()
        self.label_lamp.raise_()
        self.label_tv.raise_()
        self.label_6.raise_()
        self.sleep.raise_()
        self.hot.raise_()
        self.relax.raise_()
        self.sensor.raise_()
        self.verticalLayoutWidget.raise_()
        self.open_chart.raise_()
        self.clear.raise_()
        self.exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
  ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
        self.open_chart.clicked.connect(self.show_diagram) #hiển thị chart
        self.on_tv.clicked.connect(self.on)# bật tv
        self.off_tv.clicked.connect(self.off)# tắt tv
        self.maylanh.clicked.connect(self.toggle_ac)# bật tắt ac
        self.exit.clicked.connect(QtWidgets.QApplication.quit)#thoat
        self.sensor.setText(f"Độ ẩm:{doam}<br>Nhiệt độ:{nhietdo}") #sensor
        font = QtGui.QFont("Times New Roman", 12)
        self.sensor.setFont(font)
        self.keosang.valueChanged[int].connect(self.onSliderChange)
        self.sleep.clicked.connect(self.dingu)#che do di ngu
        self.hot.clicked.connect(self.nong)#che do qua nong
        self.relax.clicked.connect(self.neftlix)#che do giai tri
        self.clear.clicked.connect(self.bandau)# set lại ban đầu
 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Phòng ngủ thông minh"))
        self.label_6.setText(_translate("MainWindow", "Nguyễn Thanh Quân"))
        self.open_chart.setText(_translate("MainWindow", "open"))
    def show_diagram(self):
        thoi_gian = ['1h', '2h', '3h', '4h', '5h']  # Thời gian
        nhiet_do = [22, 24, 20, 23, 25]  # Nhiệt độ tương ứng (độ C
        fig, ax=plt.subplots()
        ax.bar(thoi_gian, nhiet_do, color='skyblue')
        ax.set_title('Biểu đồ Nhiệt độ theo Thời gian', fontdict={'fontsize': 8, 'fontweight': 'bold', 'fontfamily': 'Times New Roman'})
        ax.set_xlabel('Thời gian (h)', fontsize=12, fontfamily='Times New Roman')
        ax.set_ylabel('Nhiệt độ (°C)', fontsize=12, fontfamily='Times New Roman')
        canvas = FigureCanvas(fig)
        self.verticalLayout.addWidget(canvas)
    def on(self):
        self.label_tv.setStyleSheet("image: url(:/tv/tv_on.png);")
    def off(self):
        self.label_tv.setStyleSheet("image: url(:/tv/tv_off.png);")
    def toggle_ac(self):
        if self.maylanh.isChecked():
            self.label_ac.setStyleSheet("image: url(:/ac/ac_on.png);")
            self.maylanh.setStyleSheet("QCheckBox::indicator{\n"
                                        "width:50px;\n"
                                        "height:50px;\n"
                                        "image: url(:/toggle/right.png)\n"
                                        "}")
        elif (self.maylanh.isChecked()==False):
            self.label_ac.setStyleSheet("image: url(:/ac/ac_off.png);")
            self.maylanh.setStyleSheet("QCheckBox::indicator{\n"
                                        "width:50px;\n"
                                        "height:50px;\n"
                                        "image: url(:/toggle/left.png)\n"
                                        "}")
    def onSliderChange(self, value):
        if value==0:
            self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_off - Copy.png);")
        elif  value==1:
            self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_on1 - Copy.png);")
        elif value==2:
            self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_on2.png);")
        elif value==3:
            self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_on3.png);")

    def dingu(self):
        self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_off - Copy - Copy.png);")
        self.label_ac.setStyleSheet("image: url(:/ac/ac_on.png);")
   
        self.label_tv.setStyleSheet("image: url(:/tv/tv_off.png);")
    def nong(self):
        self.label_ac.setStyleSheet("image: url(:/ac/ac_max.png);")
    def neftlix(self):
        self.label_ac.setStyleSheet("image: url(:/ac/ac_on.png);")
        self.label_tv.setStyleSheet("image: url(:/tv/tv_on.png);")
        self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_off - Copy.png);")
    def bandau(self):
        self.label_tv.setStyleSheet("image: url(:/tv/tv_off.png);")
        self.label_ac.setStyleSheet("image: url(:/ac/ac_off.png);")
        self.label_lamp.setStyleSheet("image: url(:/lamp/lamp_off - Copy.png);")

 ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
