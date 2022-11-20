from random import randint

print('''\t\t\t\t\tWELCOME IN MY GAME
    \t Computer choose a number between 1 and 256
    \t\tCan you guess which one he choose?
    \t\t\t\t\tGOOD LUCK
''')

while True:
    looking_number = randint(1, 257)
    finded_number = False

    while not finded_number:
        try:
            players_number = int(input("Choose your number: "))
        except ValueError:
            print("Error!!!! Use integer number.", end='\n\n')
            continue

        if looking_number > players_number:
            print('Too small number!!! Try again.', end='\n\n')
        elif looking_number < players_number:
            print('Too big number!!! Try again.', end='\n\n')
        else:
            print(f'Congratulations!!!!! {looking_number} was correct answer.', end='\n\n')
            finded_number = True

    players_choice = input('Play again? Write "YES" to play again, press any key to exit')

    if players_choice.upper() == 'YES':
        continue
    else:
        break
