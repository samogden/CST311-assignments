#!env python

"""Chat server for CST311 Programming Assignment 3"""
__author__ = "[team 1]"
__credits__ = [
  "Aiden Rougot",
  "Nayan Gupta",
  "Jonathan McCaslin", 
  "Hal Halberstadt"  
]


import socket as s
import threading

# Configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_port = 12000
response = ""
temp = 0

def connection_handler(connection_socket, address, query_decoded):
  # Read data from the new connectio socket
  #  Note: if no data has been sent this blocks until there is data
  # Log query information
  globals()['temp'] += 1
  log.info("Recieved query test \"" + str(query_decoded) + "\"")
  
  # Perform some server operations on data to generate response
  globals()['response'] += str(address) + ":" + query_decoded.upper() + " "
    
  
  

def main():
  # Create a TCP socket
  # Notice the use of SOCK_STREAM for TCP packets
  server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
  
  # Assign IP address and port number to socket, and bind to chosen port
  server_socket.bind(('',server_port))
  
  # Configure how many requests can be queued on the server at once
  server_socket.listen(2)
  
  # Alert user we are now online
  log.info("The server is ready to receive on port " + str(server_port))
  s_c = []
  
  # Surround with a try-finally to ensure we clean up the socket after we're done
  try:
    # Enter forever loop to listen for requests
    for _ in range(2):
      while globals()['temp'] < 2:
        # When a client connects, create a new socket and record their address
        connection_socket, address = server_socket.accept()
        s_c.append([connection_socket, address])
        log.info("Connected to client at " + str(address))
        # Pass the new socket and address off to a connection handler function
        query = connection_socket.recv(1024)
    
        # Decode data from UTF-8 bytestream
        query_decoded = query.decode()
    
        connection_handler(connection_socket, address, query_decoded)
    for con in s_c:
      # Sent response over the network, encoding to UTF-8
      con[0].send(globals()['response'].encode())
      
      # Close client socket
      con[0].close()
  finally:
    server_socket.close()

if __name__ == "__main__":
  main()
