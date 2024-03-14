with open('24.txt') as f:
    x = f.readline()
    maxi = 1
    count = 1
    for i in range(len(x) - 1):
        if x[i] >= x[i + 1]:
            count += 1
        else:
            maxi = max((maxi), count)
            count = 1

    print(maxi)
