# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
arr = list(map(int, input().split()))

arr.sort(reverse = True) # 입력받은 수들 정렬하기
result = 0

if arr[0] == arr[1]: # 가장 큰 수가 2개 이상일 경우
  count = m
  result = arr[0] * count
  print(result) # 최종 답안 출력
else: # 반대 경우
  count = int(m / (k + 1)) * k + int(m % (k + 1)) # k + 1 크기의 수열 
  result = count * arr[0] # 가장 큰 수의 갯수
  result += (m - count) * arr[1] # 두 번째 큰 수의 갯수
    
  print(result) # 최종 답안 출력
