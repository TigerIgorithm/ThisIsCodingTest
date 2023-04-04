n = int(input())

array = []
#age = []

for i in range(n):
    age_data = input().split()
    array.append([int(age_data[0]),age_data[1]])
    
array = sorted(array, key = lambda student: student[0])

for student in array:
    print(student[1], student[0],end = " ")

