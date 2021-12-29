# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
length = len(array)

for i in range(length):
  min_index = i
  for j in range(i + 1, length):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index]

  
# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
length = len(array)

# i는 header 역할
for i in range(1, length):
  for j in range(i, 0, -1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break
      

# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
length = len(array)

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    # 조건을 반대로 하면 왜 안돼? 진짜 XX XXXX
    while array[left] <= array[pivot] and left <= end:
      left += 1

    while array[right] >= array[pivot] and start < right:
      right -= 1

    if left > right:
      array[pivot], array[right] = array[right], array[pivot]  
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, length - 1)
print(array)


##
