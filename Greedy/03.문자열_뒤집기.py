# 문자열을 int형 리스트로 받음
n = list(map(int, input()))
# index
i = 0 # 기준
j = 1 # 비교할 부분
count0 = 0 # 0 묶음의 갯수
count1 = 0 # 1 묶음의 갯수

while True:
  # j가 인덱스 범위를 벗어나면 종료
  if j > (len(n) - 1):
    # 종료되기 전에 남은 묶음 갯수 추가
    if n[i] == 0:
      count0 += 1
    else:
      count1 += 1
    break
  # 기준이 0일 때
  if n[i] == 0:
    if n[j] == 1:
      i = j
      count0 += 1  
    j += 1
  # 기준이 1일 때
  else:
    if n[j] == 0:
      i = j
      count1 += 1 
    j += 1

# 묶음의 갯수가 적은 게 최종 정답
if count0 > count1:
  print(count1)
else:
  print(count0)
