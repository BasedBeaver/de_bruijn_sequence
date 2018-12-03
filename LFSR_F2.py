def xor_func(a, b):
    if not a != (not b):
        x = 1
    else:
        x = 0
    return x

def and_func(a, b):
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



res = [0, 1, 0, 0]
res_NL = [0, 1, 0, 0]
while len(res) < 16:
    s1, s2 = res[-4], res[-3]
    f = f_func(s1, s2)
    res.append(f)
    c1, c2, c3 = res[-4], res[-3], res[-2]
    if c1 == 0 and c2 == 0 and c3 == 0:
        res_NL.append(0)
    res_NL.append(f)
    print("-----------")
if (res[1] == 0 and res[2] == 0 and res[-1] == 0) or\
        (res[1] == 0 and res[-2] == 0 and res[-1] == 0):
    res_NL.append(0)
print(res)
print(res_NL)
print(len(res), len(res_NL))

