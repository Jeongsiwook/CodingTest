"""
동빈이는 두 개의 배열 A와 B를 가지고 있다.
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 바꾸는 것을 말한다.
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

ex)
5 3
1 2 5 4 3
5 5 6 6 5

26
"""
# 계수 정렬
n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))
count_a = [0] * (max(array_a) + 1) 
count_b = [0] * (max(array_b) + 1)
result_a = []
result_b = []

def quick_sort_a(array):
  for i in range(len(array_a)):
    count_a[array_a[i]] += 1

def quick_sort_b(array):
  for i in range(len(array_b)):
    count_b[array_b[i]] += 1

quick_sort_a(array_a)
quick_sort_b(array_b)

for i in range(1, len(count_a)):
  for j in range(count_a[i]):
    result_a.append(i)

for i in range(1, len(count_b)):
  for j in range(count_b[i]):
    result_b.append(i)

for i in range(k):
  if result_a[i] < result_b[n - (i + 1)]: # 이 조건도 생각 못했다..
    result_a[i], result_b[n - (i + 1)] = result_b[n - (i + 1)], result_a[i]

print(sum(result_a))


# 답안 예시
n, k = map(int, input().split())
a = list(map(int, input().split())
b = list(map(int, input().split())
         
a.sort()
b.sort(reverse=True)
         
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
         
         
         
         
         
         
