def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
