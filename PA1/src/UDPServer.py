#! env python

"""UDP server for CST311 Programming Assignment 1"""
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

# Define a port to use above 1024
## Q: If we were to use 0 what would be the impact?
SERVER_PORT = 12001


def handle_client_request(server_socket, message, client_addr):
  """Handles invidiual connections from clients
  
  :param server_socket: server UDP socket to write back to client with
  :param message: message from client
  :param client_addr: client address to respond to
  :return:
  """
  
  log.debug("Recieved message: \"" + message + "\" from client @ \"" + client_addr + "\"")
  
  # Does two things:
  ## 1. decode message -- messages are transmitted as a UTF-8 bytestream so we have to decode them
  ## 2. convert string to upcase -- we use the upper() str function
  response_msg = message.decode().upper()
  
  # Encode the message string back to a UTF-8 bytestream
  response = response_msg.encode()
  
  # Send the message across our common socket to the client specified by the client address
  ## Q: could there be problems with multithreading in this configuration?
  server_socket.sendto(
    response,
    client_addr
  )
  

def main():
  
  
  # We use a with statement (see pep-0343 for details) to automatically close the socket when we are done
  ## It's important to close sockets after you are done with them.
  ## We pass two arguments to socket:
  ### s.AF_INET says we are using an address from the internet
  ### s.SOCK_DGRAM says we are using a UDP socket
  # Note the difference between the socket module (which we are referring to as 's' per line 12),
  ## and our own socket which we are naming socket
  with s.socket(s.AF_INET, s.SOCK_DGRAM) as socket:
  
    # Bind the socket to a particular port
    ## Note that the first part (e.g. '') specifies an empty string, indicating we should be generally
    socket.bind(('', SERVER_PORT))
    
    log.info("The server is ready to receive")
    
    # Start an infinite loop to wait until we hear from a client
    ## Note, this loop will continue until ^C is issued (aka cntl-c, the kill signal)
    while True:
      # Get the message and client address from the socket
      ## Q: Why do we need to get the client address?
      message, client_addr = socket.recvfrom(1024)
      
      # Pass the message and address, along with the socket, to a specific function to handle client requests
      handle_client_request(socket, message, client_addr)

if __name__ == "__main__":
  main()