import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_opc = input('piedra, papel o tijera => ').lower()
  
  if not user_opc in options:
    print('Esa opcion no es valida')
    #continue
    return None, None
  
  computer_opc = random.choice(options)

  print('User option => ', user_opc)
  print('Computer option => ', computer_opc)
  return user_opc, computer_opc

def check_rules(user_opc, computer_opc, user_wins, computer_wins):
  if user_opc == computer_opc:
    print('Empate!')
  elif user_opc == 'piedra' and computer_opc == 'tijera':
      print(f'{user_opc} gana {computer_opc}')
      print('User gano!')
      user_wins += 1
  elif user_opc == 'papel' and computer_opc == 'piedra':
      print(f'{user_opc} gana {computer_opc}')
      print('User gano!')
      user_wins += 1
  elif user_opc == 'tijera' and computer_opc == 'papel':
      print(f'{user_opc} gana {computer_opc}')
      print('User gano!')
      user_wins += 1
  else:
    print(f'{computer_opc} gana {user_opc}')
    print('Computer gana!')
    computer_wins += 1
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if user_wins == 3:
    print('El ganador es el usuario')
    exit()
  elif computer_wins == 3:
    print('El ganador es la computadora')
    exit()
    

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
  
    print('*' *10)
    print('ROUND', rounds)
    print('*' *10)
    print(f'MARCADOR\nUSER {user_wins} - COMPUTER {computer_wins}')
    print('*' *10)
    
    rounds +=1 
  
    user_opc, computer_opc = choose_options()
    user_wins, computer_wins=check_rules(user_opc, computer_opc, user_wins, computer_wins)
    check_winner(user_wins, computer_wins)

run_game()