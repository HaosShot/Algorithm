def mwis(g, w, n, A):
    if n in A:
        return A[n]

    if n == 0:
        return set()

    if n == 1:
        return {1}
    
    S1 = mwis(g, w, n - 1, A)
    w_S1 = sum(w[v] for v in S1)

    S2 = mwis(g, w, n - 2, A)
    S2 = S2 | {n}  
    w_S2 = sum(w[v] for v in S2)

    if w_S1 > w_S2:
        A[n] = S1
    else:
        A[n] = S2
 
    return A[n]

W = {1: 1, 2: 4, 3: 5, 4: 4}

n = len(W)  

graph = {i: i + 1 for i in range(1, n)}  
A = {}
result = mwis(graph, W, n, A)

print("Максимальное независимое множество:", result)
print("Суммарный вес:", sum(W[v] for v in result))
