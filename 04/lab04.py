#algorithms import
from quick_sort_algorithms import quick_sort
from quick_sort_algorithms import median_quick_sort

#input
print("Write input file name:")
file_name = input()
input_file = open(file_name, "r")
open(file_name, "r")
output_file = open("output.txt", "w")
counter_1 = 0
arr_1 = [line.split() for line in input_file]
arr_1.insert(0,0)
arr_2 = [i for i in arr_1]


#algorithms call
counter_1 = quick_sort(arr_1, 1, len(arr_1) - 1)
counter_2 = median_quick_sort(arr_2, 1, len(arr_2) - 1)

#output
output_file.write("Simple quick sort: " + str(counter_1) + "\n")
output_file.write("Median quick sort: " + str(counter_2) + "\n")

#close
input_file.close()
output_file.close()

#for i in range(len(arr_1)):
   # print(arr_1[i], end = " ")

#for i in range (len(arr_2)):
    #print (arr_2[i], end = " ")
