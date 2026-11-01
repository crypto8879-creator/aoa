
#kruskal
def kruskal(edges, vertices):

    edges.sort()
    parent = list(range(vertices))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    cost = 0

    print("Selected Edges:")

    for w, u, v in edges:

        a = find(u)
        b = find(v)

        if a != b:
            print(u, "-", v, ":", w)
            cost += w
            parent[a] = b

    print("Minimum Cost:", cost)


# Main program
edges = [
    (1, 0, 1),
    (2, 0, 2),
    (3, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]

kruskal(edges, 4)
#prims
def prim(graph, vertices):

    visited = [0] * vertices
    visited[0] = 1

    cost = 0

    print("Selected Edges:")

    for i in range(vertices - 1):

        minimum = 999
        x = 0
        y = 0

        for u in range(vertices):
            if visited[u]:
                for v in range(vertices):
                    if graph[u][v] != 0 and not visited[v]:

                        if graph[u][v] < minimum:
                            minimum = graph[u][v]
                            x = u
                            y = v

        print(x, "-", y, ":", minimum)

        cost += minimum
        visited[y] = 1

    print("Minimum Cost:", cost)


# Main program
graph = [
    [0, 1, 2, 0],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [0, 4, 5, 0]
]

prim(graph, 4)
#dijkstra
import heapq

def dijkstra(graph, start):

    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    queue = [(0, start)]

    while queue:

        dist, node = heapq.heappop(queue)

        if dist > distance[node]:
            continue

        for neighbour, weight in graph[node].items():

            new_dist = dist + weight

            if new_dist < distance[neighbour]:
                distance[neighbour] = new_dist
                heapq.heappush(queue, (new_dist, neighbour))

    print("Shortest Distances:", distance)


# Main program
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

dijkstra(graph, 'A')
