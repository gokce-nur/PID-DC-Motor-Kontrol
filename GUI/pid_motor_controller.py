# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pid_motor_controller_GUI.ui'
#
# Author: Gökçe Nur Beken


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QIODevice
from mplwidget import MplWidget
import sys
import serial
import threading
import time
from threading import Thread
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import collections
import struct
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
#-------------------------------------------------------Created by: PyQt5 UI code generator 5.9.2--------------------------------------------------#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 785)
        MainWindow.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(40, 630, 89, 25))
        self.pushButton_start.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"gridline-color: rgb(46, 52, 54);")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(40, 680, 89, 25))
        self.pushButton_stop.setStyleSheet("background-color: rgb(164, 0, 0);\n"
"gridline-color: rgb(46, 52, 54);")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.lineEdit_setSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_setSpeed.setGeometry(QtCore.QRect(170, 650, 113, 25))
        self.lineEdit_setSpeed.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_setSpeed.setText("")
        self.lineEdit_setSpeed.setObjectName("lineEdit_setSpeed")
        self.lineEdit_kp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kp.setGeometry(QtCore.QRect(310, 650, 113, 25))
        self.lineEdit_kp.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_kp.setObjectName("lineEdit_kp")
        self.lineEdit_ki = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ki.setGeometry(QtCore.QRect(450, 650, 113, 25))
        self.lineEdit_ki.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_ki.setObjectName("lineEdit_ki")
        self.lineEdit_kd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd.setGeometry(QtCore.QRect(590, 650, 113, 25))
        self.lineEdit_kd.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(730, 650, 89, 25))
        self.pushButton_send.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"gridline-color: rgb(46, 52, 54);")
        self.pushButton_send.setObjectName("pushButton_send")
        self.label_setSpeed = QtWidgets.QLabel(self.centralwidget)
        self.label_setSpeed.setGeometry(QtCore.QRect(190, 680, 67, 17))
        self.label_setSpeed.setObjectName("label_setSpeed")
        self.label_kp = QtWidgets.QLabel(self.centralwidget)
        self.label_kp.setGeometry(QtCore.QRect(330, 680, 67, 17))
        self.label_kp.setObjectName("label_kp")
        self.label_ki = QtWidgets.QLabel(self.centralwidget)
        self.label_ki.setGeometry(QtCore.QRect(470, 680, 67, 17))
        self.label_ki.setObjectName("label_ki")
        self.label_kd = QtWidgets.QLabel(self.centralwidget)
        self.label_kd.setGeometry(QtCore.QRect(610, 680, 67, 17))
        self.label_kd.setObjectName("label_kd")
        self.lineEdit_currentSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_currentSpeed.setGeometry(QtCore.QRect(880, 520, 113, 25))
        self.lineEdit_currentSpeed.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_currentSpeed.setObjectName("lineEdit_currentSpeed")
        self.label_currentSpeed = QtWidgets.QLabel(self.centralwidget)
        self.label_currentSpeed.setGeometry(QtCore.QRect(890, 550, 101, 17))
        self.label_currentSpeed.setObjectName("label_currentSpeed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 591, 71))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 57 33pt \"Ubuntu\";\n"
"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(117, 80, 123, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(59, 129, 801, 411))
        self.MplWidget.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.MplWidget.setObjectName("MplWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 560, 411, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PID Controller"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
        self.pushButton_send.setText(_translate("MainWindow", "SEND"))
        self.label_setSpeed.setText(_translate("MainWindow", "Set Speed"))
        self.label_kp.setText(_translate("MainWindow", "       Kp"))
        self.label_ki.setText(_translate("MainWindow", "       Ki"))
        self.label_kd.setText(_translate("MainWindow", "       Kd"))
        self.label_currentSpeed.setText(_translate("MainWindow", "Current Speed"))
        self.label.setText(_translate("MainWindow", "PID MOTOR SPEED CONTROL"))
        self.label_2.setText(_translate("MainWindow", ""))

#----------------------------------------------------------------------------------END-------------------------------------------------------------------#

        self.pushButton_stop.setEnabled(False)
        self.pushButton_start.clicked.connect(self.start_function)
        self.pushButton_stop.clicked.connect(self.stop_function)
        self.pushButton_send.clicked.connect(self.send_function)
        self.ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        # self.ser.pressed.connect(self.current_speed_function)
        time.sleep(1)

    def send_function(self):
        def setValueSpeed():
            msg = "set_speed"
            setspeed = self.lineEdit_setSpeed.text()
            msg = msg + setspeed + "\n"
            self.ser.write(msg.encode('utf-8'))

        def setValueKp():
            msg_kp = "Kp"
            kp = self.lineEdit_kp.text()
            msg_kp = msg_kp + kp + "\n"
            self.ser.write(msg_kp.encode('utf-8'))
            
        
        def setValueKi():
            msg_ki = "Ki"
            ki= self.lineEdit_ki.text()
            msg_ki = msg_ki + ki + "\n"
            self.ser.write(msg_ki.encode('utf-8'))

        def setValueKd():
            msg_kd = "Kd"
            kd = self.lineEdit_kd.text()
            msg_kd = msg_kd + kd + "\n"
            self.ser.write(msg_kd.encode('utf-8'))
        
        counter = 0
        if not self.ser.isOpen():
            self.ser.open()
        if counter == 0:
            setValueSpeed()
            setValueKp()
            setValueKi()
            setValueKd()
            counter = counter +1
            time.sleep(2)
        else:
            self.ser.close()

    def start_function(self):
        self.label_2.setText("Motor is Starting!")
        def setValues():
            self.ser.write(b"start\n")
        counter = 0
        if not self.ser.isOpen():
                self.ser.open(QIODevice.Read)
        if counter == 0:
            setValues()
            counter = counter + 1
            time.sleep(1)
        else:
            self.ser.close()
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setEnabled(True)

    def stop_function(self):
        msg_stop = "stop" + "\n"
        msg_stop = msg_stop.encode('utf-8')
        self.ser.write(msg_stop)
        if not self.ser.isOpen():
                self.ser.open(QIODevice.Read)
        self.label_2.setText("Motor is Stopping!")
        self.pushButton_stop.setEnabled(False)
        self.pushButton_start.setEnabled(True)
        time.sleep(1)

#     def current_speed_function(self):
         
#         self.lineEdit_currentSpeed.setText("%s",self.ser.readSerialStart().data().decode())
#         self.ser.close()
    def graph_view(self):
        portName = '/dev/ttyACM0'   
        baudRate = 9600
        maxPlotLength = 100
        dataNumBytes = 4        
        s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes)   
        s.readSerialStart()                                               

        pltInterval = 50    # Period at which the plot animation updates [ms]
        xmin = 0
        xmax = maxPlotLength
        ymin = -(5000)
        ymax = 5000
        fig = plt.figure()
        ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
        ax.set_title('Arduino Serial Read')
        ax.set_xlabel("time")
        ax.set_ylabel("Motor Speed (rpm)")

        lineLabel = 'Motor Speed Value'
        timeText = ax.text(0.50, 0.95, '', transform=ax.transAxes)
        lines = ax.plot([], [], label=lineLabel)[0]
        lineValueText = ax.text(0.50, 0.90, '', transform=ax.transAxes)
        anim = animation.FuncAnimation(fig, s.getSerialData, fargs=(lines, lineValueText, lineLabel, timeText), interval=pltInterval)    # fargs has to be a tuple

        plt.legend(loc="upper left")
        plt.show()

        s.close()



class serialPlot:
    def __init__(self, serialPort = '/dev/ttyACM0', serialBaud = 38400, plotLength = 100, dataNumBytes = 2):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.rawData = bytearray(dataNumBytes)
        self.data = collections.deque([0] * plotLength, maxlen=plotLength)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.plotTimer = 0
        self.previousTimer = 0
        self.csvData = []

        print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        try:
            self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=4)
            print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        except:
            print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

    def readSerialStart(self):
        if self.thread == None:
            self.thread = Thread(target=self.backgroundThread)
            self.thread.start()
            # Block till we start receiving values
            while self.isReceiving != True:
                time.sleep(0.1)

    def getSerialData(self, frame, lines, lineValueText, lineLabel, timeText):
        currentTimer = time.perf_counter()
        self.plotTimer = int((currentTimer - self.previousTimer) * 1000)     # the first reading will be erroneous
        self.previousTimer = currentTimer
        timeText.set_text('Plot Interval = ' + str(self.plotTimer) + 'ms')
        value,  = struct.unpack('f', self.rawData)    # use 'h' for a 2 byte integer
        self.data.append(value)    # we get the latest data point and append it to our array
        lines.set_data(range(self.plotMaxLength), self.data)
        lineValueText.set_text('[' + lineLabel + '] = ' + str(value))
        self.csvData.append(self.data[-1])

    def backgroundThread(self):    # retrieve data
        time.sleep(1.0)  # give some buffer time for retrieving data
        self.serialConnection.reset_input_buffer()
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            self.isReceiving = True
            #print(self.rawData)

    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        print('Disconnected...')

def main():
    application = QtWidgets.QApplication(sys.argv)
    control = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(control)
    control.show()
#     ui.current_speed_function()
    ui.graph_view()
    sys.exit(application.exec_()) 
 
if __name__ == '__main__':
    main()