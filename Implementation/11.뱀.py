# 보드의 크기
n = int(input())
# 보드 요소를 모두 0으로 설정
arr = [[0] * n for i in range(n)]

# 사과의 갯수
k = int(input())
# 보드에 사과가 있으면 요소를 1로 설정
for i in range(k):
  r, c = map(int, input().split())
  arr[r - 1][c - 1] = 1

# 이동한 초와 방향을 가지고 있는 리스트
d = []
# 몇 번을 회전하는 지
l = int(input())
for i in range(l):
  x, c = map(str, input().split())
  d.append((x, c))

# 뱀 위치
snake_arr = [[0] * n for i in range(n)]
# 뱀이 시작한 위치이므로 1
snake_arr[0][0] = 1
# 방향 인덱스
direction = 0

# 시뮬레이션 시작
dx = [0, 1, 0, -1] # 동, 서, 남, 북 / 동, 남, 서, 북
dy = [1, 0, -1, 0]

# (0, 0) 위치에서 시작
next_x = 0; next_y = 0; tail_x = 0; tail_y = 0 # 다음 x, y 위치
index = 0 # 종료 하기 위한 조건
result = 0 # 결과
tag = 0 # 부딪침 확인
while True:
  # 종료 조건
  if index > l:
    print(result)
    break
  # 주어진 시간만큼 이동
  for i in range(int(d[index][0])):
    next_x += dx[direction]
    next_y += dy[direction]

    # 범위를 벗어난 경우
    if next_x < 0 or next_x > n - 1 or next_y < 0 or next_y > n - 1:
      result += 1
      tag = 1
      break

    # 뱀의 몸에 부딪치지 않는 경우
    if snake_arr[next_x][next_y] != 1:
      snake_arr[next_x][next_y] = 1
    # 뱀의 몸에 부딪친 경우(1)
    else:
      result += 1
      tag = 1
      break

    # 사과가 없는 경우     
    if arr[next_x][next_y] != 1:
      snake_arr[tail_x][tail_y] = 0
      tail_x += dx[direction]
      tail_y += dy[direction]
    result += 1
  
  # 뱀의 몸에 부딪친 경우(2)
  if tag == 1:
    print(result)
    break

  # 방향 확인    
  if d[index][1] == 'D':
    direction += 1
    direction %= 4
  else:
    direction -= 1
    direction %= 4

  # 종료 조건 확인  
  index += 1
  
"""
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1
  
# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction
  
def simulate():
  x, y = 1, 1 # 뱀의 머리 위치
  data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
  direction = 0 # 처음에는 동쪽을 보고 있음
  time = 0 # 시작한 뒤에 지난 '초' 시간
  index = 0 # 다음에 회전할 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:     # 사과가 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪혔다면
    else:
      time += 1
      break
    x, y = nx, ny
    time += 1
    if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time
  
print(simulate())
"""
