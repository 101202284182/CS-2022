#TASK 2
# for a in range(1, 13):
#     print("Time table for %d" % (a))
#     for b in range(1, 13):
#         print("%d x %d = %d" % (a, b, a * b))

#TASK 3
# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))

# for i in range(rows):
#     items = ""
#     for n in range(columns):
#         items += "*"
#     print(items)

#TASK 4
# pattern = int(input("Enter pattern: "))
# items = ""

# for i in range(pattern):
#     items += "*"
#     print(items)

#TASK 5
# pattern = int(input("Enter pattern: "))
# items = []

# def printPattern(patternArray):
#     finalPattern = ""
#     for i in range(len(patternArray)):
#         finalPattern += patternArray[i]
#     print(finalPattern)

# for i in range(pattern):
#     items.append(" ")

# for i in range(pattern):
#     items.remove(" ")
#     items.append("*")
#     printPattern(items)

#TASK 6
# price = float(input("Enter price per sq. meter: "))

# print("\tWidth")
# print("Length\t5m\t10m\t15m\t20m")
# for i in range(1, 11):
#     print("%sm\t%d\t%d\t%d\t%d" % (i * 10, (5*(i*10)) * price, (10*(i*10)) * price, (15*(i*10)) * price, (20*(i*10)) * price))

#TASK 7
# studentsGrades1 = []
# studentsGrades2 = []
# students = int(input("Enter amount of students in a class: "))

# for i in range(students):
#     grade = int(input("Student #" + str(i + 1) + ", enter your grade in 1 subj (0-100): "))
#     if(grade == 0):
#         break
#     else:
#         studentsGrades1.append(grade)

# for i in range(students):
#     grade = int(input("Student #" + str(i + 1) + ", enter your grade in 2 subj (0-100): "))
#     if(grade == 0):
#         break
#     else:
#         studentsGrades2.append(grade)

# maxGrade1 = "Student #" + str(studentsGrades1.index(max(studentsGrades1))) + " have max grade of " + str(max(studentsGrades1) + "in subject 1")
# minGrade1 = "Student #" + str(studentsGrades1.index(min(studentsGrades1))) + " have min grade of " + str(min(studentsGrades1) + "in subject 1")
# maxGrade2 = "Student #" + str(studentsGrades2.index(max(studentsGrades2))) + " have max grade of " + str(max(studentsGrades2) + "in subject 2")
# minGrade2 = "Student #" + str(studentsGrades2.index(min(studentsGrades2))) + " have min grade of " + str(min(studentsGrades2) + "in subject 2")

# print("%s\n%s\n%s\n%s" % (maxGrade1, minGrade1, maxGrade2, minGrade2))