N = int(input())
A = list(map(int, input().split()))

# A = [50000, 50000, 25000, 75000]の入力があった時
# cnt = [0,0,...,cnt[25000],...,cnt[50000],...]となる
# cnt[25000]は出現回数1となり、cnt[50000]は2となる
cnt = [0 for i in range(N)]
for i in range(N):
    cnt[A[i]] += 1

# cnt配列を元にcnt[i] * cnt[100000 - i]の部分で場合の数を求める
# また、合計が100000になるものを検索し、あればAnswerにカウントする
Answer = 0
for i in range(1, 50000):
    Answer += cnt[i] * cnt[100000 - i]
Answer += cnt[50000] * (cnt[50000 - 1]) // 2

print(Answer)

