"""
* 문제: https://www.acmicpc.net/problem/21866
    경진대회 점수 결과를 받아서, 해커인지, 추첨 대상자인지, 아무것도 아닌지를 출력하는 프로그램을 작성하시오.
* 풀이: 각 점수에 대한 최대 점수를 리스트로 만들어서, zip 함수를 이용하여 각 점수와 최대 점수를 비교함.
"""

grades_str = input()
grades_str_list = grades_str.split(" ")
grades = list(map(int, grades_str_list))

max_grades = [100, 100, 200, 200, 300, 300, 400, 400, 500]

is_hacker = any(grade > max_grade for grade, max_grade in zip(grades, max_grades))

if is_hacker:
    print("hacker")
elif sum(grades) >= 100:
    print("draw")
else:
    print("none")