def hashing(strin):
    p = 67
    m = 10 ** 9 + 9
    p_pow = 1
    ans = 0
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    full = {l: i for i, l in enumerate(alphabet, 1)}
    print(full)
    for i in strin:
        ans = (ans + full[i] * p_pow) % m
        p_pow = (p_pow * p) % m
    return ans


print(hashing('упав'))
