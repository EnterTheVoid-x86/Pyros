# Pyros kernel, an operating system made in python
import os
print("Pyros v1.0")
print("Type 'shutdown' to shutdown")
def main():
    try:
     while True:
        line = input("\033[1;34;40m Pyr\033[1;33;40mos$>\033[1;37;40m ")
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
        else:
            print("Unknown command")
    except KeyboardInterrupt:
        print("^C")
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