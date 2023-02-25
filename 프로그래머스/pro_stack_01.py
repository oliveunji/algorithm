def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        else:
            if answer[-1] != num:
                answer.append(num)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer
