#title
print("Comparing two lists")

a = [1,1,2,3,5,8,10,10,11,13,21,34,55,89]
#removing duplicates
alist = list(dict.fromkeys(a))

#removing duplicates
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,21,22,23,34,34,66]
blist = list(dict.fromkeys(b))

c = []

for i in alist:
    for s in blist:
        if i == s:
            c.append(i)


print('The numbers available in both lists are\n',c)
