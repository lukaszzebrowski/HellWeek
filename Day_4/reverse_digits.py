from time import sleep
correct_number = False

print("I'm tired, just give me a number and I will revers it\n")
sleep(3)
while not correct_number:
    try:
        user_number = int(input("Come on, what are you waiting for? Give me your number:"))
        correct_number = True
    except ValueError:
        print("Ehhhh integer, enter integer, didn't I say?\n")
        sleep(3)

revers_number = 0
temp = user_number

while user_number > 0:
    reszta = user_number % 10
    revers_number = revers_number * 10 + reszta
    user_number = user_number // 10

if temp % 10 != 0:
    print(f'Your reverse number: {revers_number}\n')
else:
    print(f'Your reverse number: {str(temp)[::-1]}')
    print(f'But i think number: {str(temp)[::-1]} is not exist, so your number is just: {revers_number}')
