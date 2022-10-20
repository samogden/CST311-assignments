#!env python

"""TCP Client for CST311 Programming Assignment 1"""
__author__ = "[team name here]"
__credits__ = [
  "Your",
  "Names",
  "Here"
]


import socket as s


# Import and configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

import TCPServer

server_host = "localhost"

def main():
  
  
  # Get input message from user
  message = input("Input lowercase sentence:")
  
  # We use a with statement (see pep-0343 for details) to automatically close the socket when we are done
  ## It's important to close sockets after you are done with them.
  ## We pass two arguments to socket:
  ### s.AF_INET says we are using an address from the internet
  ### s.SOCK_STREAM says we are using a TCP socket
  # Note the difference between the socket module (which we are referring to as 's' per line 12),
  ## and our own socket which we are naming socket
  with s.socket(s.AF_INET, s.SOCK_STREAM) as socket:
    
    # Connect our socket.  Notice that we pull server port directly from our TCPServer class.
    ## Q: Why is this step not in our UDP client?
    socket.connect(
      (server_host, TCPServer.SERVER_PORT)
    )
    
    # Send data, encoded as a UTF-8 bytestream
    socket.send(message.encode())
    
    # Wait for a response
    ## note, we won't move beyond this point until there is something to recieve from the socket
    response = socket.recv(1024)
    
    print ("From Server:", response.decode())

if __name__ == "__main__":
  main()