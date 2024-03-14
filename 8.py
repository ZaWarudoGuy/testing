count = 1
for a in 'НРТУ':
    for b in 'НРТУ':
        for c in 'НРТУ':
            for d in 'НРТУ':
                g = a + b + c + d
                print(g, count)
                if count == 215:
                    print(g)
                count += 1
