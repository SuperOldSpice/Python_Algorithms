#algorithms import
from radix_sort import radix_sort 

#input
print("Write input file name:")
file_name = input()
input_file = open(file_name, "r")
output_file = open("output.txt", "w")
arr = [int(line) for line in input_file]
arr.insert(0,0)
print("Wanna pick the d? (y/n):")
d = input()
if(d == "y" or d == "yes"):
    print("Input the d:")
    d = int(input())
else:
    d = 0

#algorithm
arr = radix_sort(arr, d)

#output
for i in range(1, len(arr)):
    output_file.write(str(arr[i]) + "\n")

#close
input_file.close()
output_file.close()
