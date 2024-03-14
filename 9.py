import csv

with open('9.csv') as f:
    x = csv.reader(f, delimiter=';')
    count = 0
    for i in x:
        h = sorted(list(map(int, i)))
        if (h[0] * 6) < (h[1] + h[2] + h[3]):
            if (h[0] * h[-1]) > (h[1] * h[2]):
                count += 1
    print(count)
