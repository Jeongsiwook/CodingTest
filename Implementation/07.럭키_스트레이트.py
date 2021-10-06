# 숫자를 string으로 입력 받음
n = input()
# 자릿수를 확인
length = len(n)
# 왼쪽 자릿수들의 합과 오른쪽 자릿수들의 합
sum_left = 0
sum_right = 0

# 반으로 쪼갠 만큼을 확인하기 위한 변수
cnt = 0
for i in n:
  # 왼쪽 자릿수들의 합 구하기
  if cnt <= length / 2 - 1:
    sum_left += int(i)
    cnt += 1
  else:
    # 오른쪽 자릿수들의 합 구하기
    sum_right += int(i)

if sum_left == sum_right:
  print("LUCKY")
else:
  print("READY")
