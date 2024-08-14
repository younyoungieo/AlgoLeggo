"""
* 문제: https://www.acmicpc.net/problem/1920
    N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.  
* 풀이: 이진 탐색을 사용하여 풀이한다. 입력받은 n_list를 정렬한 뒤, 이진 탐색을 통해 check 리스트의 값이 n_list에 있는지 확인한다.
* 시행착오: (1) 처음에 이중 for문으로 했다가 시간 초과 (2) 이진 탐색은 반드시 정렬된 리스트에서만 사용할 수 있다. (3) set(집합)을 이용하여 풀이할 수도 있다. set 매우 빠름.
"""

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
check = list(map(int, input().split()))

 
for i in check:
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if n_list[mid] == i:
            print(1)
            break
        elif n_list[mid] < i:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print(0)

# --- Using set ---

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_set = set(map(int, input().split()))

# m = int(input())
# check = list(map(int, input().split()))

# for i in check:
#     print(1) if i in n_set else print(0)	