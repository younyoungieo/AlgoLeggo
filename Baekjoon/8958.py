n = int(input())

for i in range(n):
    line = input()
    state = 0
    score = 0
    total = 0
    for i in line:
        if i == "O" and state == 0:
            state = 1
            score = 1
            total += score
        elif i == "O" and state == 1:
            state = 1
            score += 1
            total += score
        else:
            state = 0
    print(total)