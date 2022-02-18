import itertools

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

for i in itertools.combinations(arr, L):
  number = i.count("a") + i.count("e") + i.count("i") + i.count("u") + i.count("o")
  if number >= 1 and len(i) - number >= 2:
    print("".join(list(i)))
    
    
"""
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

array = input().split(' ')
array.sort()

for password in combinations(array, l):
  count = 0
  for i in password:
    if i in vowels:
      count += 1
      
if count >= 1 and count <= l - 2:
  print(''.joint(password))
"""
