from datetime import datetime
from socket import *
from time import time

def main():

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = 'Ping'

    #initializing the variables
    counter = 10
    i = 0

    print 'Now attempting ', counter, 'pings....\n'

    while i < counter:

        i+= 1
        print '\n This is Ping attempt number: ',i
        print 'There are ',counter - i, 'attempts left.'

        a = datetime.now()
        clientSocket.sendto(message,(serverName,serverPort))



        clientSocket.settimeout(1) #Setting the timeout as 1 sec

        try:
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)

            b = datetime.now()
            c = a-b;
            print modifiedMessage
            print 'elapsed time in microseconds is --> ',c.microseconds
        except timeout:
            print 'Sorry! Your connection has timed out! Please try again.'

    if i == 10:
        print 'Bye!'

    clientSocket.close()

    print 'Socket has been closed! No more pings!'

    pass

if __name__ == '__main__' :
    main()
