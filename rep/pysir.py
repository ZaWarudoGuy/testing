def sorting(x, leng):
    for i in range(leng):
        for j in range(0, leng - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


s = [0, 1, 2, -10, 234, 20, 12, -123]

print(sorting(s, len(s)))