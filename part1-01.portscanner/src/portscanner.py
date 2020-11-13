#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    #error handling
    while min_port <= max_port:
        try:
            con = socket.socket()
            con.connect((address, min_port))
            open_port = min_port
            min_port += 1
        except:
            min_port += 1
        else:
            found_ports.append(open_port)
            print(con.recv(2048))

    return found_ports


def main(argv):
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
                print(p)
# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
