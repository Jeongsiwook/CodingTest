# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 선언, 초기화, 입력받고, 원소로 추가하는 방법까지 한 줄
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  arrMin = list() 
  arrMin.append(min(arr[i])) # 가장 작은 원소들로 리스트 생성

arrMin.sort(reverse = True) # 가장 큰 원소 찾기 위해 정렬

print(arrMin[0]) # 최종 답안 출력
