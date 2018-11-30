F.<x>=GF(2)['x']
f = x^23 + x^6 + 1
print("is " + str(f) + " primitive?")
c1 = f.is_primitive()
print(c1)
print("is " + str(f) + " reducible?")
flag = f.is_irreducible()
if not flag:
    print("It is reducible")
    print("The factors are: ")
    c2 = f.factor()
    for fac in c2:
        print(fac[0])
        print("is primitive: ", fac[0].is_primitive())
        print("is irreducible: ", fac[0].is_irreducible())
        print("--------------------------------------------------")
else:
    print("It is irreducible")
