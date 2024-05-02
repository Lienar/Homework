grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_len = list(students)

students_grades = {}
students_len.sort()
sum = 0

for i in range (len(grades)):
    for j in range (len(grades[i])):
        sum = sum + int(grades[i][j])
    students_grades[students_len[i]] = sum / len(grades[i])
    sum = 0

for i in range (len(students_len)):
    print (students_len[i], ': ',students_grades[students_len[i]])


