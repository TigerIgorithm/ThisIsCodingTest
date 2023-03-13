s = input()
s = list(s)
c0 = s.count("0")
c1 = s.count("1")

count = 0
if c0>c1:
    for i in range(len(s)):
        if s[i]=="1" and s[i] == s[i+1]:
            continue
        if s[i] == "1" and s[i] != s[i+1]:
            count +=1
else:
    for i in range(len(s)):
        if s[i]=="0" and s[i] == s[i+1]:
            continue
        if s[i] == "0" and s[i] != s[i+1]:
            count +=1
print(count)