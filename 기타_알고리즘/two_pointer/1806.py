from sys import stdin

n, s = map(int, input().split())
data = list(map(int, stdin.readline().split()))

index = 1
tag = 1
min_count = 9999999

for start in data:
  # 그러한 합을 만드는 것이 불가능할 경우
  if sum(data) < s:
    print(0)
    break
  # 초기화
  count = 0
  interval_sum = 0
  interval_sum += start
  index = tag
  while index < n:
    if interval_sum >= s:
      count += 1
      break
    count += 1    
    interval_sum += data[index]
    index += 1

  if min_count > count and min_count > count and interval_sum > s:
    min_count = count
  tag += 1
  
if min_count == 9999999:
  print(0)
else:
  print(min_count) 
  
  
"""
from sys import stdin

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 0
end = 1
result = n
interval_sum = arr[start]
if interval_sum == s:
    result = 1
flag = 0

while not (start == end == n):
    if interval_sum < s and end < n:
        interval_sum += arr[end]
        end += 1
    else:
        interval_sum -= arr[start]
        start += 1

    if interval_sum >= s:
        result = min(result, end-start)
        flag = 1

if flag == 0:
    print(0)
else:
    print(result)
"""
