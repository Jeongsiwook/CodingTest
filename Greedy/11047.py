# 백준 11047
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

def func(data):
  s = 0 # 합계
  cnt = 0 # 카운트
  # 큰 수 부터
  for i in range(n - 1, -1, -1):
    # 합계가 k가 더 크면 계속 현재 원소 더함
    while k > s:
      s += data[i]
      cnt += 1
    # 합계 s가 특정한 수 k를 만족시킬 경우 
    if s == k:
      print(cnt)
      return
    # s가 k보다 더 커졌을 경우
    else:
      s -= data[i] 
      cnt -= 1        
      
n, k = map(int, input().split())
data = []
for _ in range(n):
  i = int(input())
  data.append(i)

func(data)
