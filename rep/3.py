import csv


with open('students.csv', encoding='utf8') as f:
    dump = list(csv.reader(f, delimiter=','))[1:]


x = input()
while x != 'СТОП':
    for i in dump:
        if i[-3] == x:
            surname, name, lastname = i[1].split()
            print(f'Проект № {i[-3]} делал: {name[0]}.{surname} он(а) получил(а) оценку - {i[-1]}')
            break
    else:
        print('Ничего не найдено.')
    x = input()
