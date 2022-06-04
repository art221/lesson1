p = (0,10)
it = iter(p)
l = [(1+next(it)*5) for a in range(1,10)]
print(l)
it = iter(l)
while it:
    try:
        print((next(it)))
    except:
        break
