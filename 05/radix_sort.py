#radix sort
def radix_sort(A, d):
    if(d > 0):
        return(counting_sort(A, d))
    else:
        d = find_max_rank(A)
        for i in range(1, d + 1, 1):
            A = counting_sort(A, i)
        return(A)

#finds max rank
def find_max_rank(A):
    maxium = -9999999999999
    for i in range(len(A)):
        if(A[i] > maxium):
            maxium = A[i]
    i = 0
    while(maxium > 0):
        maxium = int(maxium / 10)
        i += 1
    return i

#counting sort
def counting_sort(A, d):
    rank_A = []
    for i in range(len(A)):
        rank_A.append(int(A[i]/pow(10, (d - 1))))
        rank_A[i] = rank_A[i] - (int(rank_A[i] / 10) * 10)
    C = []
    B = []
    for i in range(len(A)):
        C.append(0)
        B.append(0)
    for i in range(1, len(A)):
        C[rank_A[i]] += 1
    for i in range(1, len(A)):
        C[i] += C[i-1]
    for i in range(len(A) - 1, 0, -1):
        B[C[rank_A[i]]] = A[i] 
        C[rank_A[i]] -= 1
    return B
