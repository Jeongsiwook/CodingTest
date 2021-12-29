"""
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 구매하겠다고 한다.
가게 안에 부품이 모두 있는지 요청한 부품 번호의 순서대로 확인해 부품이 있으면 yes를, 없으면 no를 출력한다.

ex)
N = 5
[8, 3, 7, 9, 2]

M = 3
[5, 7, 9]
"""

# bisect library 사용
from bisect import bisect_left, bisect_right

N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
request = list(map(int, input().split()))

for i in request:
  if bisect_right(data, i) - bisect_left(data, i):
    print("yes", end=" ")
  else:
    print("no", end=" ")
    

# binary_search 사용
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
request = list(map(int, input().split()))

for i in request:
  if binary_search(array, i, 0, n - 1) != None:
    print("yes", end=" ")
  else:
    print("no", end=" ")
    

# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print("yes", end=" ")
  else:
    print("no", end=" ")
