import os
print("Pyros Debug Tools v1.0")
print("1. Kernel Panic Pyros")
print("2. Exit")
inp = input(">> ")
if inp == "1":
  print("KERNEL PANIC: Force crash!")
  os.system("killall python3")
  os.system("killall python")
  os.system("killall py")
  