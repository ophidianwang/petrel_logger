# -*- coding: utf-8 -*-

# Server program
# UDP VERSION

import re
from datetime import datetime
from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM

# Set the socket parameters
host = "172.28.128.22"
port = 514
buf = 1024
addr = (host, port)
log_path = "/realtime/storm_log/storm_petrel_{0}_{1}.log"

# Create socket and bind to address
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while 1:
    data, addr = UDPSock.recvfrom(buf)
    if not data:
        continue
    else:
        line = str(data)
        with open("/realtime/storm_log/test.log", "a") as log_file:
            log_file.write("{0}\n".format(line))

        match = re.search(r"^<.*>\[.*\]\[(.*)\]\[.*\]", line)
        with open(log_path.format(match.group(1), datetime.now().strftime("%Y%m%d")), "a") as log_file:
            try:
                print("\nReceived message '{0}'".format(line))
                log_file.write("{0}\n".format(line))
            except:
                print("something wrong")
                log_file.write("something wrong\n")
# Close socket
UDPSock.close()
