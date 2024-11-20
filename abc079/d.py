import heapq

def dijkstra(graph, start, end):
    inf = 10 ** 18
    n = len(graph)
    distances = [inf] * n
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
      init_distance, position = heapq.heappop(queue)
      
      if position == end:
          return distances[end]
      if distances[position] < init_distance:
          continue
      
      for destination, cost in graph[position]:
          dist = init_distance + cost
          if dist < distances[destination]:
              distances[destination] = dist
              heapq.heappush(queue, [dist, destination])

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in [0] * 10]
A = [list(map(int, input().split())) for _ in [0] * H]

G = [[] for _ in [0] * 10]
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        G[i].append([j, C[i][j]])

inf = 10 ** 18
change_cost = []
for i in range(10):
    change_cost.append(dijkstra(G, i, 1))

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1:
            continue
        ans += change_cost[A[i][j]]

print(ans)