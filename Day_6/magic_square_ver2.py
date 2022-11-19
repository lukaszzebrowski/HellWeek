def row(matrix):
    row_sum = sum(matrix[0])
    temp = 0
    for i in range(len(matrix)):
        temp = sum(matrix[i])
        if temp != row_sum:
            return False
    return True


def column(matrix):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][0]
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != col_sum:
            return False
    return True


def diagonal(matrix):
    diag_sum = 0
    temp = 0
    count = 0
    for i in range(len(matrix)):
        diag_sum += matrix[i][i]
    for j in range((len(matrix)) - 1, -1, -1):
        temp += matrix[count][j]
        count += 1
    return True if temp == diag_sum else False


def unique_value(matrix):
    first_value = matrix[0][0]
    for i in range(1, len(matrix)):
        for j in range(len(matrix)):
            if first_value == matrix[i][j]:
                return "The numbers in the square are not unique "
    return "The numbers in the square are unique "



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
          f"each column,\nand both main diagonals ar the same and and is equal to: {sum(magic_matrix[0])}\n"
          f"{unique_value(magic_matrix)}")
else:
    print(f"I'm sorry it is not magic square\n{unique_value(magic_matrix)}")


