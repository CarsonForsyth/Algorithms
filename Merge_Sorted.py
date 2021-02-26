# Merge Two Sorted Arrays
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020 

# Algorithm merges two sorted arrays of integers into a single sorted array in O(n).
# Input is a two lines, each a list of integers seperated by spaces.

input1 = [int(value) for value in input().split()]
input2 = [int(value) for value in input().split()]
output = [int(input1.pop(0)) + int(input2.pop(0))]

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

# Display merged array with leading number of elements, and spaces between each element.
print(*output)