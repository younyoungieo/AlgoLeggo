"""
* 문제: https://www.acmicpc.net/problem/8958
    OX 퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
* 풀이: O이 연속되면 점수가 1씩 증가하고 X가 나오면 점수가 초기화되어야하므로, state 변수를 이용하여 O가 나왔는지 여부를 저장함.
* 시행착오: 입력값을 한 줄씩 순서대로 받는 걸 이해 못하고, 한 번에 여러 줄을 받는다고 생각해서 틀렸다가 다른 풀이를 찾아보고 이해함.
"""


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