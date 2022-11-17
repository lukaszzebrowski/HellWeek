from typing import List
from random import randint

def f(val: int, digits: List[int]) -> bool:
    return True if val in digits else False

n = 10
example_digits = [randint(-1000, 1000) for _ in range(n)]
chosed_number = False

print('Enter an integer and we will check if it is on the list\n')

while not chosed_number:
    try:
        users_number = int(input('Choose your number:\n'))
        chosed_number = True
    except:
        print('Error!!!!! Enter an integer\n')

if f(users_number, example_digits):
    print(f'congratulations, your number: {users_number} is on the list')
else:
    print(f"I'm sorry, your number: {users_number} is not on the list")