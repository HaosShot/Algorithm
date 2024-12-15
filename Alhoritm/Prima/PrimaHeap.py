import heapq
import time 

def prima_heap(graph, start):
    V = set()              
    T = []                     
    min_heap = []                

    for neighbor, cost in graph[start]:
        heapq.heappush(min_heap, (cost, start, neighbor))

    V.add(start)  

    while min_heap and len(V) < len(graph):
        cost, v, w = heapq.heappop(min_heap)  

        if w not in V:  
            V.add(w)    
            T.append((v, w, cost))  

            for neighbor, e in graph[w]:
                if neighbor not in V:
                    heapq.heappush(min_heap, (e, w, neighbor))

    return T

graph = {
        'A': [('B', 200), ('C', 300)],
        'B': [('A', 200), ('C', 100), ('D', 400)],
        'C': [('A', 300), ('B', 100), ('D', 500)],
        'D': [('B', 400), ('C', 500)]
    }

s = 'A'
t = prima_heap(graph, s)

print("Минимальное остовное дерево:")
for edge in t:
    print(f"Ребро: {edge[0]} - {edge[1]}, стоимость: {edge[2]}")

start = time.time()
result = prima_heap(graph, 'A')
end = time.time()

print(f'Время: {end - start:3f}') # быстрее чем обычный Прима