"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
# import model from a module locate in current directory
sys.path.append('./')
from recursive_floyd import recursive_floyd_warshall
from iterative_floyd import iterative_floyd
from copy import deepcopy
from itertools import product 
from time import process_time

# Sample GRAPH definition; ensure to use deepcopy to reset the graph state for each test
NO_PATH = sys.maxsize
ORIGINAL_GRAPH = [
    [0,   7,  NO_PATH, 8],
    [NO_PATH,  0,  5,  NO_PATH],
    [NO_PATH, NO_PATH, 0,   2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

def performance_test(function_handle):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

    """

    # Reset the GRAPH to its original state before each test
    # to ensure both functions work on the same initial conditions
    global GRAPH
    GRAPH = deepcopy(ORIGINAL_GRAPH)

    # Start timing
    start_time = process_time()
    
    # Execute the function
    function_handle()
    
    # End timing
    end_time = process_time()
    
    # Output the elapsed time
    print(f"Time taken by {function_handle.__name__}: {end_time - start_time} seconds")

# Import functions (in this setup, assuming they are present in the current script)
"""
def recursive_floyd_warshall(k=0, i=0, j=0):
    if k == MAX_LENGTH:
        return
    if i == MAX_LENGTH:
        return recursive_floyd_warshall(k + 1, 0, 0)
    if j == MAX_LENGTH:
        return recursive_floyd_warshall(k, i + 1, 0)
    if GRAPH[i][k] != NO_PATH and GRAPH[k][j] != NO_PATH:
        GRAPH[i][j] = min(GRAPH[i][j], GRAPH[i][k] + GRAPH[k][j])
    recursive_floyd_warshall(k, i, j + 1)

    
def iterative_floyd():
    for intermediate, start_node,end_node\
    in product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        
           if start_node == end_node:
               GRAPH[start_node][end_node] = 0
               continue
           
           GRAPH[start_node][end_node] = min(GRAPH[start_node][end_node],
                                 GRAPH[start_node][intermediate] + GRAPH[intermediate][end_node] ) 
"""
MAX_LENGTH = len(ORIGINAL_GRAPH)

print ("Recursion Test Time")
performance_test(recursive_floyd_warshall)

print ("Iterative Test Time")
performance_test(iterative_floyd)

    


