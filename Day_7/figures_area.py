def figures(dict):
    for key in dict:
        if key == 'kwadrat':
            print(square(dict[key]))
        elif key == 'trojkat':
            print(triangle(dict[key]))


def square(list):
    for i in range(len(list)):
        return list[i] ** 2


def triangle(list):
    return 1/2 * list[0] * list[1]



def trapeze(a, b, h):
    pass


def circle(r):
    pass


file_with_data = open('figures.txt', 'r', encoding="utf-8")

figures_str = file_with_data.read()

figures_list = figures_str.split('\n')

figures_with_value = []

for element in figures_list:
    figures_with_value.append(element.split(','))

figures_dict = {}

for i in range(len(figures_with_value)):
    figures_dict[figures_with_value[i][0]] = figures_with_value[i][1:]

for string in figures_dict:
    figures_dict[string] = list(map(int, figures_dict[string]))

figures(figures_dict)


