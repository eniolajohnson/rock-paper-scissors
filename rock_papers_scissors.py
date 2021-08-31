import random

def play():
  print("Choose your destiny!\n", "select 'r' for rock, 'p' for paper, 's' for scissors")
  user = input()
  computer = random.choice(['r', 'p', 's'])

