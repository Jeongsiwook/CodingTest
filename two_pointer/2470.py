from sys import stdin

# 용액의 수 N
n = int(input())
# 용액의 특성값 list
data = list(map(int, stdin.readline().split()))
data.sort() 

start, end = 0, n - 1
count = 0
# 두 용액의 특성값과 특성값을 합친 값을 저장할 리스트
arr = []

def check(data, arr):
  global start, end
  while start < end:
    interval_sum = data[start] + data[end]  
    # 합계가 0보다 크면 end를 움직이고, 반대면 start를 움직임
    if interval_sum > 0:
      # 구한 값은 arr에 넣어줌
      arr.append((data[start], data[end], abs(interval_sum)))
      end -= 1
    elif interval_sum < 0:
      arr.append((data[start], data[end], abs(interval_sum)))
      start += 1
    # 합계가 0이라면 바로 출력
    else:
      print(data[start], data[end])
      return
  # 리스트를 3번째 요소를 기준으로 정렬
  arr = sorted(arr, key=lambda x: x[2])
  print(arr[0][0], arr[0][1])   
  return

check(data, arr)
    
