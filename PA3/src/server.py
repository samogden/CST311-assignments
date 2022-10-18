#!env python

"""Chat server for CST311 Programming Assignment 3"""
# __author__ = "Team 1"
# __credits__ = 
#  Shane Cromer , Justin Dick, David Gin, Christopher Cisneros


import threading
import time
import socket as s

# Configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_port = 12000

def connection_handler(connection_socket, address):
  # Read data from the new connectio socket
  #  Note: if no data has been sent this blocks until there is data
  query = connection_socket.recv(1024)
  
  # Decode data from UTF-8 bytestream
  query_decoded = query.decode()
  
  # Log query information
  log.info("Recieved query test \"" + str(query_decoded) + "\"")
  
  # Perform some server operations on data to generate response
  response = query_decoded.upper()
  
  # Sent response over the network, encoding to UTF-8
  connection_socket.send(response.encode())
  
  # Close client socket
  connection_socket.close()
  

def main():
  # Create a TCP socket
  # Notice the use of SOCK_STREAM for TCP packets
  server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
  
  # Assign IP address and port number to socket, and bind to chosen port
  server_socket.bind(('',server_port))
  
  # Configure how many requests can be queued on the server at once
  server_socket.listen(1)
  
  # Alert user we are now online
  log.info("The server is ready to receive on port " + str(server_port))
  
  # Surround with a try-finally to ensure we clean up the socket after we're done
  try:
    # Enter forever loop to listen for requests
    while True:
      # When a client connects, create a new socket and record their address
      connection_socket, address = server_socket.accept()
      log.info("Connected to client at " + str(address))
      # Pass the new socket and address off to a connection handler function
      connection_handler(connection_socket, address)
  finally:
    server_socket.close()

if __name__ == "__main__":
  main()