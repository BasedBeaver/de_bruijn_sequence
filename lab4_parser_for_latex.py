with open("lab4_polys.txt") as fp:
    for line in fp:
        line = fp.readline()
        line = line.replace('*', '')
        line = "$" + line + "$"
        line = "\item [] " + line
        print(line)