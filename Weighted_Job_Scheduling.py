# Find Connected Components
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020 

# This dynamic programming algorithm will find a maximum weight subset of mutually compatible jobs.
# Takes in n jobs: job i starts from S_i, finishes at T_i, and has the weight V_i.


import math

# Take in an array of lists [start, terminate, weight] that is len_array long.
# Return optimal weight achievable considering all jobs.


def dp_scheduling(array, len_array):
    array.sort(key=lambda elem: int(elem[1]))
    opt = [0]*len_array
    pre = [0]*len_array
    opt[0] = array[0][2]
    for k in range(1, len_array):
        pre[k] = binary_search(array, k, 0, k - 1)
        if array[k][0] < array[pre[k]][1]:
            opt[k] = max(opt[k-1], (array[k][2]))
        else:
            opt[k] = max(opt[k-1], (array[k][2]+opt[pre[k]]))
    return opt[len_array-1]

# Take in sorted array of jobs. Find largest element with termination time that is compatible with job k.

def binary_search(array, k, a, b):
    m = math.floor((a + b) / 2)
    if b <= a:
        return a
    elif array[m][1] <= array[k][0] < array[m + 1][1]:
        return m
    elif array[m][1] > array[k][0]:  # Termination of m is greater than start of k: check array prior to m.
        return binary_search(array, k, a, m)
    elif array[k][0] >= array[m+1][1]:  # Start of k is after termination of the array after m: check
        return binary_search(array, k, m+1, b)
    else:
        return -1


num_jobs = int(input())
jobs = []
for i in range(num_jobs):
    jobs.append([int(x) for x in input().split()])
print(dp_scheduling(jobs, num_jobs))
