from random import choice

print('''\t\t\t\t\tWELCOME IN MY GAME
    \t Computer choose a number between 1 and 256
    \t\tCan you guess which one he choose?
    \t\t\t\t\tGOOD LUCK
''')

while True:
    looking_number = choice(range(1, 257))
    finded_number = False

    while not finded_number:
        try:
            players_number = int(input("Choose your number: "))
        except ValueError:
            print("Error!!!! Use integer number.")
            print()
            continue

        if looking_number > players_number:
            print('Too small number!!! Try again.')
            print()
        elif looking_number < players_number:
            print('Too big number!!! Try again.')
            print()
        else:
            print(f'Congratulations!!!!! {looking_number} was correct answer.')
            print()
            finded_number = True

    players_choice = input('Play again? Write "YES" to play again, press any key to exit')

    if players_choice.upper() == 'YES':
        continue
    else:
        break
