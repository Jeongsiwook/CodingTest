# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    s_len = len(s)      # 문자열의 길이    
    min_value = 1001    # 최소 문자열의 길이
    
    # i는 자르는 단위 크기
    for i in range(1, s_len):
        temp_str = ""   # 임시 문자열 길이
        k = 0           # 항상 인덱스 0부터 확인하게 하는 변수
        temp = 1        # 문자열의 같은 갯수
        
        # i의 크기만큼 움직이며 확인하며 슬라이싱 문자열을 비교
        for j in range(0 + i, s_len, i * 1):
            # 두 문자열이 같다면 temp + 1
            if s[k:k+i] == s[j:j+i]:                
                temp += 1
            # 두 문자열이 다를 때
            else:
                # 문자열의 같은 갯수가 1이면 생략
                if temp == 1:
                    temp_str += s[k:k+i]
                    k = j
                # 1보다 크다면 temp와 같은 문자열 적음
                else:
                    temp_str += str(temp) + s[k:k+i]
                    k = j
                    temp = 1
        
        # 마지막 부분 처리
        if temp == 1:
            temp_str += s[k:k+i]
            k = j
        else:
            temp_str += str(temp) + s[k:k+i]
        
        # 제일 압축된 값 찾기
        if min_value > len(temp_str):
            min_value = len(temp_str)
                 
    return min_value
