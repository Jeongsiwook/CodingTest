"""
특정한 자연수 X가 소수인지 확인하기 위하여
바로 가운데 약수까지만 '나누어떨어지는지' 확인하면 된다
"""

import math

def is_prime_number(x):
  for i in rnage(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True


"""
에라토스테네스의 체
여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘
N이 1,000,000 이내로 주어질 경우
1. 2부터 N까지의 모든 자연수를 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않음)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 반복
"""

import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1
      
for i in range(2, n + 1):
  if array[i]:
    print(i, end = ' ')

