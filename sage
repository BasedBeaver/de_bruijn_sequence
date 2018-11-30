F.<x>=GF(7)['x']
f = x^8 + x^6 + 1
print("Is " + str(f) + " primitive?")
c1 = f.is_primitive()
if c1:
    print(c1)
else:
    print(c1)
    print("\n")
    print("Is " + str(f) + " reducible?")
    flag = f.is_irreducible()
    if not flag:
        print(not flag)
        print("\n")
        print("The factors are: ")
        c2 = f.factor()
        for fac in c2:
            print(fac[0])
            print("is primitive: ", fac[0].is_primitive())
            print("is irreducible: ", fac[0].is_irreducible())
            print("\n")
    else:
        print(str(f) + " is irreducible")

