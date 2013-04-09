def thing(alist, *blur):
    alist.extend(blur)

blist = [1, 2, 3]

thing(blist, 6, 8)

print(blist)
