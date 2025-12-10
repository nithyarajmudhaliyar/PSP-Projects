key = input("Enter answer key (space separated): ").split()
n = int(input("Enter number of students: "))

students = []

for _ in range(n):
    name = input("Enter student name: ")
    answers = input(f"Enter answers of {name} (space separated): ").split()
    students.append([name, answers])

for student in students:
    name = student[0]
    answers = student[1]
    if len(answers) != len(key):
        print(f'{name} is invalid')
    score = 0
    for i in range(len(key)):
        if answers[i] == key[i]:
            score += 1
    print(f'{name}:{score}/{len(key)}')
