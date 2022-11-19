def magic_square_sum(list):
    if sum(list[0:3:1]) == sum(list[3:6:1]) == sum(list[6:9:1]):
        if sum(list[0:9:3]) == sum(list[1:9:3]) == sum(list[2:9:3]):
            if sum(list[0:9:4]) == sum(list[-1::-4]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

square_size = 3

file_with_square = open('magic_square_1.txt', 'r', encoding="utf-8")
numbers_square = file_with_square.read()

numbers_list = list(map(int, ','.join(numbers_square.split('\n')).replace(' ', '').split(',')))

if magic_square_sum(numbers_list) == True:
    print(f"This square:\n\n{numbers_square}\n\nis magic square because the sum of the numbers in each row, "
          f"each column,\nand both main diagonals ar the same and and is equal to: {sum(numbers_list[0:3:1])}")
else:
    print("I'm sorry it is not magic square")



