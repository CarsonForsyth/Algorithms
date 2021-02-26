# Find Connected Components
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020 

# Traverse graph in reverse postlist order counting connected components.

from typing import List

# Declare global variables.
num_connected = 0
post_list: List[int] = []
visited_vertices = []

# Depth first search algorithm to create postlist and count connected components of adjacency_list.
def dfs(adjacency_list, num_vert, explore_order):
    global visited_vertices
    global num_connected
    global post_list
    num_connected = 0
    visited_vertices = [-1] * num_vert
    post_list = []
    
    for vertex in explore_order:
        if visited_vertices[vertex] == -1:
            num_connected += 1
            explore(adjacency_list, vertex, num_vert)
    return


def explore(adjacency_list, vertex, num_vert):
    global post_list
    global num_connected
    global visited_vertices
    visited_vertices[vertex] = num_connected
    
    for edge in adjacency_list[vertex]:
        if visited_vertices[edge] == -1:
            explore(adjacency_list, edge, num_vert)
    
    post_list.append(vertex)
    return

# Return post order of graph to create new specific order of graph.
def get_post_list():
    return post_list

# Return number of connected components found from adjacency_list in order of explore_order.
def get_connected():
    return num_connected




numV, numE = [int(vertex) for vertex in input().split(" ") if vertex.isdigit()]

# From input get all edges to build an adjacency_list, and reverse_adjacency_list.
adjacency_list = [[]]*numV
reverse_adjacency_list = [[]]*numV
for edge in range(numE):
    vertex1, vertex2 = [int(vertex) for vertex in input().split(" ") if vertex.isdigit()]
    if not adjacency_list[vertex1-1]:
        adjacency_list[vertex1-1] = [vertex2-1]
    else:
        adjacency_list[vertex1-1].append(vertex2-1)
    if not reverse_adjacency_list[vertex2-1]:
        reverse_adjacency_list[vertex2-1] = [vertex1-1]
    else:
        reverse_adjacency_list[vertex2-1].append(vertex1-1)

# Perform DFS on reverse_adjacency_list in any order to get post_order of GR.
dfs(reverse_adjacency_list, numV, range(numV))
post_order = get_post_list()

# Perform DFS on adjacency_list in reverse post_order to find all strongly connected components in G.
post_order.reverse()
dfs(adjacency_list, numV, post_order)

# Output number of connected components.
print(get_connected())
