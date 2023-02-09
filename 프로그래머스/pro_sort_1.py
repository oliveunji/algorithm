def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp_list = sorted(array[i-1:j])
        print(temp_list)
        answer.append(temp_list[k-1])
    return answer
