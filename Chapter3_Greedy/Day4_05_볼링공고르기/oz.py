n , m = map(int,input().split())
weight = list(map(int,input().split()))

count = 0

for i in range(len(weight)):
    for j in range(len(weight)):
        if j<=i:
            continue
        
        if weight[i] == weight[j]:
            continue
        
        count += 1

print(count)