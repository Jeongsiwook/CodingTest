# 피보나치 수열 탑 다운(메모제이션 기법), 오버헤드가 일어날 수 있음
d = [0] * 100

def fibo(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  # 책에선 else를 사용하지 않았는데 이유가 있을까?
  else: 
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 피보나치 수열 바텀 업
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]
  
 print(d[n])
