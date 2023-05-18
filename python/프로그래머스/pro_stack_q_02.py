import math


def solution(progresses, speeds):
    work_days = []
    for i in range(len(progresses)):
        duration = math.ceil((100-progresses[i])/speeds[i])
        work_days.append(duration)

    answer = []
    count = []
    for i in range(len(work_days)):
        if len(answer) == 0:
            answer.append(work_days[i])
            count.append(1)
        else:
            if work_days[i] <= answer[-1]:
                count[-1] += 1
            else:
                answer.append(work_days[i])
                count.append(1)
    return count


solution([93, 30, 55], 	[1, 30, 5])
