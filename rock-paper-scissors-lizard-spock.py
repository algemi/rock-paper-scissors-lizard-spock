import random

computer_wins = 0
player_wins = 0
ties = 0

print('')
print('Welcome to the game rock-paper-scissors-lizard-spock.')
print('If you want to play press:')
print('1 for Rock')
print('2 for Paper')
print('3 for Scissors')
print('4 for Lizard')
print('5 for Spock')

def User_Option():
    user_option = input('Choose option (1,2,3,4,5): ')
    if user_option in ['1', 'Rock', 'rock', 'R', 'r']:
        user_option = '1'
    elif user_option in ['2', 'Paper', 'paper', 'P', 'p']:
        user_option = '2'
    elif user_option in ['3', 'Scissors', 'scissors', 'S', 's']:
        user_option = '3'
    elif user_option in ['4', 'Lizard', 'lizard', 'L', 'l']:
        user_option = '4'
    elif user_option in ['5', 'Spock', 'spock', 'Sp', 'sp']:
        user_option = '5'
    else:
        print('Invalid. Try again.')
        User_Option()
    return user_option

def Computer_Option():
    computer_option = random.randint(1,5)
    if computer_option == 1:
        computer_option = '1'
    elif computer_option == 2:
        computer_option = '2'
    elif computer_option == 3:
        computer_option = '3'
    elif computer_option == 4:
        computer_option = '4'
    elif computer_option == 5:
        computer_option = '5'
    return computer_option

while True:
    user_option = User_Option()
    computer_option = Computer_Option()

    if user_option == '1':
        if computer_option == '1':
            print('player: rock, computer: rock. You tied.')
            ties += 1
        elif computer_option == '2':
            print('player: rock, computer: paper. You lose.')
            print('"Paper covers Rock."')
            computer_wins += 1
        elif computer_option == '3':
            print('player: rock, computer: scissors. You win.')
            print('"Rock crushes Scissors."')
            player_wins += 1
        elif computer_option == '4':
            print('player: rock, computer: lizard. You win.')
            print('"Rock crushes Lizard."')
            player_wins += 1
        elif computer_option == '5':
            print('player: rock, computer: spock. You lose.')
            print('"Spock vaporizes Rock."')
            computer_wins += 1

    elif user_option == '2':
        if computer_option == '1':
            print('player: paper, computer: rock. You win.')
            print('"Paper covers Rock."')
            player_wins += 1
        elif computer_option == '2':
            print('player: paper, computer: paper. You tied.')
            ties += 1
        elif computer_option == '3':
            print('player: paper, computer: scissors. You lose.')
            print('"Scissors cuts Paper."')
            computer_wins += 1
        elif computer_option == '4':
            print('player: paper, computer: lizard. You lose.')
            print('"Lizard eats Paper."')
            computer_wins += 1
        elif computer_option == '5':
            print('player: paper, computer: spock. You win.')
            print('"Paper disproves Spock."')
            player_wins += 1

    elif user_option == '3':
        if computer_option == '1':
            print('player: scissors, computer: rock. You lose.')
            print('"Rock crushes Scissors."')
            computer_wins += 1
        elif computer_option == '2':
            print('player: scissors, computer: paper. You win.')
            print('"Scissors cuts Paper."')
            player_wins += 1
        elif computer_option == '3':
            print('player: scissors, computer: scissors. You tied.')
            ties += 1
        elif computer_option == '4':
            print('player: scissors, computer: lizard. You win.')
            print('"Scissors decapitates Lizard."')
            player_wins += 1
        elif computer_option == '5':
            print('player: scissors, computer: spock. You lose.')
            print('"Spock smashes Scissors."')
            computer_wins += 1

    elif user_option == '4':
        if computer_option == '1':
            print('player: lizard, computer: rock. You lose.')
            print('"Rock crushes Lizard."')
            computer_wins += 1
        elif computer_option == '2':
            print('player: lizard, computer: paper. You win.')
            print('"Lizard eats Paper."')
            player_wins += 1
        elif computer_option == '3':
            print('player: lizard, computer: scissors. You lose.')
            print('"Scissors decapitates Lizard."')
            computer_wins += 1
        elif computer_option == '4':
            print('player: lizard, computer: lizard. You tied.')
            ties += 1
        elif computer_option == '5':
            print('player: lizard, computer: spock. You win.')
            print('"Lizard poisons Spock"')
            player_wins += 1

    elif user_option == '5':
        if computer_option == '1':
            print('player: spock, computer: rock. You win.')
            print('"Spock vaporizes Rock."')
            player_wins += 1
        elif computer_option == '2':
            print('player: spock, computer: paper. You lose.')
            print('"Paper disproves Spock."')
            computer_wins += 1
        elif computer_option == '3':
            print('player: spock, computer: scissors. You win.')
            print('"Spock smashes Scissors."')
            player_wins += 1
        elif computer_option == '4':
            print('player: spock, computer: lizard. You lose.')
            print('"Lizard poisons Spock."')
            computer_wins += 1
        elif computer_option == '5':
            print('player: spock, computer: spock. You tied.')
            ties += 1

    print('')
    print('player wins: ' + str(player_wins))
    print('computer wins: ' + str(computer_wins))
    print('ties: ' + str(ties))
    print('')

    user_option = input('Play again? (yes/no) ')
    if user_option in ['yes', 'Yes', 'y', 'Y', '1', '2', '3', '4', '5', '']:
        pass
    elif user_option in ['No', 'no']:
        break
    else:
        break
