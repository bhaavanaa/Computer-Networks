#players get the question at the same time
# Python program to implement server side of chat room. 
import socket 
import time
import select 
import sys 
import _thread 


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
    message12="You are player number "+str(pcount)
    message1=message12
    q.append(0)
   
    conn.send(message.encode('ascii'))
    conn.send(message1.encode('ascii'))
    
    while player_count!=2:
    	pass
    time.sleep(10)
    mess1="give the correct order"+"1 2 3 4"
    mess2=mess1
    if(1 not in q):
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
	# creates and individual thread for every user 
	# that connects 
	player_count=player_count+1
	mark.append(0)
	present.append(0)
	timer.append(100)
	_thread.start_new_thread(clientthread,(conn,addr, flagq))	 

if(1 in mark):
	print("winner is ", timer.index(min(timer))+1)
else:
	print("waste fellow!!!")
conn.close() 
server.close() 


