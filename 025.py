N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Answer = 0
for i in range(N):
    Answer += (1/3) * A[i] + (2/3) * B[i]

print(Answer)