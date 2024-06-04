#与えられた数字が素数かどうか判定する
def can_prime_factorization(N):
    Answer = []
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        while N % 2 == 0:
            N /= i
            Answer.append(i)

        if N >= 2:
            Answer.append(N)

    return Answer

N = int(input())
result = can_prime_factorization(N)
print(result)