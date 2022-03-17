import numpy as np
import random
from shedule_build import plot_data
sizes = [10, 100]               #array sizes
types = ["random", "best", "worst"]
data_plot = {'random': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}, #collection for operation numbers
             'best': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}},
             'worst': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}}

def generate_data(n, gen_type = "random"):      #function, that generate arrays
    if gen_type=="best":
        a = [i+1 for i in range(n)]
        return a
    elif gen_type=="worst":
        a = [i+1 for i in reversed(range(n))]
        return a
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
        return a

def bubble_sort(arr):                           #simple slow bubble sort
    counter = 0
    for i in range(0, len(arr) - 1, 1):
        for j in range(0, len(arr) - 1, 1):
            counter += 1
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return counter

def bubble_impr_sort(arr):                      #func for improve_buble_sort
    counter = 0
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, len(arr) - 1, 1):
            counter = counter + 1
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return counter

def insertion_sort(arr):                        #insertion sort
    counter = 0
    for i in range(1, len(arr), 1):             
        j = i - 1
        b = arr[i]
        while( j > 0 and arr[j] > b):
            counter = counter + 1
            arr[j + 1] = arr[j]
            arr[j] = b
            j = j - 1
        counter = counter + 1
    return counter
        
for n in sizes:                                  #loop, that input operation numbers into the collection and print them
    print ("\nDATA SIZE: ", n)
    for gen_type in types:
        print ("\n\tDATA TYPE:", gen_type)
        data = generate_data(n, gen_type)
        data_bubble = np.copy(data)
        bubble_op_count = bubble_sort(data_bubble)
        print ("\tBubble sort operation count:", int(bubble_op_count))
        data_plot[gen_type]['bubble'][n] = bubble_op_count
        data_bubble_impr = np.copy(data)
        bubble_impr_op_count = bubble_impr_sort(data_bubble_impr)
        print ("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count
        data_insertion = np.copy(data)
        insertion_op_count = insertion_sort(data_insertion)
        print ("\tInsertion sort operation count:", int(insertion_op_count))
        data_plot[gen_type]['insertion'][n] = insertion_op_count
    plot_data(data_plot, logarithmic=True, oneplot=True) 
        

#print(data_plot)           
