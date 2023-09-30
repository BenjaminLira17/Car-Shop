import time
from os import system

def navegation(prompt, length):
  nav = input(prompt)
  if length == 2:
    while nav not in ("1", "2"):
      nav = input(prompt)
  elif length == 3:
    while nav not in ("1", "2", "3"):
      nav = input(prompt)
  elif length == 4:
    while nav not in ("1", "2", "3", "4"):
      nav = input(prompt)
  return nav

def delay(seg):
  time.sleep(seg)

def advance():
  input("\nPresione Enter para continuar")

def cl():
    system('cls')
