# Great link: https://crypto.stackexchange.com/questions/15447/convert-m-sequence-into-a-de-bruijn-sequence/15451

# Another good possible link: https://www.usna.edu/Users/math/wdj/_files/documents/brock/brock-honorsthesis/index.html

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


def f_func(s_1, s_2):
    res = xor_func(s_1, s_2)
    return res

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


res = [0, 1]
print(res)
while len(res) < 4:
    s1, s2 = res[-1], res[-2]
    print(s1, s2)
    f = f_func(s1, s2)
    res.append(f)
    print(res)
    print("-----------")
print(res)
