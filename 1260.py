node, edge, start = map(int, input().split())
graph = {}
for i in range(edge):
    n, m = map(int, input().split())
    graph[n] = [graph[n], m]
    graph[m] = [graph[m], n]
print(graph)