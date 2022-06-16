# Unix shell in Python
import platform
import os
print ("PSH v1.1")
print ("Type 'exit' to exit")
while True:
    line = input(">> ")
    if line == "exit":
        print ("Exiting...")
        exit()
    elif line == "help":
        print ("PSH v1.1 - A basic shell in python.")
        print("Supports any standard unix or windows commands.")
        print("Also comes with a sysinfo script.")
    elif line == "pshinfo":
        print("PSH v1.1")
        print("Running on " + platform.system())
        print("Created by etvx86.")
    else:
        os.system(line)
