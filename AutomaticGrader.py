key = list(map(str, input().split()))

students = [
    ["John", ['A', 'B', 'B', 'C', 'D']],
    ["Jane", ['A', 'A', 'A', 'A', 'A']],
    ["Bob",  ['B', 'A', 'D', 'D', 'C']]
]
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
