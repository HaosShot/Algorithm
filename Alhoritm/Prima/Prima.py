import time

def prima(graph, start):
    X = {start}  
    T = []       

    while len(X) < len(graph):  
        min_edge = None
        min_cost = float('inf')

        for v in X:
            for w, cost in graph[v]:
                if w not in X and cost < min_cost: 
                    min_edge = (v, w)
                    min_cost = cost

        if min_edge:
            v, w = min_edge
            T.append((v, w, min_cost))  
            X.add(w) 

    return T

graph = {
        'A': [('B', 1), ('C', 300)],
        'B': [('A', 100), ('C', 400), ('D', 200)],
        'C': [('A', 300), ('B', 400), ('D', 500)],
        'D': [('B', 200), ('C', 500)]
}
s = 'A'
mst = prima(graph, s)
    
print("Минимальное остовное дерево:")
for edge in mst:
    print(f"Ребро: {edge[0]} - {edge[1]}, стоимость: {edge[2]}")

start = time.time()
result = prima(graph, 'A')
end = time.time()

print(f'Время: {end - start:3f}')# медленее 