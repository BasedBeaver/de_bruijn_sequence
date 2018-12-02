
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


def f_func(s_1, s_2, s_3):
    res = xor_func(xor_func(and_func(s_1, s_2), s_1), s_3)
    return res

print("########################")
print(f_func(0, 0, 0))
print(f_func(0, 0, 1))
print(f_func(0, 1, 0))
print(f_func(0, 1, 1))
print(f_func(1, 0, 0))
print(f_func(1, 0, 1))
print(f_func(1, 1, 0))
print(f_func(1, 1, 1))
print("########################")


res = [0, 1, 0]
res2 = [2, 3, 4]
print(res2[-1], res2[-2], res2[-3])
print(res)
while len(res) < 12:
    s1, s2, s3 = res[-1], res[-2], res[-3]
    print(s1, s2, s3)
    f = f_func(s1, s2, s3)
    res.append(f)
    print(res[-1])
    print("-----------")
print(res)