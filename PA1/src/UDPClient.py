#!env python

"""UDP client for CST311 Programming Assignment 1"""
__author__ = "[team name here]"
__credits__ = [
  "Your",
  "Names",
  "Here"
]

# Import the socket module as a named module to help keep our namespace clean
import socket as s

# Import and configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Import our module last
import UDPServer

# localhost is shorthand for our current host.  If talking to a different host this should be changed
server_host = 'localhost'
# We grab the server port from our server so we are guaranteed to be using the same one
server_port = UDPServer.SERVER_PORT

def main():
  
  # Get input message from user
  message = input("Input lowercase sentence:")
  
  # We use a with statement (see pep-0343 for details) to automatically close the socket when we are done
  ## It's important to close sockets after you are done with them.
  ## We pass two arguments to socket:
  ### s.AF_INET says we are using an address from the internet
  ### s.SOCK_DGRAM says we are using a UDP socket
  with s.socket(s.AF_INET, s.SOCK_DGRAM) as socket:
    
    # Send data across the docket
    ## Notice how we encode the message to a UTF-8 bytestream
    ## The second argument of sendto is the address we're sending too -- it contains a server name and the port
    socket.sendto(
      message.encode(),
      (server_host, server_port)
    )
  
    # We use the '_' character to represent a do-not-care in python and implicitly throw out the value returned
    ## In this case we already know the server address so we don't need to record it when we read the response
    response_msg, _ = socket.recvfrom(1024)
    print(response_msg.decode())
    
if __name__ == "__main__":
  main()
