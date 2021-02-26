# Merge-sort for an Array
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020 

# An algorithm for merge-sort to sort an array on O(nlogn).
# Input is given as a line containing number of integers in array, followed by
# A line of integers for the array, seperated by a space

import math


# Define function to merge two correctly sorted arrays.
def merge_two_sorted_arrays(input1, input2):
    output = []
    # While input1 or input2 contain values, continue appending sorted values to output.
    while (len(input1) or len(input2)):
        # If input2 contains no values, pop  lowest value from input1 to output.
        # Else if input1 contains elements, and the lowest value of input1
        # is less than that of input2, pop lowest value from input2 to output.
        # Else, input2 should be popped to output.
        if (len(input2) == 0):
            output.append(input1.pop(0))
        elif ((len(input1) > 0) and (input1[0] <= input2[0])):
            output.append(input1.pop(0))
        else:
            output.append(input2.pop(0))
    return output

# Define function to divide and conquer the sorting of the array.
# Return only single element at base case, else split up array and recombine using merge_two_sorted_arrays.
def merge_sort(size, array):
    # Base case: array is split into only one element, return element.
    if (size <= 1):
        return array
    # Otherwise seperate array in half, and merge_sort each half of the array.
    else:
        index = math.floor(size/2)
        subArray1 = merge_sort(int(index), array[0:index])
        subArray2 = merge_sort(int(size-index), array[index:])
        return merge_two_sorted_arrays(subArray1, subArray2)

# Line one contains size of array to be sorted.
inputSize = int(input())
# Line two of input contains string of array elements.
inputArray = [int(value) for value in input().split()]

# Output sorted array, elements seperated by spaces. Trailing space necessary to match cases.
output = ""
for element in merge_sort(inputSize, inputArray):
    output += str(element) + ' '
print(output)