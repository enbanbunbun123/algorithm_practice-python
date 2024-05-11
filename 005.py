# 与えられた数の合計を100で割った余りを求める
def multipy_mod():
    N = int(input())
    A = list(map(int, input().split()))

    total = 0
    for i in range(N):
        total += A[i]

    Answer = total % 100
    return Answer

result = multipy_mod()
print(result)