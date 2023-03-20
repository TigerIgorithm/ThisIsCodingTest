n,m,r = map(int,input().split())

arr= []
for i in range(3):
    li = list(map(int,input().split()))
    arr.append(li)

table = [set([]) for _ in range(100)]
for index,line in enumerate(arr):
    a,b = line
    for i in range(a,b):
        table[i].add(index)

cost = 0

for line in table:
    if len(line)==3:
        cost += 3*1*r

    elif len(line)==2:
        cost += 2*1*m
    
    elif len(line) == 1:
        cost += 1*1*n

print(cost)