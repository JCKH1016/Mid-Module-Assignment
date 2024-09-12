# PRACTICAL ASSIGNMENT: PROGRAMMING
# Floyd Warshall Algorithm
=================================================

## Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Explanation](#explanation)
- [Example](#example)

## Background
The Floyd Warshall algorithm is an example of dynamic programming. It is used to find shortest paths between all pairs of vertices in a graph with positive or negative edge weights. It is a dynamic-programming algorithm; shortest path distances are calculated bottom up, these estimates are refined until the shortest path is obtained. Positive and zero weight cycles in the graph are ignored, and negative weight cycles are detected.

This repository contains Python implementations of the Floyd-Warshall algorithm using both iterative and recursive approaches. The Floyd Warshall Algorithm was given in iterative version.The tasks is to rewirte the algorithm as recursive version. Additionally, performance testing and unit testing are included for implementations.

## Install

Clone the repository to local directory:

git clone git@github.com:JCKH1016/Mid-Module-Assignment.git

Install dependencies as requirements.txt required.

## Usage
#Running Floyd Warshall Algorithm in iterative version
To run the iterative implementation, execute the following script:

python iterative_floyd.py


#Running Floyd Warshall Algorithm in recursive version
To run the recursive implementation, execute the following script:

python recursive_floyd.py

#Running Performance Tests
To run the performance tests for both the iterative and recursive implementations, execute the following script:

python performance_test.py

#Running Unit Tests
To execute the unit tests, run the following command:

python -m unittest test_floyd_warshall.py

This command will discover and run all the tests defined in the test_floyd_warshall.py.


## Explanation
Floyd Warshall Algoritham - Iterative version 

The iterative version is given by the task, it employs three nested loops to systematically evaluate every possible path between nodes while considering each node as an intermediate point. Using the product function from itertools makes the code cleaner and more concise, facilitating better readability.

Floyd Warshall Algoritham - Recursive version

The exercise requies us to rewrite the algorithm recursively. The recursive Floyd-Warshall algorithm is a depth-first search approach that minimizes the distance between every pair of nodes by considering all possible intermediate nodes. 

Base Case and Recursion:
- If k reaches MAX_LENGTH, the recursion ends as all nodes are processed.
- If i reaches MAX_LENGTH, proceed to the next intermediate node k.
- If j reaches MAX_LENGTH, proceed to the next starting node i.

Distance Calculation: For each pair (i, j), it checks if there is a shorter path through an intermediate node k. If a shorter path exists, it updates the distance in the adjacency matrix (GRAPH).

This design handles the recursive logic and processes the Floyd-Warshall algorithm without loops. 

## Example
Output Example

When you run performance_test.py, you may see output similar to:


Recursion Test Time
Time taken by recursive_floyd_warshall: 2.0999999999993246e-05 seconds


Iterative Test Time
Time taken by iterative_floyd: 0.00018899999999999473 seconds



Command Examples
To check the output of the distance from each node to every other node using the default graph, you can run:


python main.py


This will print the shortest distances as per both the recursive and iterative implementations. 


Expected Output for the Default Graph
For the default graph provided in the implementation:


Distance from Node 0 to Node 0 is 0

Distance from Node 0 to Node 1 is 7

Distance from Node 0 to Node 2 is 12

Distance from Node 0 to Node 3 is 8

Distance from Node 1 to Node 0 is No Path

Distance from Node 1 to Node 1 is 0

Distance from Node 1 to Node 2 is 5

Distance from Node 1 to Node 3 is 7

...

This output details the shortest path from every node to every other node based on the initial definitions in the GRAPH variable.
