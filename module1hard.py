grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_len = list(students)

students_grades = {}
students_len.sort()

for i in range (len(grades)):
    students_grades[students_len[i]] = sum(grades[i]) / len(grades[i])


for i in range (len(students_len)):
    print (students_len[i], ': ',students_grades[students_len[i]])



