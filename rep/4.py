import random
import csv

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'abcdefghijklomnopqrstuvwxz'
c = '0123456789'
all = a + b + c


with open('students.csv', encoding='utf8') as f:
    x = list(csv.reader(f, delimiter=','))[1:]
    ans = []
    for i in x:
        surname, name, lastname = i[1].split()
        login = f'{surname}_{name[0]}{lastname[0]}'
        flag = 0
        while flag == 0:
            c1 = 0
            c2 = 0
            c3 = 0
            passwd = ''.join(random.sample(all, 8))
            for j in passwd:
                if j in a:
                    c1 += 1
                if j in b:
                    c2 += 1
                if j in c:
                    c3 += 1
            if c1 > 0 and c2 > 0 and c3 > 0:
                flag = 1
        temp = i
        temp.append(login)
        temp.append(passwd)
        ans.append(temp)

print(ans)
with open('students_password.csv', 'w', encoding="utf8") as f:
    x = csv.writer(f, delimiter=',')
    x.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    for i in ans:
        x.writerow(i)
