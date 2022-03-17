"""
for both heaps
"""

def parent(i):
    return int(i/2)

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def index_last(A):
    return len(A) - 1

def insert(a):
    if a <= max(h_low):
        max_insert(h_low, a)
    else:
        min_insert(h_high, a)

    if len(h_low) > len(h_high) + 1:
        a = get_max(h_low)
        min_insert(h_high, a)
    elif len(h_high) > len(h_low) + 1:
        a = get_min(h_high)
        max_insert(h_low, a)
    
def find_median():
    if (len(h_low) + len(h_high)) % 2 == 0:
        return (maxium(h_low), minium(h_high))
    if len(h_high) > len(h_low):
        return minium(h_high)
    if len(h_low) > len(h_high):
        return maxium(h_low)

def list_to_string(A):
    new_str = "["
    for i in range(len(A)):
        if(i == (len(A) - 1)):
            new_str += " " + str(A[i])
        else:
            new_str += " " + str(A[i]) + ","
    new_str += " ]"
    return new_str

"""
for low heap
"""

h_low = []

def max_insert(A, a):
    A.append(a)
    i = index_last(A)
    while i > 1 and A[parent(i)] < A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

def max_heapify(A, i):
    p = left(i)
    q = right(i)
    if p < len(A) and A[p] > A[i]:
        largest = p
    else:
        largest = i
    if q < len(A) and A[q] > A[i]:
        largest = q
    if largest != i:
        A[i], A[largest] = A[largest], A[i]

def get_max(A):
    maxium = float('-inf')
    for i in range(1, len(A)):
        if A[i] > maxium:
            maxium = A[i]
            index = i
    A.pop(index)
    build_max_heap(A)
    return maxium 

def build_max_heap(A):
    n = int(len(A)/2)
    for i in range (n, 0, 1):
        max_heapify(A, i)

def maxium(A):
    maxium = float('-inf')
    for i in range(1, len(A)):
        if A[i] > maxium:
            maxium = A[i]
    return maxium 
        
"""
for high heap
"""

h_high = []

def min_insert(A, a):
    A.append(a)
    i = index_last(A)
    while i > 1 and A[parent(i)] > A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

def min_heapify(A, i):
    p = left(i)
    q = right(i)
    if p < len(A) and A[p] < A[i]:
        smallest = p
    else:
        smallest = i
    if q < len(A) and A[q] < A[i]:
        smallest = q
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]

def get_min(A):
    minium = float('inf')
    for i in range(1, len(A)):
        if(A[i]) < minium:
            minium = A[i]
            index = i
    A.pop(index)
    build_min_heap(A)
    return minium

def minium(A):
    minium = float('inf')
    for i in range(1, len(A)):
        if(A[i]) < minium:
            minium = A[i]
    return minium

def build_min_heap(A):
    n = int(len(A)/2)
    for i in range (n, 0, 1):
        min_heapify(A, i)
    
"""main function"""
def main():

    """input"""
    print("Write the file name:")
    file_name = "input.txt"
    #file_name = input()
    input_file = open(file_name, "r")
    output_file = open("output.txt", "w")
    n = int(input_file.readline())
    arr = [int(line) for line in input_file]
    h_low.insert(0,0)
    h_high.insert(0,0)
    

    """algorithms call"""
    for i in range(len(arr)):
        insert(arr[i])
        print_arr = arr[: i + 1]
        print_arr.sort()
        median = find_median()
        print("Array: ", print_arr)
        print("Low Heap:", h_low)
        print("High Heap:", h_high)
        print("Median", median, "\n")
        output_file.write("Step №" + str(i) + "\n")
        output_file.write("Array: " + list_to_string(print_arr) + "\n")
        output_file.write("Low Heap: " + list_to_string(h_low[1:]) + "\n")
        output_file.write("High Heap: " +  list_to_string(h_high[1:]) + "\n")
        output_file.write("Median: " + str(median) + "\n")
        output_file.write("\n\n" + "/////////////////////" + "\n\n\n")

    """output"""


    """close"""
    input_file.close()
    output_file.close()


main()
