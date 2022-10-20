#!env python

"""TCP server for CST311 Programming Assignment 1"""
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

SERVER_PORT = 12000

def handle_client_request(conn):
  
  # Wait until we receive a message from the client.  Once we have it decode it from a UTF-8 bytestream
  message = conn.recv(1024).decode()
  
  # Process the message.  In this case we convert to uppercode
  response = message.upper()
  
  # Send the message back to the client, encoding our response to a UTF-8 bytestream
  conn.send(response.encode())
  
  # Close our connection
  conn.close()


def main():
  
  
  # We use a with statement (see pep-0343 for details) to automatically close the socket when we are done
  ## It's important to close sockets after you are done with them.
  ## We pass two arguments to socket:
  ### s.AF_INET says we are using an address from the internet
  ### s.SOCK_STREAM says we are using a TCP socket
  # Note that we are calling this "welcome_socket" since this would be used for all incoming TCP connection handshakes
  with s.socket(s.AF_INET, s.SOCK_STREAM) as welcome_socket:
    
    # Bind the socket to a particular port
    ## Note that the first part (e.g. '') specifies an empty string, indicating we should be generally
    welcome_socket.bind(('', SERVER_PORT))
    
    # Set the listen parameter, which is how many connections we can enqueue while dealing with a connection
    ## Note: these are not concurrent connections, just how may we can have waiting at once
    welcome_socket.listen(1)
    
    log.info("The server is ready to receive")
    
    # Start an infinite loop to wait until we hear from a client
    ## Note, this loop will continue until ^C is issued (aka cntl-c, the kill signal)
    while True:
      # Wait for a client to connect to us
      ## Note that we use an underscore ('_') to explicitly ignore the client address
      ## Q: Why can we do ignore the client address?
      connection_socket, _ = welcome_socket.accept()
      
      # Pass the message and address, along with the socket, to a specific function to handle client requests
      handle_client_request(connection_socket)
      
  
if __name__ == "__main__":
  main()


