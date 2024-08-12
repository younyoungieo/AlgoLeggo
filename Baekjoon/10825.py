"""
* 문제: https://www.acmicpc.net/problem/10825
    첫째 줄에는 학생의 수, 둘째 줄부터는 학생의 이름, 국어, 영어, 수학 점수를 입력받는다. 국어 점수가 감소하는 순서로, 국어 점수가 같으면 영어 점수가 증가하는 순서로, 국어 점수와 영어 점수도 같으면 수학 점수가 감소하는 순서로, 그래도 같으면 이름이 사전 순으로 증가하는 순서로 정렬한다.
* 풀이: 입력값들을 리스트로 만든 뒤, sort() 함수를 사용하여 정렬한다. 정렬 기준은 lambda 함수로 지정한다.
* 시행착오: sort() 함수의 인자 중 key 값에 여러 값을 넣어서 정렬할 수 있음을 알게 됨. 또한 lambda 함수를 새롭게 활용해봄.
"""

import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])