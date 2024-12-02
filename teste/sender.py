
import socket
import sys
import os

def main(target, filename):
    port = 443
    buffersize = 50000

    file = open(filename, 'rb')
    
    print("[+] Starting File Transfer!")
    
    for i in range (0,100):
        data = file.read(buffersize)
        s = socket.socket()
        source_port = 1025 + i
        s.bind(('0.0.0.0', source_port))
        s.connect((target, port))
        print("[+] Connected to the target...")
        s.sendall(data)
        print("[+] Data sent")
        s.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

# sender.py <dst_ip> <filename>
