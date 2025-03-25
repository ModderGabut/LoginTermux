import time as t
import os as o
from colorama import Fore, Back, Style
import random as r
from datetime import datetime as dt
import getpass as inv

#colors and variable
pill = (Fore.GREEN + '1. Daftar')
pill1 = (Fore.GREEN + '2. Accaunt List')
pill2 = (Fore.GREEN + '3. Login')
pill3 = (Fore.RED  + '0. Exit' + Fore.RESET)
reset = (Fore.WHITE + Back.RED + 'Reset All (type r to reset)' + Fore.RESET + Back.RESET)
error = (Fore.WHITE + Back.RED + 'incorrent input' + Back.RESET)
error1 = (Fore.RED + Back.WHITE + '.accaunt.txt is empty!')
welcome_sign = (Fore.CYAN + 'Welcome')
loading_wait = list(range(1, 8))
time = dt.now().strftime("%Y-%m-%d %H:%M")

#log file
o.system('clear')
log = open("history.file", "a")
log.write("Masuk system\n")

def saved_accaunt(username, password):
    with open(".accaunt.txt", "a") as file:
          file.write(f"\nUsername: {username}\nPassword: {password}\n")

def sign_accaunt():
  log.write("membuat akun baru\n")
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")
  saved_accaunt(username, password)
  print("Akun berhasil disimpan!")
  t.sleep(1)
  log.write(f"{username} has been saved\n")

def see_accaunt():
  log.write("see an accaunt!\n")
  try:
        with open(".accaunt.txt", "r") as file:
          print(file.read())
          t.sleep(3)
  except FileNotFoundError:
    print(".accaunt.txt is empty!")
    t.sleep(3)

def login():
  log.write("Mencoba untuk sign in\n")
  username = input("Enter username: ")
  password = inv.getpass("Enter password: ")
  with open(".accaunt.txt", "r") as file:
    for line in file:
      if line.strip().startswith("Username: ") and line.strip().endswith(username):
                password_line = next(file)
                if password_line.strip().startswith("Password: ") and password_line.strip().endswith(password):
                    print("Checking... ")
                    t.sleep(3)
                    print("")
                    print("Login berhasil!")
                    print("")
                    print(f"Welcome {username}")
                    print("")
                    #o.system('bash .login.sh')
                    log.write(f"Login Succesfully (Username: {username})\n")
                    exit()
                    break
                    return
    print("Username atau password salah!")
    t.sleep(3)
    log.write("Login Falied\n")

while True:
  o.system('clear')
  o.system('figlet Login Menu | lolcat')
  print(Style.BRIGHT + "")
  print(pill)
  print(pill1)
  print(pill2)
  print(pill3)
  print(reset)
  print("")
  e_g = input("Select Menu: ")
  
  if e_g == "1":
    sign_accaunt()
  elif e_g == "2":
    see_accaunt()
  elif e_g == "3":
    login()
  elif e_g == "0":
    t.sleep(1)
    break
  elif e_g == "r":
    o.system('rm -rf .accaunt.txt')
    log.write("Login.py has been reset!\n")
    break
  elif e_g == "delfil":
    o.system('rm -rf history.file')
    delfill = open("history(.file) has been deleted", "x")
  else:
    print(error)
    t.sleep(3)
