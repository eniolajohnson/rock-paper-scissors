import random

def play():
  print("Choose your destiny!\n", "select 'r' for rock, 'p' for paper, 's' for scissors")
  user = input()
  computer = random.choice(['r', 'p', 's'])

  
def you_won(player, comp):
  if (player == 'r' and comp == 's') \
    or (player == 'p' and comp == 'r') \
    or (player == 's' and comp == 'p'):
    return True

