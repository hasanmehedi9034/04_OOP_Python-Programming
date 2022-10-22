total_students = int(input())

all_students = []

for i in range(total_students):
    student_name, student_marks = input().split()
    all_students.append(dict(zip([student_name], [int(student_marks)])))

with open('result_sheet.txt', 'w') as f:
    for roll, result in enumerate(all_students):
        for name, marks in result.items():
            r = roll + 1
            f.write(f'{r}. Name: {name}, Marks: {marks}\n')
