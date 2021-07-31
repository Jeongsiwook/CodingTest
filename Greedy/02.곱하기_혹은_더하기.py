# 입력받은 값을 int형 리스트로 만듬
s = list(map(int, input()))

cnt = len(s)
i = 2
result = 0

# 리스트 크기가 1인 경우
if cnt == 1:
  print(s[0])

# 리스트 크기가 2인 경우
else:
  # 두 수 중에서 하나라도 0 혹은 1인경우, 곱하기보다는 더하기 수행
  if (s[0] <= 1) or (s[1] <= 1):
    result += s[0] + s[1]
  else:
    result += s[0] * s[1]

  for _ in range(cnt - 2):
    if (result <= 1) or (s[i] <= 1):
      result += s[i]
    else:
      result *= s[i]
    i += 1
  
print(result)
