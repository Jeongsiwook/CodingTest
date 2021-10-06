# 문자열을 입력 받음
s = input()
# 문자를 순서대로 넣을 배열 선언
arr_s = []
# 정수들의 합
sum_i = 0

for i in s:
  # 아스키 코드의 값이 A보다 클 경우에 문자들로 판단
  if ord(i) >= ord('A'):
    arr_s.append(ord(i))
  # 나머지는 정수들로 판단
  else:
    sum_i += int(i)

# 문자들의 아스키 코드를 오름차순으로 정렬
arr_s.sort()

# 아스키 코드를 다시 문자로 바꿔 출력
for i in arr_s:
  print(chr(i), end="")

# 정수들의 합 출력
print(sum_i)

# 문자가 알파벳인지 확인하는 코드: 문자.isalpha()
# 리스트 요소들을 붙여서 출력: print(''.join(리스트))
