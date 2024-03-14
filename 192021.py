def f(x, m, a=0, b=0, c=0):
    if x >= 50: return m % 2 == 0
    if m == 0: return 0
    if a == 1:
        h = [f(x + 2, m - 1), f(x * 2, m - 1)]
    if b == 1:
        h = [f(x + 1, m - 1), f(x * 2, m - 1)]
    if c == 1:
        h = [f(x + 1, m - 1), f(x + 2, m - 1)]
    if a == 0 and b == 0 and c == 0:
        h = [f(x * 2, m - 1, 0, 0, 1), f(x + 1, m - 1, 1, 0, 0), f(x + 2, m - 1, 0, 1, 0)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


for i in range(1, 50):
    if (not(f(i, 1))) and (f(i, 2)):
        print(i)

print()

for i in range(1, 50):
    if (not(f(i, 1))) and (f(i, 3)):
        print(i)

print()

for i in range(1, 50):
    if (not(f(i, 2))) and (f(i, 4)):
        print(i)
