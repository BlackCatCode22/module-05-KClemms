fname = input('Enter File: ')
if len(fname) < 1 : fname = '/Users/ikarlie_2/Desktop/py4e/ex_09/clown.txt'
fhand = open(fname)

many = dict()

for lin in fhand:
    lin = lin.rstrip()
    wds = lin.split()
   
    for w in wds: 
       many[w] = many.get(w, 0) + 1

# Find the top 5 words by frequency

# print(many.items)
# print(sorted(many.items()))

tmp = dict()
newlist = list()
for k,v in many.items() :
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)
print(cool)

# prints the first 5 items of the list

for v,k in cool[:5] :
    print(k,v)