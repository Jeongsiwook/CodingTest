"""
동빈이네 떡볶이 떡은 떡의 길이가 일정하지 않다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만틈의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

ex)
4 6
19 15 10 17

15
"""

# bisect library 사용
from bisect import bisect_left

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
max_number = array[-1]
result = 0
while max_number != 0:
  temp = array[bisect_left(array, max_number):]
  if (sum(temp) - len(temp) * max_number) == m:
    print(max_number)
    break
  else:
    max_number -= 1


# 답안 예시
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = m + 1

print(result)
