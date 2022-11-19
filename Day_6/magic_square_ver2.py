def row(list):
    row_sum = sum(list[0])
    temp = 0
    for i in range(len(list)):
        temp = sum(list[i])
        if temp != row_sum:
            return False
    return True


def column(list):
    col_sum = 0
    for i in range(len(list)):
        col_sum += list[i][0]
    for i in range(len(list)):
        temp = 0
        for j in range(len(list)):
            temp += list[j][i]
        if temp != col_sum:
            return False
    return True


def diagonal(list):
    diag_sum = 0
    temp = 0
    count = 0
    for i in range(len(list)):
        diag_sum += list[i][i]
    for j in range((len(list)) - 1, -1, -1):
        temp += list[count][j]
        count += 1
    return True if temp == diag_sum else False



file_with_square = open('magic_square_1.txt', 'r', encoding="utf-8")
numbers_square = file_with_square.read()

square_size = len(numbers_square.split('\n'))

numbers_list = list(map(int, ','.join(numbers_square.split('\n')).replace(' ', '').split(',')))

magic_matrix = []

while numbers_list != []:
    magic_matrix.append(numbers_list[:square_size])
    numbers_list = numbers_list[square_size:]


if row(magic_matrix) and column(magic_matrix) and diagonal(magic_matrix):
    print(f"This square:\n\n{numbers_square}\n\nis magic square because the sum of the numbers in each row, "
          f"each column,\nand both main diagonals ar the same and and is equal to: {sum(magic_matrix[0])}")
else:
    print("I'm sorry it is not magic square")
