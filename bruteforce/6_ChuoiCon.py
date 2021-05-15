def isPalindrome(string):
    return string == string[::-1]


def backtracking(A: list, start, n, string):
    if start == n:
        print(*A)
        return
    for i in range(start, n):
        if isPalindrome(string[start:i + 1]):
            backtracking(A + [string[start:i+1]], i + 1, n, string)


string = input()
n = len(string)
A = []
backtracking(A, 0, n, string)
