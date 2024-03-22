
"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
"""

if __name__ == '__main__':
   students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
students.sort(key=lambda x: x[1])
second_lowest_grade = students[0][1]
for s in students:
    if s[1] > second_lowest_grade:
        second_lowest_grade = s[1]
        break

second_lowest_students = []
for s in students:
    if s[1] == second_lowest_grade:
        second_lowest_students.append(s[0])
second_lowest_students.sort()
for name in second_lowest_students:
    print(name)

