import os
import platform
print("Pyros Debug Tools v1.0")
print("1. Kernel Panic Pyros")
print("2. Exit")
inp = input(">> ")
if inp == "1":
  print("KERNEL PANIC: Force crash!")
  print("Pyros is shutting down...")
  if platform.system() == "unix":
    os.system("kill -9 python3 > /dev/null")
    os.system("kill -9 py > /dev/null")
  else:
    os.system("taskkill /f /pid py.exe > NUL")
elif inp == "2":
  exit()
  