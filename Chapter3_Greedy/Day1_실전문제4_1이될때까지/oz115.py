<<<<<<< HEAD
n, k = map(int, input().split())
result = 0

while n>=k:

    if n%k!=0:
        n -= 1
        result +=1
    else:
        n = n//k
        result += 1

while n>1:
    n -= 1
    result +=1


=======
n, k = map(int, input().split())
result = 0

while n>=k:

    if n%k!=0:
        n -= 1
        result +=1
    else:
        n = n//k
        result += 1

while n>1:
    n -= 1
    result +=1


>>>>>>> 4dd9e1749888c8c2c9cff44ab72e99376e490484
print(result)