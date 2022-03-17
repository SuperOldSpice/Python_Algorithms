#simple quick sort
def quick_sort(A, p, r):
    if(p < r):
        #print ("\n" + str(p) + " " + str(r))
        z, q = partition(A, p, r)
        #for i in range (len(A)):
           # print (A[i], end = " ")
        x = quick_sort(A, p, q - 1)
        y = quick_sort(A, q + 1, r)
        return (x + y + z)
    else:
        return 0

def partition(A, p, r):
    counter = 0
    x = A[r][0]
    i = p - 1
    for j in range(p, r, 1):
        counter += 1
        if(int(A[j][0]) < int(x)):
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return counter, i + 1

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

#median quick sort
def median_quick_sort(A, p, r):
    if(p < r):
        #print ("\n" + str(p) + " " + str(r))
        if(r - p + 1 > 3):
            z, q = median_partition(A, p, r)
        else:
            z, q = partition(A, p, r)
        #for i in range (len(A)):
            #print (A[i], end = " ")
        x = median_quick_sort(A, p, q - 1)
        y = median_quick_sort(A, q + 1, r)
        return (x + y + z)
    else:
        return 0

def median_partition(A, p, r): 
    n = find_median(A, p, r)
    #print("median", p, r, n)
    swap(A, n, r)
    counter = 0
    x = A[r][0]
    i = p - 1
    for j in range(p, r, 1):
        counter += 1
        if(int(A[j][0]) < int(x)):
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return counter, i + 1

def find_median(A, p, r):
    
    q1 = int(A[p][0])
    q2 = int(A[int((p+r)/2)][0])
    q3 = int(A[r][0])
    
    if((q1 <= q2 and q1 >= q3) or (q1 >= q2 and q1 <= q3)):
        return p
    
    elif((q2 <= q1 and q2 >= q3) or (q2 >= q1 and q2 <= q3)):
        return int((p+r)/2)
    
    elif((q3 <= q1 and q3 >= q2) or (q3 >= q1 and q3 <= q2)):
        return r

    
    
