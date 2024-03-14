import csv


def sorting(listik, length):
    for i in range(1, length):
        for j in range(i, 0, -1):
            if listik[j][-1] > listik[j - 1][-1]:
                listik[j], listik[j - 1] = listik[j - 1], listik[j]
            else:
                break
    return listik


with open('students.csv', encoding='utf8') as f:
    x = list(csv.reader(f, delimiter=','))[1:]
    ans = sorting(x, len(x))
    count = 1
    print('10 класс')
    print()
    for i in ans:
        if count == 4:
            break
        if i[-1] != 'None' and i[-2][:2] == '10':
            surname, name, lastname = i[1].split()
            print(f'{count} место: {name[0]}.{surname}')
            print()
            count += 1
