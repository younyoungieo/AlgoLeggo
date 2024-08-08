"""
* 문제: https://www.acmicpc.net/problem/10989
    첫째 줄에는 수의 개수, 둘째 줄부터는 수를 입력받아서, 이를 정렬한 결과를 출력하시오. 이때 수는 10,000보다 작거나 같은 자연수이다.
* 풀이: 입력값을 한 줄씩 받아서, 해당 수의 인덱스에 해당하는 값을 1씩 증가시킨다. 그리고 해당 인덱스의 값이 0이 아니면 그 값만큼 인덱스를 출력한다. (카운팅 정렬 또는 계수 정렬)
* 시행착오: 당연히 sort() 함수를 사용하면 시간초과가 발생할 줄 알았으나, 떠오르는 게 않아서 시도해보고 틀림. 다른 풀이를 찾아보고 이해함.
"""

# sys.stdin.readline를 쓰면 input()보다 빠르다!
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000+1)

for _ in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)