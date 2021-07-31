# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
count = 0

while True:
  if n == 1:
    break

  while True:
    # N이 k로 나누어 떨어질때까지 1씩 빼기
    if n == 1 or n % k == 0:
      break
    n -= 1
    count += 1
    
  if n == 1:
    break
    
  n = int(n / k) # n이 k로 나누어 떨어지면 나누기
  count += 1 

print(count) # 최종 답안 출력
