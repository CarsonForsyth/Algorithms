# Find Connected Components
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020

# This is a dynamic programming algorithm to return the largest palindromic
# substring found in a given string. Table is filled as 
# row = start of sequence, column = end of sequence, value = length of sequence. 


input_string = input()
n = len(input_string)
# init dp table
dp_table = []
for row in range(n):
    this_row = []
    for column in range(n):
        if row == column:
            this_row.append(1)
        else:
            this_row.append(0)
    dp_table.append(this_row)
# fill out from bottom to top, table not needed below F(i,i)
for row in reversed(range(n-1)):
    for column in range(row+1, n):
        if input_string[row] == input_string[column]:
            dp_table[row][column] = dp_table[row+1][column-1] + 2
        else:
            dp_table[row][column] = max(dp_table[row+1][column], dp_table[row][column-1])
print(dp_table[0][n-1])
