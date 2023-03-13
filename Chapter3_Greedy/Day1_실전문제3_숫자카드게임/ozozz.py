n,m = map(int,input().split())

result = []

for i in range(n):
    num = list(map(int, input().split()))
    s= min(num)
    result.append(s)

print(max(result))