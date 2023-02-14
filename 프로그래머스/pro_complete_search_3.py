def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    digits = list(numbers)
    arr = []
    
    def dfs(i, cur, digits):
        nonlocal arr
        if i == len(digits):
            return
        arr.append(cur+digits[i])
        arr.append(digits[i]+cur)
        
        dfs(i+1, cur+digits[i], digits)
        dfs(i+1, digits[i]+cur, digits)
        
    dfs(-1, "", digits)
    
    result = set()
    for num in arr:
        cur_val = int(num)
        if cur_val >=2 and isPrime(cur_val):
            result.add(cur_val)
    # print(result)
    return len(result)
