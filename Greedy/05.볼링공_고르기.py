# combination 라이브러리 사용
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
data = list() # 중복되는 갯수 확인용 
result = len(list(combinations(arr, 2)))

for i in range(1, m + 1):
  # 가장 큰 숫자만큼 돌면서 같은 갯수가 몇 개인지 확인
  count = 0
  for j in arr:
    if i == j:
      count += 1  
  data.append(count)

for i in data:
  # 같은 갯수가 2인 경우를 제외하고 combination 계산해서 result에서 빼줌
  if i == 2:
    result -= 1
  elif i > 2:
    result -= len(list(combinations(range(i), 2)))

print(result) # 최종 결과 출력
