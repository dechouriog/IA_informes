import time
from collections import deque
import tracemalloc


class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state        
        self.parent = parent      
        self.depth = depth        

    def path(self):
        node, p = self, []
        while node:
            p.append(node.state)
            node = node.parent
        return list(reversed(p))


class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return self.graph[state]

    def goal_test(self, state):
        return state == self.goal



def bfs(problem):
    frontier = deque([Node(problem.initial)])
    explored = set()

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node.path()

        explored.add(node.state)
        for child in problem.actions(node.state):
            if child not in explored and all(n.state != child for n in frontier):
                frontier.append(Node(child, node))
    return None



def dls(node, problem, limit):
    if problem.goal_test(node.state):
        return node
    elif limit == 0:
        return None
    else:
        for child in problem.actions(node.state):
            result = dls(Node(child, node, depth=node.depth+1), problem, limit-1)
            if result is not None:
                return result
    return None

def ids(problem):
    depth = 0
    while True:
        result = dls(Node(problem.initial), problem, depth)
        if result is not None:
            return result.path()
        depth += 1

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "H", "I"],
    "F": ["C", "J"],
    "G": ["D"],
    "H": ["E"],
    "I": ["E", "J"],
    "J": ["F", "I"]
}


if __name__ == "__main__":
    problem = Problem("A", "J", graph)



    tracemalloc.start()
    start = time.perf_counter()
    ruta_bfs = bfs(problem)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()


    tracemalloc.start()

    start1 = time.perf_counter()
    ruta_ids = ids(problem)
    end1 = time.perf_counter()
    current1, peak1 = tracemalloc.get_traced_memory()


    print("Ruta encontrada con BFS:", ruta_bfs)
    print("Ruta encontrada con IDS:", ruta_ids)

    print("Tiempo BFS:", end - start)
    print("Tiempo IDS:", end1 - start1)
    print("Memoria BFS: actual =", current, "bytes; pico =", peak, "bytes")
    print("Memoria IDS: actual =", current1, "bytes; pico =", peak1, "bytes")





    