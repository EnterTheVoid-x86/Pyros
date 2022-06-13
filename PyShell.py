# Unix shell in Python
import sys
import os
print ("PSH v1.0")
print ("Type 'exit' to exit")
user = os.getlogin()
while True:
    line = input("{}@PSH:~$ ".format(user))
    if line == "exit":
        print ("Exiting...")
        break
    else:
        os.system(line)
