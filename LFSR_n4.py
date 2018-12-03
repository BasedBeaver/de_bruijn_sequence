def xor_func(a, b):
    x = 0
    if not a != (not b):
        x = 1
    else:
        x = 0
    return x

def and_func(a, b):
    x = 0
    if a and b:
        x = 1
    else:
        x = 0
    return x


def f_func(s1, s2):
    return xor_func(s1, s2)

print("########################")
print(f_func(0, 0))
print(f_func(0, 0))
print(f_func(0, 1))
print(f_func(0, 1))
print(f_func(1, 0))
print(f_func(1, 0))
print(f_func(1, 1))
print(f_func(1, 1))
print("########################")



res = [1, 0, 1, 0]
res_NL = res
while len(res) < 18:
    s1, s2 = res[-4], res[-3]
    print(s1, s2)
    f = f_func(s1, s2)
    res.append(f)
    res_NL.append(f)
    c1, c2, c3 = res[-3], res[-2], res[-1]
    if c1 and c2 and c3 == 0:
        res_NL.append(0)
    print("-----------")
print(res)
print(res_NL)
