for x in range(10):
    fir = 4 * 15 ** 3  +  12 * 15 ** 2  +  x * 15  +  4
    sec = x * 13 ** 3  +  6 * 13 ** 2  +  2 * 13  +  10

    if (fir + sec) % 121 == 0:
        print((fir + sec) / 121)