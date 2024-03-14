def sorting(x, leng):
    """функция сортировки"""
    for i in range(leng):
        for j in range(i, 0, -1):
            if x[j] > x[j - 1]:
                x[j - 1], x[j] = x[j], x[j - 1]
    return x


g = [1, 2, 4, 1, 0, -12, 234, -1234, -546, 34, 1488]
print(sorting(g, len(g)))
