s = input()
s = s.upper()
alphabet = list(set(s))

arr=[]
for a in alphabet:
    arr.append(s.count(a))


if len(arr)!=len(set(arr)):
    print("?")
else:
    print(alphabet[arr.index(max(arr))])