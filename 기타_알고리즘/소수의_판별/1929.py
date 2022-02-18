import math

M, N = map(int, input().split())
array = [True for i in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= N:
      array[i * j] = False
      j += 1

array[1] = False

for i in range(M, N + 1):
  if array[i] == True:
    print(i)
