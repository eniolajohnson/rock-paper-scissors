import random

def play():
  print("Choose your destiny!\n", "select 'r' for rock, 'p' for paper, 's' for scissors")
  user = input()
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return "Your opponent chose", computer, 'so it\'s a tie!'
  
  if you_won(user, computer):
    return "Won! you rock!"
  
  if you_won(computer, user):
    return "Your opponent chose", computer, "better luck next time!"
  # return "Better luck next time!"
  
def you_won(player, comp):
  if (player == 'r' and comp == 's') \
    or (player == 'p' and comp == 'r') \
    or (player == 's' and comp == 'p'):
    return True

print(play())
