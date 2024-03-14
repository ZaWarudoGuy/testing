h = []
for a in range(10):
    for b in range(10):
        x = int(f'1293{a}1{b}')
        if x % 3127 == 0:
            h.append(x)

for i in range(10):
    for a in range(10):
        for b in range(10):
            x = int(f'12{i}93{a}1{b}')
            if x % 3127 == 0:
                h.append(x)

for j in range(10):
    for i in range(10):
        for a in range(10):
            for b in range(10):
                x = int(f'12{i}{j}93{a}1{b}')
                if x % 3127 == 0:
                    h.append(x)

print(sorted(h))
