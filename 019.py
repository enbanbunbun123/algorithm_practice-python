N = int(input())
A = list(map(int, input().split()))

R = 0
G = 0
B = 0
for i in range(N):
    if A[i] == 1:
        R += 1
    if A[i] == 2:
        G += 1
    if A[i] == 3:
        B += 1

conbination_R = (R * (R-1)) / 2
conbination_G = (G * (G-1)) / 2
conbination_B = (B * (B-1)) / 2

result = conbination_R + conbination_G + conbination_B
print(result)