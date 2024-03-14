for i in range(201, 300):
    x = '1' * i
    while '1111' in x:
        x = x.replace('1111', '22', 1)
        x = x.replace('222', '1', 1)
    print(x, i)
