#players get the question at the same time
# Python program to implement server side of chat room. 
import socket 
import time
import select 
import sys 
import _thread
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import pyqtSlot
from subprocess import Popen, PIPE 
##################################33
global mess1,winner
#ques=str('')
winner=str('')
mess1="Order them in terms of their net worth(Descending)\n"+"A.Mukesh Ambani\nB.Bill Gates\nC.Warren Buffet\nD.Allen P Alex\n"
global click
click=0;
##########################################################################################################################
###### WAITING PAGE
##########################################################################################################################
class Ui_server1(object):
	def on_click(self):
		QtCore.QCoreApplication.instance().quit()
	def setupUi(self, server1):
		server1.setObjectName("server1")
		server1.resize(1296, 640)
		self.label = QtWidgets.QLabel(server1)
		self.label.setGeometry(QtCore.QRect(0, 0, 1291, 661))
		self.label.setStyleSheet("background-image: url(:/newPrefix/serverpg1.v1.jpg);")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(server1)
		self.label_2.setGeometry(QtCore.QRect(310, 230, 771, 181))
		self.label_2.setObjectName("label_2")
		self.pushButton= QtWidgets.QPushButton(server1)
		self.pushButton.setGeometry(QtCore.QRect(300, 150, 200, 60))
		self.pushButton.setStyleSheet("background-color: rgb(0,0,0);font-color: rgb(255,255,255)\n"
			"font: 20pt \"Ubuntu Condensed\";")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_click)
		self.retranslateUi(server1)
		QtCore.QMetaObject.connectSlotsByName(server1)

	def retranslateUi(self, server1):
		_translate = QtCore.QCoreApplication.translate
		server1.setWindowTitle(_translate("server1", "server"))
		self.label.setText(_translate("server1", "TextLabel"))
		self.label_2.setText(_translate("server1", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; font-style:italic; color:#ffffff;\">Awaiting Connections...</span></p></body></html>"))
		self.pushButton.setText(_translate("server1", "Continue"))
		self.pushButton.move(790,510)
import server_rc
def runs1():
    app = QtWidgets.QApplication(sys.argv)
    server1 = QtWidgets.QDialog()
    ui = Ui_server1()
    ui.setupUi(server1)
    server1.show()
    app.exec_()
##########################################################################################################################
###### QUESTION PAGE
##########################################################################################################################
class Ui_server2(object):
	def on_click(self):
		QtCore.QCoreApplication.instance().quit()
	def setupUi(self, server2):
		server2.setObjectName("server2")
		server2.resize(1021, 648)
		self.question = QtWidgets.QLabel(server2)
		self.question.setGeometry(QtCore.QRect(10, 20, 931, 551))
		self.question.setObjectName("question")
		self.label = QtWidgets.QLabel(server2)
		self.label.setGeometry(QtCore.QRect(-40, 0, 1071, 651))
		self.label.setStyleSheet("background-image: url(:/newPrefix/server2_v1.jpg);")
		self.label.setText("")
		self.label.setObjectName("label")
		self.pushButton= QtWidgets.QPushButton(server2)
		self.pushButton.setGeometry(QtCore.QRect(300, 150, 200, 60))
		self.pushButton.setStyleSheet("background-color: rgb(0,0,0);font-color: rgb(255,255,255)\n"
			"font: 20pt \"Ubuntu Condensed\";")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_click)
		self.retranslateUi(server2)
		QtCore.QMetaObject.connectSlotsByName(server2)
	def retranslateUi(self, server2):
		_translate = QtCore.QCoreApplication.translate
		server2.setWindowTitle(_translate("server2", "Question"))
		self.label.setText(_translate("server2","<html><head></head><body align=\"center\" ><p><h1><b>ORDER THEM BY THEIR NET_WORTH<br>(Descending)</b><br><br></h1></p><br><p><h2><font face=\"Courier New\" size=\"30\"><table align=\"center\" bgcolor=\"yellow\" width=\"70%\" height=\"15%\"  ><tr><td align=\"center\">A.Mukesh Ambani<td align=\"center\">B.Bill Gates</tr><br><br><tr><td align=\"center\">C.Warren Buffet<td align=\"center\">D.Allen P Alex</tr></table></font></h2></td></p></body></html>"))
		self.pushButton.setText(_translate("server2", "RESULTS"))
		self.pushButton.move(790,510)
import server2_rc
def runs2():
	app = QtWidgets.QApplication(sys.argv)
	server2 = QtWidgets.QDialog()
	ui = Ui_server2()
	ui.setupUi(server2)
	server2.show()
	app.exec_()
##########################################################################################################################
###### RESULT PAGE
##########################################################################################################################
class Ui_winner1(object):
	def on_click(self):
		QtCore.QCoreApplication.instance().quit()	
	def setupUi(self, winner1):
		winner1.setObjectName("winner1")
		winner1.resize(1403, 633)
		self.timing = QtWidgets.QLabel(winner1)
		self.timing.setGeometry(QtCore.QRect(40, 140, 831, 251))
		self.timing.setObjectName("timing")
		self.winnner = QtWidgets.QLabel(winner1)
		self.winnner.setGeometry(QtCore.QRect(130, 40, 601, 81))
		self.winnner.setObjectName("winnner")
		self.label = QtWidgets.QLabel(winner1)
		self.label.setGeometry(QtCore.QRect(-4, -14, 1411, 651))
		self.label.setStyleSheet("background-image: url(:/newPrefix/server3.v1.jpg);")
		self.label.setText("")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(winner1)
		self.label_2.setGeometry(QtCore.QRect(360,130, 500, 500))
		self.label_2.setObjectName("label_2")
		#self.label_2.setStyleSheet('color: white')
		self.label_2.setStyleSheet("font: 30pt Comic Sans MS")
		self.pushButton= QtWidgets.QPushButton(winner1)
		self.pushButton.setGeometry(QtCore.QRect(300, 150, 200, 60))
		self.pushButton.setStyleSheet("background-color: rgb(0,0,0);font-color: rgb(255,255,255)\n"
		"font: 20pt \"Ubuntu Condensed\";")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_click)
		self.retranslateUi(winner1)
		QtCore.QMetaObject.connectSlotsByName(winner1)

	def retranslateUi(self, winner1):
		_translate = QtCore.QCoreApplication.translate
		winner1.setWindowTitle(_translate("winner1", "Winner1"))
		self.timing.setText(_translate("winner1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
		#self.winner1.setText(_translate("winner1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
		self.label_2.setText(_translate("winner1","<html><head></head><body align=\"center\" color=\"white\" ><h1><b> WINNER IS</b></h1><font face=\"Courier New\" align =\"center\" size=\"500\"><h1>"+str(winner)+"</h1></font></body></html>"))
		self.pushButton.setText(_translate("winner1", "EXIT"))
		self.pushButton.move(790,510)
import server3_rc

def runs3():
	app = QtWidgets.QApplication(sys.argv)
	winner1 = QtWidgets.QDialog()
	ui = Ui_winner1()
	ui.setupUi(winner1)
	winner1.show()
	app.exec_()
##########################################################################################################################
###### THANK YOU PAGE
##########################################################################################################################
class Ui_winner2(object):
	def on_click(self):
		QtCore.QCoreApplication.instance().quit()	
	def setupUi(self, winner):
		winner.setObjectName("winner")
		winner.resize(1403, 633)
		self.timing = QtWidgets.QLabel(winner)
		self.timing.setGeometry(QtCore.QRect(40, 140, 831, 251))
		self.timing.setObjectName("timing")
		self.winnner = QtWidgets.QLabel(winner)
		self.winnner.setGeometry(QtCore.QRect(130, 40, 601, 81))
		self.winnner.setObjectName("winnner")
		self.label = QtWidgets.QLabel(winner)
		self.label.setGeometry(QtCore.QRect(-4, -14, 1411, 651))
		self.label.setStyleSheet("background-image: url(:/newPrefix/server3.v1.jpg);")
		self.label.setText("")
		self.label.setObjectName("label")
		self.pushButton= QtWidgets.QPushButton(winner)
		self.pushButton.setGeometry(QtCore.QRect(300, 150, 200, 60))
		self.pushButton.setStyleSheet("background-color: rgb(0,0,0);font-color: rgb(255,255,255)\n"
		"font: 20pt \"Ubuntu Condensed\";")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_click)
		self.retranslateUi(winner)
		QtCore.QMetaObject.connectSlotsByName(winner)

	def retranslateUi(self, winner):
		_translate = QtCore.QCoreApplication.translate
		winner.setWindowTitle(_translate("winner", "Winner"))
		self.timing.setText(_translate("winner", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
		self.winnner.setText(_translate("winner", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
		self.label.setText(_translate("winner","<html><head></head><body align=\"center\" ><p><h1><b>BETTER LUCK NEXT TIME</b></body></html>"))
		self.pushButton.setText(_translate("winner", "END GAME"))
		self.pushButton.move(790,510)
import server3_rc

def runs4():
	app = QtWidgets.QApplication(sys.argv)
	winner = QtWidgets.QDialog()
	ui = Ui_winner2()
	ui.setupUi(winner)
	winner.show()
	app.exec_()

##########################################################################################################################
###### END OF GUI
##########################################################################################################################

global player_count
player_count=0 

global timer
timer=[]

global mark
mark=[]

global present
present=[]

global flagq
flagq=0 

global q
q=[] 


"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 


# checks whether sufficient arguments have been provided 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 


# takes the first argument from command prompt as IP address 
IP_address = str(sys.argv[1]) 


# takes second argument from command prompt as port number 
Port = int(sys.argv[2]) 

""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind(('', Port)) 

""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100) 


list_of_clients = [] 


def clientthread(conn, addr, flagq): 
    pcount=player_count
    flagq1=flagq
	# sends a message to the client whose user object is conn 
	#conn.send("Welcome to Fastest Finger First!Qn1.Arrange the following in ascending order2 3 1 4") 
    message="Welcome to Fastest Finger First!"
    message12="You are player "+str(pcount)
    message1=message12
    q.append(0)
   
    conn.send(message.encode('ascii'))
    conn.send(message1.encode('ascii'))
    
    while player_count!=2:
    	pass
    time.sleep(10)
    #ques=mess1
    mess2=mess1
    if(1 not in q):
    	#runs2()
    	print("question is: ", mess2)
    	q[pcount-1]=1
    conn.send(mess2.encode('ascii'))
    t1=time.time()
    correct=['1','2','3','4']
    message = conn.recv(2408)
    message1=message.decode('ascii')
    t2=time.time()
    print ("pcount"+str(player_count)+"time "+ str(t2-t1))
    
    print("mess "+str(message1))
    ans=message1.strip('\n')
    ans1=ans.split(' ')
    print (ans1)
    if ans1==correct:
    	mark[pcount-1]=1
    	timer[pcount-1]=t2-t1
    	m1="You are right"
    	conn.send(m1.encode('ascii'))
    else:
    	m2="You are wrong"
    	conn.send(m2.encode('ascii'))
    present[pcount-1]=1	
    print("\nmark: ", mark)
    print("timer: ", timer)
    print("present: ", present)
	#TAKE TIME STAMPPPPPP
	#if k=="A":
	#	conn.send('You are right\nQn2.What is National Animal of India\nA.Tiger B.Lion C.Rat')
		
	#else:
	#	conn.send('You are wrong')
		
			#print "<" + addr[0] + "> " + message 

			# Calls broadcast function to send message to all 
	#	message_to_send = "<" + addr[0] + "> " + message 
	#	broadcast(message_to_send, conn) 

		
			

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

"""The following function simply removes the object 
from the list that was created at the beginning of 
the program"""
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True:
	if(player_count==2):
		runs2()
		time.sleep(20)
		break
	"""Accepts a connection request and stores two parameters, 
	conn which is a socket object for that user, and addr 
	which contains the IP address of the client that just 
	connected"""
	conn, addr = server.accept() 

	"""Maintains a list of clients for ease of broadcasting 
	a message to all available people in the chatroom"""
	list_of_clients.append(conn) 

	# prints the address of the user that just connected 
	print (addr[0] + " connected")
	if(player_count==0):
		runs1()	
	# creates and individual thread for every user 
	# that connects 

	
	player_count=player_count+1
	mark.append(0)
	present.append(0)
	timer.append(100)
	_thread.start_new_thread(clientthread,(conn,addr, flagq))


conn.close() 
server.close() 
if(1 in mark):
	winner=str(timer.index(min(timer))+1)
	print("winner is ", timer.index(min(timer))+1)
	time.sleep(3)
	runs3()
else:
	runs4()
	print("BETTER LUCK NEXT TIME")

