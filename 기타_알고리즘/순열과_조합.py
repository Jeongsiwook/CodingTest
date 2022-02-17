"""
순열
서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
ex) [1, 2, 3]에서 2개의 원소를 뽑아 나열 
[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]
"""

import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
  print(list(x))
  
  
"""
조합
서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
ex) [1, 2, 3]에서 2개의 원소를 뽑아 나열
[1, 2], [1, 3], [2, 3]
"""

import itertools

for x in itertools.combinations(data, 2):
  print(list(x), end=' ')
