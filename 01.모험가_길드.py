n = int(input())
arr = list(map(int, input().split()))

i = 0 # 모험가 리더 인덱스
result = 0 
index = n - 1 # 공포도가 가장 높은 인덱스

arr.sort()
while True:
  index -= arr[i] # 공포심이 작은 모험가가 큰 모험가를 데려감
  if index < i: # 사람이 부족하면 반복문 탈출
    break
  result += 1 # 그룹의 수 증가시키기
  i += 1 #

print(result) # 총 그룹의 수 출력
