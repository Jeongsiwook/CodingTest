# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
arr = list(map(int, input().split()))

arr.sort(reverse = True) # 입력받은 수들 정렬하기
result = 0

while(m > 0):
  for _ in range(k): # 가장 큰 수를 K번 더하기
    result += arr[0]
    m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
      break
  if m == 0: # m이 0이라면 반복문 탈출
    continue

  # 두 번째로 큰 수가 첫 번째 수와 같은 지 확인
  if arr[0] == arr[1]: # 같은 경우 
    for _ in range(k):
      result += arr[1]
      m -= 1
      if m == 0:
        break
  else: # 다른 경우
    if m == 0:
      continue 
    result += arr[1]
    m -= 1 

print(result) # 최종 답안 출력
