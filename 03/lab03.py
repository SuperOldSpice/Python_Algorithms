#my merge functions
from merge_sort import merge_count
from merge_sort import merge_split_count

#input
print("Write input file name:")
file_name = input()
arr = [[]]
input_file = open(file_name, "r")
output_file = open("output.txt", "w")
print("Write user number (starts with 1):")
user_number = input()
line = "Picked user number: " + user_number + "\n"
output_file.write(line)

#arrays creating
arr = [line.split() for line in (input_file)]
u, m = int(arr[0][0]), int(arr[0][1])
user = arr[int(user_number)]
invertions = [i+1 for i in range(int(m)+1)]

#algorithm
for i in range(1, u + 1, 1):
    if (i != int(user_number)):
        for j in range(1, m + 1, 1):
            invertions[int(user[j])] = arr[i][j]
        counter = merge_count(invertions, 1, m)
        arr[i] = i, counter

#insertion 
for i in range(2, u + 1, 1):
    key = arr[i]
    j = i - 1
    while(j > 0 and int(key[1]) < int(arr[j][1])):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

#output
for i in range(1, u + 1, 1):
    if(arr[i][0] != user_number):
        line = "user: " + str(arr[i][0]) + " invertions number: "
        line += str(arr[i][1]) + "\n"
        output_file.write(line)

#files closing
input_file.close()
output_file.close()

