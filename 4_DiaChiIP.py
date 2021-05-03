string = input()
for i in range(1, 4):
    for j in range(i + 1, i + 4):
        for k in range(j + 1, j + 4):
            if k >= len(string):
                break
            a = int(string[:i])
            b = int(string[i:j])
            c = int(string[j:k])
            d = int(string[k:])
            if a <= 255 and b <= 255 and c <= 255 and d <= 255 \
                    and str(a) == string[:i] and str(b) == string[i:j] and str(c) == string[j:k] and str(d) == string[k:]:
                result = ".".join([str(a), str(b), str(c), str(d)])
                print(result)