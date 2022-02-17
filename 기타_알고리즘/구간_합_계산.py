"""
연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하기
1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L - 1]
"""

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)
  
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
