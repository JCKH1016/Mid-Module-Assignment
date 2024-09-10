import unittest
from sys import maxsize
import sys
sys.path.append('./')
from recursive_floyd import recursive_floyd_warshall

NO_PATH = maxsize

GRAPH = [[0,   7,  NO_PATH, 8],
[NO_PATH,  0,  5,  NO_PATH],
[NO_PATH, NO_PATH, 0,   2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])

def run_floyd_warshall(input_graph):
    graph = [row[:] for row in input_graph]  # Create a copy of the input graph
    def recursive_floyd_warshall(k=0, i=0, j=0):
        if k == len(graph):
            return
        if i == len(graph):
            return recursive_floyd_warshall(k+1, 0, 0)
        if j == len(graph):
            return recursive_floyd_warshall(k, i+1, 0)
        if graph[i][k] != NO_PATH and graph[k][j] != NO_PATH:
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        return recursive_floyd_warshall(k, i, j+1)
    
    recursive_floyd_warshall()
    return graph

class TestRecursiveFloydWarshall(unittest.TestCase):

    def test_basic_case(self):
        graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected = [
            [0, 7, 12, 8],
            [maxsize, 0, 5, 7],
            [maxsize, maxsize, 0, 2],
            [maxsize, maxsize, maxsize, 0]
        ]
        result = run_floyd_warshall(graph)
        self.assertEqual(result, expected)

    def test_empty_graph(self):
        graph = []
        expected = []
        result = run_floyd_warshall(graph)
        self.assertEqual(result, expected)

    def test_negative_weights(self):
        graph = [
            [0, 1, NO_PATH],
            [NO_PATH, 0, -1],
            [1, NO_PATH, 0]
        ]
        expected = [
            [0, 1, 0],
            [0, 0, -1],
            [1, 2, 0]
        ]
        result = run_floyd_warshall(graph)
        self.assertEqual(result, expected)
        
    def test_all_zeros_except_diagonal(self):
        graph = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = run_floyd_warshall(graph)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
