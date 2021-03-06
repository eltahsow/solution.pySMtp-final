from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #mailserver = '127.0.0.1'
    #mailPort = 1025
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM: <es5754@ny.edu> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2 )
    #if recv1[:3] != '250':
        #print('250 reply not received from server')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTO = "RCPT TO: <destination@gmail.com> \r\n"
    recv3 = clientSocket.recv(1024).decode()
    #print("after RCPT TO COMMAND: " +recv3)
    #if recv1[:3] != '250':
        #print('250 reply not received from server')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send((data.encode()))
    recv4 = clientSocket.recv(1024).decode()
    #print("After Data Command: " =recv4)
    #if recv1[:3] != '250':
        #print ('250 reply not received from server')
    # Fill in end

    # Send message data.
    # Fill in start
    Subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocketSocket.send(subject.encode())
    message = raw_input("Enter your message: \r\n")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    #print ("Response after sending message body:" +recv_msg.decode())
    #if recv1[:3] != '250':
        #print('250 reply not received from server')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024)
    #print(message)
    clientSocket.close()
    # Fill in end
                  
if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')

