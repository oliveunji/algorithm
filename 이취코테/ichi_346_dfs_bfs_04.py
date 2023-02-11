# link: https://school.programmers.co.kr/learn/courses/30/lessons/60058
# solution: https://medium.com/@dltkddud4403/2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B4%84%ED%98%B8-37ad7be7acd6

def checkIfValid(str):
    stack = []
    for item in str:
        if not stack or item == "(":
            stack.append(item)
        else:
            if stack[-1] == "(":
                stack.pop()
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def isBalanced(s):
    check = 0
    for char in s:
        if char == "(":
            check += 1
        else:
            check -= 1
    if check == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    u = v = ''

    if len(p) == 0 or checkIfValid(p):
        return p

    for i in range(2, len(p)+1, 2):
        if isBalanced(p[0:i]):
            u = p[0:i]
            v = p[i:len(p)]
            break

    if checkIfValid(u):
        answer += u + solution(v)
    else:
        answer += "(" + solution(v) + ")"
        for char in u[1:-1]:
            if char == "(":
                answer += ")"
            else:
                answer += "("

    return answer
