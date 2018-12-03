def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]

def add_func(a, b):
    return (a + b) % 5


def mul_func(a, b):
    return (a * b) % 5


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


def f2_func(s1, s2):
    return xor_func(s1, s2)


def f5_func(s1, s2, s3):
    return (s1 + s2 + s3*2)*3 % 5


"""
F2 code
"""

res_f2 = [1, 1, 1, 1]
res_NL_f2 = [1, 1, 1, 1]
while len(res_f2) < 10000:
    s1, s2 = res_f2[-4], res_f2[-3]
    f = f2_func(s1, s2)
    res_f2.append(f)
    c1, c2, c3 = res_f2[-4], res_f2[-3], res_f2[-2]
    if c1 == 0 and c2 == 0 and c3 == 0:
        res_NL_f2.append(0)
    res_NL_f2.append(f)
if (res_f2[0] == 0 and res_f2[1] == 0 and res_f2[-1] == 0) or\
        (res_f2[0] == 0 and res_f2[-2] == 0 and res_f2[-1] == 0):
    res_NL_f2.append(0)
print(res_f2)
print(res_NL_f2)
print(len(res_f2), len(res_NL_f2))


"""
F5 code
"""

res_f5 = [2, 3, 4, 1]
res_NL_f5 = [2, 3, 4, 1]
while len(res_f5) < 10000:
    s1, s2, s3 = res_f5[-4], res_f5[-2], res_f5[-1]
    f = f5_func(s1, s2, s3)
    res_f5.append(f)
    c1, c2, c3, c4 = res_f5[-4], res_f5[-3], res_f5[-2], res_f5[-1]
    if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 1:
        res_NL_f5.append(0)
    res_NL_f5.append(f)
if (res_f5[0] == 0 and res_f5[1] == 0 and res_f5[-1] == 0) or\
        (res_f5[0] == 0 and res_f5[-2] == 0 and res_f5[-1] == 0):
    res_NL_f5.append(0)
print(res_f5)
print(res_NL_f5)
print(len(res_f5), len(res_NL_f5))


"""
De Bruijn set 10
"""
res_NL = []

for i in range(0, len(res_NL_f5)):
    if res_NL_f2[i] == 1:
        res_NL.append(res_NL_f5[i])
    elif res_NL_f2[i] == 0:
        res_NL.append((9 - res_NL_f5[i]))
print(res_NL)
print(len(res_NL))


out_string = str(res_NL)
out_string = ''.join(c for c in out_string if c not in '[],')
with open("db_out.txt", 'w') as file:
    file.write(out_string)
