def solution(food_times, k):
    answer = 0
    time = 0
    i = 0
    length = len(food_times)
    sumArr = sum(food_times)

    while True:
        i %= length # 인덱스가 맨 마지막 인덱스를 넘어갈 시에 되돌려줌
        # 리스트 요소들이 모두 0이 되어버릴 경우
        if time == sumArr: 
            return -1
        # 네트워크 오류가 발생할 경우
        if time == k:
            while True:
                # 최종 위치 요소가 0일 경우
                if food_times[i] == 0:
                    i = (i + 1) % length
                else:
                    answer = i + 1 # 다음 위치 지목
                    break
            return answer # 최종 결과 반환
        # 요소가 0이 아닐 경우
        if food_times[i] != 0:
            food_times[i] -= 1
            i += 1            
            time += 1
        # 요소가 0일 경우
        else:
            i += 1
            continue     
