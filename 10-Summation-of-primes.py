# this code takes hours to run
# TODO: find more optimal solution
n = 2000000
s = 0
for i in range(2,n):
    if i%100000 == 0:
        print(i)
    p = True
    for x in range(2,i):
        if i%x == 0:
            # print('{} is not prime'.format(i))
            p = False
            break
    if p:
        s += i
print(s)
