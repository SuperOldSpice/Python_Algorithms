a = []
a = input().split()
n = len(a)

for i in range(0, n, 1):
    a[i] = int(a[i])

for i in range(1, n, 1):
    
    j = i - 1
    b = a[i]
    key = 0
        
    if( (a[j] % 2 != 0) and (a[j + 1] % 2 == 0) ):
        key = 1
            
    if( (a[j] % 2 != 0) and (a[j] % 2 != 0) and (a[j] < a[j + 1]) ):
        key = 1

    if( (a[j + 1] % 2 == 0) and (a[j] % 2 == 0) and (a[j] > a[j + 1])):
        key = 1

    while( j > -1 and key):
    
        a[j + 1] = a[j]
        a[j] = b
        j = j - 1
        key = 0
        
        if( (a[j] % 2 != 0) and (a[j + 1] % 2 == 0) ):
            key = 1
            
        if( (a[j] % 2 != 0) and (a[j] % 2 != 0) and (a[j] < a[j + 1]) ):
            key = 1

        if( (a[j + 1] % 2 == 0) and (a[j] % 2 == 0) and (a[j] > a[j + 1])):
            key = 1

for i in range(0, n, 1):
    print(a[i], end = " ")
