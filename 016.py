def greatest_common_devisor(A, B):
    while A >= 1 and B >= 1:
        if A > B:
            A = A % B
        else:
            B = B % A

    if A >= 1:
        return A
    else:
        return B
    
N = int(input())
A = list(map(int, input().split()))

R = greatest_common_devisor(A[0], A[1])
for i in range(2, N):
    R = greatest_common_devisor(R, A[i])

print(R)