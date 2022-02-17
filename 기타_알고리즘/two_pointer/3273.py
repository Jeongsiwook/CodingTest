from sys import stdin

# 갯수, 리스트, 특정 값 입력 받음
n = int(input())
data = list(map(int, stdin.readline().split()))
data.sort()
print(data)
x = int(input())

# 결과, 두 쌍의 합계, index 값
count = 0
interval_sum = 0
index = 1

# start가 제일 마지막 요소전까지만 이동
for start in range(n - 1):
  # 첫 번째 요소가 특정 값보다 클 경우 생략
  if data[start] >= x:
    break
  # 두 번째 요소가 start보다 하나 뒤에서 끝까지
  for end in range(index, n):
    # 두 번째 요소가 특정 값보다 클 경우 생략
    if data[index] >= x:
      n = index
      break
    interval_sum = data[start] + data[end]
    # 합계가 특정 값일 경우
    if interval_sum == x:
      count += 1
  index += 1

print(count)


"""
from sys import stdin

# 갯수, 리스트, 특정 값 입력 받음
n = int(input())
data = list(map(int, stdin.readline().split()))
x = int(input())
data.sort()

# 결과, 두 쌍의 합계, index 값
start, end = 0, n - 1
count = 0
while start < end:
  interval_sum = data[start] + data[end]
  if interval_sum > x:
    end -= 1
  elif interval_sum < x:
    start += 1
  else:
    count += 1
    start += 1
    end -= 1    

print(count)
"""
