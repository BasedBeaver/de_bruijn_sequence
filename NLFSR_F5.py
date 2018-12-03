def add_func(a, b):
    return (a + b) % 5


def mul_func(a, b):
    return (a * b) % 5


#def f_func(s1, s2, s3):
 #   return add_func(add_func(mul_func(s1, 3), mul_func(s2, 2)), s3)
def f_func(s1,s2,s3):
    return (s1 + s2 + s3*2)*3 % 5


res = [2, 3, 4, 1]
res_NL = [2, 3, 4, 1]
added = False
while len(res) < 627:
    s1, s2, s3 = res[-4], res[-2], res[-1]
    f = f_func(s1, s2, s3)
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
print(len(res), len(res_NL))
