n = int(input())

arr=[]
for i in range(n):
    li = list(map(int,input().split()))
    arr.append(li)


for i in arr:
    rank = 1
    for j in arr:
        if i == j:
            continue

        if i[0]<j[0] and i[1]<j[1]:
            rank +=1
    print(rank, end=' ')