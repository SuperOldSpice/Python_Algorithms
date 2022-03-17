arr = []
arr = input().split()
n = len(arr)

for i in range(0, n, 1):
    arr[i] = int(arr[i])

for i in range(0, n - 1, 1):
    for j in range(0, n - 1, 1):
        if(arr[j] > arr[j + 1]):
            b = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = b

for i in range(0, n, 1):
    print(arr[i], end = " ")
