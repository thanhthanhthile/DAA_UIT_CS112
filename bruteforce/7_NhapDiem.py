def findChildScore(result: list, arr_score, GPA, w, pos, sum):
    if pos == len(weight):
        if round(sum + 0.001, 1) == GPA:
            print(*result, sep=' ')
        return
    for x in arr_score:
        if x - int(x) == 0:
            result[pos] = int(x)
        else:
            result[pos] = x

        next_sum = sum + result[pos] * weight[pos]
        next_weight = w + weight[pos]
        if round(next_sum + 10 * (1 - next_weight) + 0.001, 1) < GPA or round(
                next_sum + 0.25 * (1 - next_weight) + 0.001, 1) > GPA:
            continue
        else:
            findChildScore(result, arr_score, GPA, next_weight, pos + 1, next_sum)


arr_score = [i / 100 for i in range(25, 1001, 25)]

n = int(input())
weight = []
for i in range(n):
    w = int(input()) / 100
    weight.append(w)
GPA = float(input())

result = [0 for i in weight]
findChildScore(result, arr_score, GPA, 0, 0, 0)
