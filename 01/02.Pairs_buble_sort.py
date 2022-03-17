a = []
a = input().split()
n = len(a)

for i in range(0, n, 1):
    a[i] = int(a[i])

for i in range(n - 1):
    for j in range(n - 1):

        key = 0
        
        if( (a[j] % 2 != 0) and (a[j + 1] % 2 == 0) ):
            key = 1
            
        if( (a[j] % 2 != 0) and (a[j] % 2 != 0) and (a[j] < a[j + 1]) ):
            key = 1

        if( (a[j + 1] % 2 == 0) and (a[j] % 2 == 0) and (a[j] > a[j + 1])):
            key = 1

        if( key ):
            b = a[j]
            a[j] = a[j + 1]
            a[j + 1] = b

for i in range(0, n, 1):
    print(a[i], end = " ")
