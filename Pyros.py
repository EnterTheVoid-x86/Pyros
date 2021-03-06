# Pyros kernel, an "operating system" made in python
# Created by EnterTheVoid-x86, (C) 2022
# Using only python standard libraries
passwd = "pyros"
import os
PATH = os.getcwd()
print("Pyros v1.3")
print("Type 'shutdown' to shutdown")
import time
import platform
t = time.localtime()
current_time = time.strftime("%I:%M", t)
print("The time is: "+ current_time)
def password():
    passprompt = input("Please enter your password: >> ")
    if passprompt == passwd:
      print("Welcome to Pyros.")
      main()
    else:
      print("Wrong password.")
      password()
def main():
    try:
     while True:
        line = input("\033[1;34;40mPyr\033[1;33;40mos$>\033[1;37;40m ")
        if line == "shutdown":
            print("Shutting down...")
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
            print("mkdir - create a directory")
            print("rm - delete a directory or file")
            print("clock - open a clock")
            print("clear - clear the screen")
            print("PyrosDebugTools - self explanitory.")
            print("moduleloader - load a module")
            print("sysinfo - small system info script")
            print("shutdown - shutdown Pyros")
        elif line == "calculator":
            calculator()
        elif line == "loader":
            loader()
        elif line == "cd":
            print("Enter the name of the directory to change to: ")
            line4 = input(">> ")
            os.chdir(line4)
        elif line == "ls":
            print(os.listdir())
        elif line == "colorlist":
            exec(open(PATH + "/colorlist.py").read())
        elif line == "numberguess":
            exec(open(PATH + "/numberguess.py").read())
        elif line == "psh":
            exec(open(PATH + "/PyShell.py").read())
        elif line == "touch":
            print("Enter file name to create:")
            filename = input(">> ")
            open(filename, "x")
        elif line == "clock":
            os.system("cls")
            os.system("clear")
            exec(open(PATH + "/clock.py").read())
        elif line == "clear":
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
        elif line == "PyrosDebugTools":
            exec(open(PATH + "/debug.py").read())
        elif line == "moduleloader":
            print("Enter the name of the module to load: ")
            line5 = input(">> ")
            import importlib
            importlib.import_module(line5)
        elif line == "sysinfo":
          print("Pyros v1.3")
          print("Running on " + platform.system())
          print("Created by etvx86")
          os.system("uptime")
          mem_bytes = os.sysconf('SC_PAGE_SIZE') *     os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
          mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74
          print(mem_gib, "gigabytes of memory")
          os.system("cat ascii.txt")
          print("\n")
        elif line == "mkdir":
          mkdir = input("Enter directory name to be created: >> ")
          os.mkdir(mkdir)
        elif line == "rm":
          rm = input("Enter file or folder name to be deleted: >> ")
          if platform.system() == "Windows":
            os.system("del " + rm)
          else:
            os.system("rm -rf " + rm)
        else:
            print("Command not recognized.")
    except KeyboardInterrupt:
            print("KeyboardInterrupt")
            main()
    except EOFError:
            print("^DEOFAttempt")
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
password()