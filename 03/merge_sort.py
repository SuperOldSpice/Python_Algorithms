def merge_count(A, p = 1, r = 5):
    if(p >= r):
        return (0)
    else:
        q = int((p + r)/2)
        x = merge_count(A, p, q)
        y = merge_count(A, q + 1, r)
        z = merge_split_count(A, p, q, r)
        #print("tree")
        #for i in range(p, r+1, 1):
        #    print(A[i], end = " ")
        #print("\n")
        #print("arr")
        #for i in range(6):
        #    print(A[i], end = " ")
        #print("\n")
        return (x + y + z)

def merge_split_count(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [i for i in range(n1 + 2)]
    R = [i for i in range(n2 + 2)]
    for i in range(1, n1 + 1, 1):
        L[i] = int(A[p + i -1])
    for j in range(1, n2 + 1, 1):
        R[j] = int(A[q + j])
    L[n1 + 1] = 999999
    R[n2 + 1] = 999999
    i = 1
    j = 1
    counter = 0
    for k in range(p, r + 1, 1):
        if(R[j] < L[i]):
            counter += (n1 - i + 1)
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
    return(counter)
