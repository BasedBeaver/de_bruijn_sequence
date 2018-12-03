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

res = [0, 1, 0, 0]
res_NL = [0, 1, 0, 0]
while len(res) < 16:
    s1, s2 = res[-4], res[-3]
    f = f2_func(s1, s2)
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


"""
F5 code
"""

res = [2, 3, 4, 1]
res_NL = [2, 3, 4, 1]
added = False
while len(res) < 625:
    s1, s2, s3 = res[-4], res[-2], res[-1]
    f = f5_func(s1, s2, s3)
    res.append(f)
    c1, c2, c3 = res[-4], res[-3], res[-2]
    if c1 == 0 and c2 == 0 and c3 == 0 and not added:
        res_NL.append(0)
        added = True
    res_NL.append(f)
    print("-----------")
if (res[1] == 0 and res[2] == 0 and res[-1] == 0) or\
        (res[1] == 0 and res[-2] == 0 and res[-1] == 0):
    res_NL.append(0)
print(res)
print(res_NL)
out_string = str(res)
out_string = ''.join(c for c in out_string if c not in '[],')
print(len(res), len(res_NL))


"""
De Bruijn set 10
"""




# with open("F5_out.txt", 'w') as file:
#     file.write(out_string)
