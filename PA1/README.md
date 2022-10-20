# Programming Assignment 1
## CST 311, Introduction to Computer Networks

READ INSTRUCTIONS CAREFULLY BEFORE YOU START THE ASSIGNMENT.

Assignment must be submitted electronically to [Canvas](https://csumb.instructure.com/) by 11:59 p.m. on the due date.  
Late assignments will not be accepted.

Use the Teams on the Programming Assignment Teams document (also on Canvas under General Information -> Team Information)
Select your Team leader and divide up work per the Programming Process instructions (also on Canvas under General Information > Team Information.)

## Assignment Goals

The goal of this assignment is threefold.
1. Help you get to know your team
2. Help improve your ability to read python code
3. Help ensure that your environment is set up

In light of these goals please select your team leader and divide up work per the Programming Process instructions (also on Canvas under General Information → Team Information).
Also, please ensure that you have followed the steps in Lab1 to set up your mininet VM and programming environment.

## Instructions

### Overview

In this assignment, you will learn the basics of socket programming for UDP and TCP in Python. 
You will learn how to send and receive datagram packets using UDP sockets and TCP sockets. 
Throughout the assignment, you will gain familiarity with a Client Server architecture, as well as with python code and working in the mininet environment.

This assignment requires you to execute the Python client and server code for the UDP socket programming example in Section 2.7.1 and then also the TCP socket programming example in Section 2.7.2 within the mininet environment.
Note, these scripts should be run in mininet, not just within the mininet VM.

The goals of this assignment are:
 - To learn about how UDP and TCP works and how to program with UDP and TCP and also
 - To make sure your computer is set up and working, ready for the next assignment where you will be writing your own code.

### Specific Tasks

#### Team Tasks

There are a few steps to getting your team organized.
First, pick a team leader for this project.
They will be responsible for running meetings as well as the final submission.

Next, split up your team to have one group do the UDP example together and another group to do the TCP example.
While these teams can work independently, there is a fair bit of overlap in their roles, and communication between them, so keeping this communication going would be beneficial.

Third, At least once have a meeting where all team members look over all the code together to help understand what it is doind and any changes that were necessary.

#### IDE Configuration
You are welcome to use whatever IDE the team prefers; for this assignment with about 10 lines of code, you may prefer to simply use an editor but this is up to you.

#### Code tasks

The goal of these client-server connections is to have the client send a request to the server, either via TCP or UDP, and the server will convert it to uppercase.
For example, if the client sends the string "hello!" to the server then the server should send back a message with the string "HELLO!"

A few more examples of inputs and outputs would be the strings:
```
abcdef abc123def
ABcdEF
AB12cdEF
Two Words HERE !!
```

Would be converted by the server to:
```
ABCDEF ABC123DEF
ABCDEF
AB12CDEF
TWO WORDS HERE !!
```

Started code can be found in the [src](src) directory.
This code is for python3 and should be able to run unchanged on your local machine.
However, to get it working within mininet will require some modifications.



#### Example Output

```shell
mininet-vm% sudo mn
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2
*** Adding switches:
s1
*** Adding links:
(h1, s1) (h2, s1)
*** Configuring hosts
h1 h2
*** Starting controller
c0
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet> h1 python3 udp_server.py &
mininet> h2 python3 udp_client.py
Input lowercase sentence: hello
HELLO

```



## Grading
This assignment is worth 100 points. The grading objectives for the assignment are given below.
Grading Objectives
- [ ] Coding Grades
  - For UDP (30 points)
    - [ ] (5 points) Socket set up correctly on server
    - [ ] (5 points) Socket set up correctly on client
    - [ ] (5 points) Server waits for input
    - [ ] (5 points) Client sends message to server
    - [ ] (5 points) Server takes input and changes it to all CAPS
    - [ ] (5 points) Client receives and prints out the modified message.
  - For TCP (30 points)
    - [ ] (5 points) Socket set up correctly on server
    - [ ] (5 points) Socket set up correctly on client
    - [ ] (5 points) Server waits for input
    - [ ] (5 points) Client sends message to server
    - [ ] (5 points) Server takes input and changes it to all CAPS
    - [ ] (5 points) Client receives and prints out the modified message.
- [ ] Documentation Grades
  - [ ] (10 points) All screenshots in one pdf file. Include one Minutes of meeting pdf file.
- [ ] Teamwork grade:
  - [ ] (30 points) Each team member will grade each other teammate out of 4 points during peer evaluation. 
    - I will average all team members’ grades and scale it to get your teamwork grade out of 30 points. 
    - Note that 30% of your grade will come from your teamwork and team member evaluations.

### What to Hand in

Since the code is already given, you need not submit python files for this assignment. 
You will hand in the following:
- Screenshots of the working UDP and TCP client/server programs for all test cases given above.
- Minutes of meeting including: Team Lead name, attendance, work division narrative (1-2 lines is good enough).
- You must also fill in the peer evaluation form for teamwork grade. 

