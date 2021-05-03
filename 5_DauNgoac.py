def backtracking(A, i, n, opened):
    if opened == n:
        print(A + (2 * n - i) * ')')
        return
    S = {'('}
    if opened > 0:
        S.add(')')
    for x in S:
        # Debug = tay chetmie moi ra duoc cai dieu kien nay do nhaaaa
        if opened >= i - opened:
            backtracking(A + x, i + 1, n, opened + (x == '('))


n = int(input())
A = ''
i = 0
opened = 0
backtracking(A, i, n, opened)