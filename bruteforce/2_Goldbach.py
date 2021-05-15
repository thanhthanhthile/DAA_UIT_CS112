# Mang primes gom cac phan tu True va False, index cua phan tu mang gia tri True la so nguyen to
def get_primes(n):
    primes = [True for i in range(0, n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] == True:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return primes


n = int(input())
primes = get_primes(n)
count = 0
for i in range(n // 2, n):
    if primes[i] and primes[n - i]:
        count += 1
print(count)
