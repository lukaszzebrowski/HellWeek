file_to_analysis = open('content.txt', 'r', encoding="utf-8")

text = file_to_analysis.read()

print('''
Welcome to the text analysis program.
We will show an analysis of a sample text.
''')

print('Our sample text:\n')
print(text, '\n')

print('Now we will show lines only containing the word "Python"\n')
print('Are you ready?\n')
input('Press "enter" to continue\n')

for opinion in text.lower().split('\n'):
    if 'python' in opinion:
        print(opinion.capitalize())

print('\nAs you can see, the second line is missing. So everything worked fine.\n')
print('Now my dear friend, we need your help.\n')
print('We only want to display words starting with the letter you specify.\n')
print('What letter will you choose?\n')

while True:
    selected_letter = input('Enter your letter: \n')

    word_list = []

    for wyraz in text.split():
        if wyraz.startswith(selected_letter.lower()) or wyraz.startswith(selected_letter.upper()):
            print(wyraz, '\n')
            word_list.append(wyraz)

    if len(word_list) == 0:
        print(f"Sorry, we couldn't find a word starting with: '{selected_letter}'\n")


    user_selection = input('\nType "quit" to exit or enter to choose another letter\n')

    if user_selection.lower() == 'quit':
        break

print('\nThank you for participating in the presentation and we invite you again')
print('Have a nice day!!!!')







