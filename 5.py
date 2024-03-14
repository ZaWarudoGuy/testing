for x in range(10000, 1000, -1):
    r = str(x)
    fir = int(r[0]) + int(r[1])
    sec = int(r[1]) + int(r[2])
    thi = int(r[2]) + int(r[3])
    h = []
    h.append(fir)
    h.append(sec)
    h.append(thi)
    h = sorted(h)
    j = str(h[-1]) + str(h[-2])
    if j =='1515':
        print(x)
