# Pyros kernel, an operating system made in python
# Created by EnterTheVoid-x86, (C) 2022
# Using only python standard libraries
import os
print("Pyros v1.1")
print("Type 'shutdown' to shutdown")
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("The time is: "+ current_time)
def main():
    try:
     while True:
        line = input("\033[1;34;40mPyr\033[1;33;40mos$>\033[1;37;40m ")
        if line == "shutdown":
            print("Exiting...")
            break
        elif line == "help":
            print("help - This help menu")
            print("calculator - simple calculator")
            print("loader - load a program")
            print("cd - change directory")
            print("ls - list files")
            print("colorlist - list colors")
            print("numberguess - number guessing game")
            print("psh - Unix shell")
            print("touch - create a file")
            print("clock - open a clock")
            print("clear - clear the screen")
            print("PyrosDebugTools - self explanitory.")
            print("shutdown - shutdown Pyros")
        elif line == "calculator":
            calculator()
        elif line == "shutdown":
            exit()
        elif line == "loader":
            loader()
        elif line == "cd":
            print("Enter the name of the directory to change to: ")
            line4 = input(">> ")
            os.chdir(line4)
        elif line == "ls":
            print(os.listdir())
        elif line == "colorlist":
            exec(open("colorlist.py").read())
        elif line == "numberguess":
            exec(open("numberguess.py").read())
        elif line == "psh":
            exec(open("PyShell.py").read())
        elif line == "touch":
            print("Enter file name to create:")
            filename = input(">> ")
            open(filename, "x")
        elif line == "clock":
            exec(open("clock.py").read())
        elif line == "clear":
            os.system("clear")
        elif line == "PyrosDebugTools":
            exec(open("debug.py").read())
        else:
            print("Unknown command")
    except KeyboardInterrupt:
            print("KeyboardInterrupt")
            main()
def calculator():
# Calculator in python
            print("Type 'exit' to exit")
            while True:
                line2 = input(">> ")
                if line2 == "exit":
                    print("Exiting...")
                    main()
                else:
                    print(eval(line2))
def loader():
# Load a program in python
    print("Enter the name of the program to load or type exit: ")
    line3 = input(">> ")
    if line3 == "exit":
        print("Exiting...")
        main()
    else:
        exec(open(line3).read())
main()