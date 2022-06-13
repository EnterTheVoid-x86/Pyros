# Unix shell in Python
import sys
import os
print ("PSH v1.0")
print ("Type 'exit' to exit")
while True:
    line = input(">> ")
    if line == "exit":
        print ("Exiting...")
        exit()
    else:
        os.system(line)
