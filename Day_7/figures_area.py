import math

def figures(dict):
    count = 0
    medium_field = 0
    for key in dict:
        if key == 'kwadrat':
            print(f'Square area = {round(square(dict[key]), 2)}')
            count += 1
            medium_field += square(dict[key])
        elif key == 'trojkat':
            print(f'Triangle area = {round(triangle(dict[key]), 2)}')
            count += 1
            medium_field += triangle(dict[key])
        elif key == 'trapez':
            print(f'Trapeze area = {round(trapeze(dict[key]), 2)}')
            count += 1
            medium_field += trapeze(dict[key])
        elif key == 'kolo':
            print(f'Cyrcle area = {round(circle(dict[key]), 2)}')
            count += 1
            medium_field += circle(dict[key])
        else:
            return f'We cannot calculate the area of this figure {key}'
    print(f'Medium field of all figures = {round(medium_field / count, 2)}')


def square(list):
    return list[0] ** 2


def triangle(list):
    return 1/2 * list[0] * list[1]



def trapeze(list):
    return ((list[0] + list[1]) / 2) * list[2]


def circle(list):
    return round(math.pi * pow(list[0], 2), 2)


file_with_data = open('figures.txt', 'r', encoding="utf-8")

figures_str = file_with_data.read()

figures_list = figures_str.split('\n')

figures_with_value = []

for element in figures_list:
    figures_with_value.append(element.split(','))

figures_dict = {}

for i in range(len(figures_with_value)):
    figures_dict[figures_with_value[i][0]] = list(map(int, figures_with_value[i][1:]))

print(figures(figures_dict))










