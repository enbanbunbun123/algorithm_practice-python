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
    
# 最小公倍数は以下の式のよって成立する
# 最小公倍数(LCM(a,b)) = |a*b|/最大公約数(GCM(a.b))
def least_common_multiple(A, B):
    return int((A * B) // greatest_common_devisor(A, B))

N = int(input())
A = list(map(int, input().split()))

R = least_common_multiple(A[0], A[1])
for i in range(2, N):
    least_common_multiple(R, A[i])

print(R)
