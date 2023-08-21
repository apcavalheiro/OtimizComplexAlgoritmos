import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    shortest_path = []
    node = end
    while node != start:
        shortest_path.append(node)
        node = min(graph[node], key=lambda x: distances[x] + graph[node][x])
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, distances[end]

start_node = 'D'
end_node = 'A'
shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)

print("Caminho mais curto:", shortest_path)
print("Distância:", shortest_distance)

