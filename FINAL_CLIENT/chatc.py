import socket 
import select 
import sys 
import datetime
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import pyqtSlot
from subprocess import Popen, PIPE
#import keyboard
#from keyboard import press
global player
global plno
global click1,click2,click3,click4
click1=0
click2=0
click3=0
click4=0
global texteditValue
global message,message1
import string
global partQ
global partT
global partA
global partB
global partC
global partD
partQ=str('')
partT=str('')
partA=str('')
partB=str('')
partC=str('')
partD=str('')
message1=str('')
message=str('')
texteditValue=str('')


##########################################################################3333
###########################################################################333333
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1253, 656)
        MainWindow.setStyleSheet("background-image: url(:/BACK/white.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1253, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#ssimport white_rc


def back():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if(click4==1):
    	app.exec_()
#back()
###############################################################################
###############################################################################



###-----------=-------------------------------------------------------
###page1-------------------------------------------------------
###-----------------------------------------------------------
class Ui_Dialog(object):
	def on_click(self):
		global click1
		click1=1
		print('PyQt5 button click ',click1)
		QtCore.QCoreApplication.instance().quit()
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(691,421)
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(-4, -4,691 , 421))
		self.label.setStyleSheet("background-image: url(:/newPrefix/clock.jpeg);")
		self.label.setText("")
		self.label.setObjectName("label")
		#pixmap = QPixmap('1.jpeg')
		#self.label.setPixmap(pixmap)
		#self.label.resize(pixmap.width(),pixmap.height())
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(330, 80, 341, 61))
		self.label_2.setObjectName("label_2")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(410, 240, 181, 51))
		self.pushButton.setStyleSheet("background-color: rgb(211, 215, 207);\n"
		"font: 15pt \"Ubuntu Condensed\";")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_click)
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Welcome to Fastest Finger First!!</span></p></body></html>"))
		self.pushButton.setText(_translate("Dialog", "START"))
import cpage11


def run1():
    app = QtWidgets.QApplication(sys.argv)
    click1=1
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))
###------------------------------------------------------------------
###page2-------------------------------------------------------
###-----------------------------------------------------------
class Ui_page2(object):
	def on_click(self):
		global click2
		click2=1
		print('PyQt5 button click ',click2)
		QtCore.QCoreApplication.instance().quit()
	def setupUi(self, page2):
	    page2.setObjectName("page2")
	    page2.resize(846, 529)
	    self.label = QtWidgets.QLabel(page2)
	    self.label.setGeometry(QtCore.QRect(-4, -4, 851, 611))
	    self.label.setStyleSheet("background-image: url(:/newPrefix/instruction.jpeg);")
	    self.label.setText("")
	    self.label.setObjectName("label")
	    self.label_2 = QtWidgets.QLabel(page2)
	    self.label_2.setGeometry(QtCore.QRect(310, 80, 211, 51))
	    self.label_2.setObjectName("label_2")
	    self.label_3 = QtWidgets.QLabel(page2)
	    self.label_3.setGeometry(QtCore.QRect(40, 140, 641, 351))
	    self.label_3.setObjectName("label_3")
	    self.pushButton = QtWidgets.QPushButton(page2)
	    self.pushButton.setGeometry(QtCore.QRect(640, 450, 121, 41))
	    self.pushButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
	    "color: rgb(255, 255, 255);")
	    self.pushButton.setObjectName("pushButton")
	    self.pushButton.clicked.connect(self.on_click)        
	    self.label_4 = QtWidgets.QLabel(page2)
	    self.label_4.setGeometry(QtCore.QRect(310, 60, 67, 17))
	    self.label_4.setText("")
	    self.label_4.setObjectName("label_4")
	    self.label_5 = QtWidgets.QLabel(page2)
	    self.label_5.setGeometry(QtCore.QRect(300, 40, 241, 31))
	    self.label_5.setObjectName("label_5")
	    self.retranslateUi(page2)
	    QtCore.QMetaObject.connectSlotsByName(page2)
	def retranslateUi(self, page2):
		_translate = QtCore.QCoreApplication.translate
		page2.setWindowTitle(_translate("page2", "instruction"))
		self.label_2.setText(_translate("page2", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">INSTRUCTIONS</span></p></body></html>"))
		self.label_3.setText(_translate("page2", "<html><head/><body><p><b><i>"+str(player)+"</b></i></p><p><span style=\" font-size:18pt;\">1. There will be one question provided.</span></p><p><span style=\" font-size:18pt;\">2.Type your answer with spaces in the box provided.</span></p><p><span style=\" font-size:18pt;\">3. Click submit to finish.</span></p><p><span style=\" font-size:18pt;\">4. Click the play button to continue.</span></p><p><br/></p><p><span style=\" font-size:18pt; font-style:italic;\">The winner is chosen based on the earliest correct response.</span></p><p><br/></p><p><span style=\" font-size:18pt; font-weight:600;\">ALL THE BEST!</span></p></body></html>"))
		self.pushButton.setText(_translate("page2", "PLAY"))
		self.label_5.setText(_translate("page2", "<html><head/><body><p><br/></p></body></html>"))
import cpage22


def run2():
	app = QtWidgets.QApplication(sys.argv)
	page2 = QtWidgets.QDialog()
	ui = Ui_page2()
	ui.setupUi(page2)
	page2.show()
	app.exec_()
###------------------------------------------------------------------
###pagerandom-------------------------------------------------------
###-----------------------------------------------------------
class Ui_Dialog1(object):
    def on_click(self):
        global click1
        click1=1
        print('PyQt5 button click ',click1)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(self.on_click)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

def run3():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
###------------------------------------------------------------------
###page3-------------------------------------------------------
###-----------------------------------------------------------
class Ui_Dialog2(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(620, 420)
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(0, 10, 621, 421))
		self.label.setStyleSheet("background-image: url(:/newPrefix/1.jpeg);")
		self.label.setObjectName("label")
		
		"""
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(60, 80, 301, 141))
		self.label_2.setObjectName("label_2")
		"""
		#self.lineEdit = QtWidgets.QLineEdit(Dialog)
		#self.lineEdit.setGeometry(QtCore.QRect(110, 270, 131, 41))
		#self.lineEdit.setObjectName("lineEdit")
		self.textedit = QtWidgets.QLineEdit(Dialog)
		self.textedit.setGeometry(QtCore.QRect(110, 270, 131, 41))
		self.textedit.setObjectName("Textedit")
		self.textedit.move(165, 180)
		self.textedit.resize(280,40)
		self.button = QtWidgets.QPushButton(Dialog)
		self.button.setGeometry(QtCore.QRect(380, 330, 131, 31))
		self.button.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
		"background-color: rgb(186, 189, 182);")
		self.button.setObjectName("button")
		self.button.move(445,185)
		
		# connect button to function on_click
		self.button.clicked.connect(self.on_click1)
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.label.setText(_translate("server2","<html><head></head><body align \"center\" ><p><h1><span style=\" color:#ffffff; font-size=45pt;\"><center><b>"+str(partQ)+"<<br></center><center>"+str(partT)+"</center></span></b><br><br></h1></p><br><p><h2><font face=\"Courier New\" size=\"5\"><table align=\"center\" bgcolor=\"white\" width=\"30%\" height=\"5%\"  ><tr><td align=\"center\">"+str(partA)+"<td align=\"center\">"+str(partB)+"</tr><br><br><tr><td align=\"center\">"+str(partC)+"<td align=\"center\">"+str(partD)+"</tr></table></font></h2></td></p></body></html>"))
		#self.label.setText(_translate("Dialog", "TextLabel"))
		#self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#eeeeec;\">"+str(message1)+"</span></p></body></html>"))
		#self.lineEdit.setText(_translate("Dialog", " "))
		self.button.setText(_translate("Dialog", "Submit"))
	def on_click1(self):
		global texteditValue
		texteditValue = self.textedit.text()
		#print >> open('file.txt','a'),texteditValue
		global click3
		click3=1
		#print('PyQt5 button click ',click1)
		QtCore.QCoreApplication.instance().quit()
	#@pyqtSlot()
import cpage33

def run4():
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog2()
	ui.setupUi(Dialog)
	Dialog.show()
	app.exec_()
###------------------------------------------------------------------
###THANK YOU-------------------------------------------------------
###-----------------------------------------------------------
class Ui_thankyou_2(object):
    def setupUi(self, thankyou_2):
        thankyou_2.setObjectName("thankyou_2")
        thankyou_2.resize(636, 545)
        self.thankyou = QtWidgets.QLabel(thankyou_2)
        self.thankyou.setGeometry(QtCore.QRect(-4, -4, 641, 561))
        self.thankyou.setStyleSheet("     \n"
"background-image: url(:/newPrefix/thanks.jpg);")
        self.thankyou.setText("")
        self.thankyou.setObjectName("thankyou")

        self.retranslateUi(thankyou_2)
        QtCore.QMetaObject.connectSlotsByName(thankyou_2)

    def retranslateUi(self, thankyou_2):
        _translate = QtCore.QCoreApplication.translate
        thankyou_2.setWindowTitle(_translate("thankyou_2", "thankyou"))
import thanks_rc

def run5():
	app = QtWidgets.QApplication(sys.argv)
	thankyou_2 = QtWidgets.QDialog()
	ui = Ui_thankyou_2()
	ui.setupUi(thankyou_2)
	thankyou_2.show()
	app.exec_()


###############
###DRIVER FUNCTION
###############
global read
read=0
while True: 

	flag=0
	sockets_list = [sys.stdin, server] 
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		#sys.stdout.write(str(texteditValue))
		if(read==3):
			print("\n")
		if socks == server: 
			print("READread\n",read)
			message1 = socks.recv(2048) 
			print (message1)
			if(read==1):
				player=str('')
				player=str(message1).replace('b\'','')
			if(read==2):
				part1=str('')
				part2=str('')
				part=str(message1).split("\\n")
				#part1=part.replace('\\','')
				print(part)
				part2=part[0].replace('\\','')
				part2=part2.replace('b\'','')
				part3=part2.split('(')
				partQ=part3[0]
				partT='('+part3[1]
				partA=part[1].replace('\\','')
				partB=part[2].replace('\\','')
				partC=part[3].replace('\\','')
				partD=part[4].replace('\\','') 
			if read==4:
				click4=1
				flag=1
		else:
			print("MESSAGEread",read)
			message = sys.stdin.readline() 
			print ("message:" + str(texteditValue))
			server.send(texteditValue.encode('ascii')) 
			sys.stdout.flush() 
		
		#print("read click\n ",read,click1) 
		if(read==0):
			run1()
		elif(read==1 and click1==1):#and click1==1):
			run2()
		elif(read==2 and click2==1):
			run4()
		elif(read==4):
			run5()
		read+=1
	if(flag==1):
		break

server.close() 





