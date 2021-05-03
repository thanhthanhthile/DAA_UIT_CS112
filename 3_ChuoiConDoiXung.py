string = input()

begin = 0
maxLen = 1
for i in range(1, len(string)):
    # truong hop abba
    left = i - 1
    right = i
    while left >= 0 and right < len(string) and string[left] == string[right]:
        if right - left + 1 > maxLen:
            begin = left
            maxLen = right - left + 1
        left -= 1
        right += 1
    # truong hop aba
    left = i - 1
    right = i + 1
    while left >= 0 and right < len(string) and string[left] == string[right]:
        if right - left + 1 > maxLen:
            begin = left
            maxLen = right - left + 1
        left -= 1
        right += 1
print(string[begin:begin + maxLen])
