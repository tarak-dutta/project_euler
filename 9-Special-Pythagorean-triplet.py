p = 1000
for a in range(1,p+1):
    for b in range(a,p+1):
        c = p - a - b
        if c**2 == a**2 + b**2:
            print(a*b*c)
