n = map(int,input().split())
adventure = list(map(int,input().split()))

adventure.sort()
count = 0
while len(adventure)!=0:
    a = adventure[-1]
    for _ in range(a):
        adventure.pop()
    count += 1
print(count)