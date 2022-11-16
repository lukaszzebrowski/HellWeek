def result_compare_max(darek, zdzisiek, edek):
    while darek > 0 or zdzisiek > 0 or edek > 0:
        if max(darek, zdzisiek, edek) == darek:
            return 'Darek'
        elif max(darek, zdzisiek, edek) == zdzisiek:
            return 'Zdzisiek'
        elif max(darek, zdzisiek, edek) == edek:
            return 'Edek'
    return None


def result_compare_min(darek, zdzisiek, edek):
    while darek > 0 or zdzisiek > 0 or edek > 0:
        if min(darek, zdzisiek, edek) == darek:
            return 'Darek'
        elif min(darek, zdzisiek, edek) == zdzisiek:
            return 'Zdzisiek'
        elif min(darek, zdzisiek, edek) == edek:
            return 'Edek'
    return None


file_to_analysis = open('scores.csv', 'r', encoding="utf-8")

text = file_to_analysis.read()

round_count = 1
darek = []
zdzisiek = []
edek = []
score_dict = {}
contest_result = {}


text = text.replace('x', '')

text = ', '.join(text.split('\n')).split(',')

# text[text.index(' ')] = 0 <======= Solution with error in score.csv
# text.remove(' ')

for i in range(len(text) - 1):
    if text[i] == '':
        text[i] = '0'
# delete next 'if' for solution with error
    if text[i] == ' ':
        text[text.index(' ')] = 0

for i in range(3, len(text), 3):
    darek.append(int(text[i]))
for i in range(4, len(text), 3):
    zdzisiek.append(int(text[i]))
for i in range(5, len(text), 3):
    edek.append(int(text[i]))

score_dict['Darek'] = darek
score_dict['Zdzisiek'] = zdzisiek
score_dict['Edek'] = edek

for key in score_dict.keys():
    contest_result[key] = 0

for i in range(len(darek)):
    if result_compare_max(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Darek':
        contest_result['Darek'] += 3

    elif result_compare_max(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Zdzisiek':
        contest_result['Zdzisiek'] += 3

    elif result_compare_max(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Edek':
        contest_result['Edek'] += 3

for i in range(len(darek)):
    if result_compare_min(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Darek':
        contest_result['Darek'] -= 1

    elif result_compare_min(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Zdzisiek':
        contest_result['Zdzisiek'] -= 1

    elif result_compare_min(score_dict['Darek'][i], score_dict['Zdzisiek'][i], score_dict['Edek'][i]) == 'Edek':
        contest_result['Edek'] -= 1


print(contest_result)

