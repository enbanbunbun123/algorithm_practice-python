def MergeSort(A):

    #配列の数が1にの時には、ソートの必要がないので、Aを返す
    if len(A) == 1:
        return A
    
    #配列Aの中央値を求め、半分に分割する
    m = len(A) // 2
    A_Dash = MergeSort(A[0:m])
    B_Dash = MergeSort(A[m:len(A)])

    #A'とB'配列のインデントを管理する
    c1 = 0
    c2 = 0
    C = []

    while(c1 < len(A_Dash) or c2 < len(B_Dash)):
        if c1 == len(A_Dash):
            #A'が空であれば、B'の配列の中で、もっと小さいものをCに追加
            #A'が空であるのなら、次はB'をCに追加していくので、c2に1を追加
            C.append(B_Dash[c2])
            c2 += 1
        elif c2 == len(B_Dash):
            #B'が空であれば、A'の配列の中で、もっと小さいものをCに追加
            #B'が空であるのなら、次はA'をCに追加していくので、c1に1を追加
            C.append(A_Dash[c1])
            c1 += 1
        else:
            #A'とB'を比べて、小さいほうをCに追加
            if A_Dash[c1] <= B_Dash[c2]:
                C.append(A_Dash[c1])
                c1 += 1
            else:
                C.append(B_Dash[c2])
                c2 += 1
    return C

A = list(map(int, input().split()))

Answer = MergeSort(A)
print(*Answer)