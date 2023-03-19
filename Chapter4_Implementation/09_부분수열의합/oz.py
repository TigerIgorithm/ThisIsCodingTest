from itertools import combinations 
n,m = map(int,input().split())
arr = list(map(int,input().split()))

count = 0

for i in range(1,len(arr)+1):
    li = combinations(arr,i)
    for a in li:
        if sum(a)== m:
            count +=1

print(count)