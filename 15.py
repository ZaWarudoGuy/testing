for A in range(1000):
    count = 0
    for x in range(1000):
        if ((x & 28 !=0) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & A != 0)):
            count += 1

    if count == 1000:
        print(A)
        break
