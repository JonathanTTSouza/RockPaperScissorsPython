'''
Rock paper scissors game in python
'''
import random

# welcome statement
print('Welcome to Rock Paper Scissors!')

while True:
    print('----------------------------')
    # ask user for rock paper or scissors and check if it's a valid input
    try:
        choice = input('\nMake your choice! Type r for rock, p for paper or s for scissors\n').lower()
        player_dict = {'r':'rock', 'p':'paper', 's':'scissors'}
        choice = player_dict[choice]
    except:
        print('Invalid input')
        continue

    # randomize computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # draw check
    if (choice == 'rock' and computer_choice == 'rock') or (choice == 'paper' and computer_choice == 'paper') or (choice == 'scissors' and computer_choice == 'scissors'):
        print('You chose {}'.format(choice))
        print('The computer chose: {}\nDraw!'.format(computer_choice))

    # player wins check
    elif (choice == 'rock' and computer_choice == 'scissors') or (choice == 'paper' and computer_choice == 'rock') or (choice == 'scissors' and computer_choice == 'paper'):
        print('You chose {}'.format(choice))
        print('The computer chose: {}\nYou win!'.format(computer_choice))

    # player loses check
    elif (choice == 'rock' and computer_choice == 'paper') or (choice == 'paper' and computer_choice == 'scissors') or (choice == 'scissors' and computer_choice == 'rock'):
        print('You chose {}'.format(choice))
        print('The computer chose: {}\nYou lose!'.format(computer_choice))
