
global wolves, low, num, graph, cnt

#graph=[[15, 35, 42, 22, 49, 7, 21, 24, 23, 46], [47, 25, 11, 4, 13, 12], [42, 21, 6, 45, 15, 46, 35, 24, 49, 40], [16, 29, 8, 41, 27, 48, 44, 26, 39], [18, 9, 25, 19, 1], [38, 46, 42, 24, 45, 33, 35], [7, 23, 33, 42, 2, 38], [22, 6, 45, 23, 0, 15, 42], [14, 32, 27, 48, 3, 41, 16, 26, 30, 39, 29, 10, 37, 31], [4, 17, 13, 36], [49, 31, 39, 32, 16, 29, 14, 8], [36, 47, 1, 34, 19, 12, 17], [25, 19, 34, 13, 36, 1, 11, 18], [19, 20, 9, 36, 12, 1], [27, 8, 37, 30, 44, 10, 48, 31], [24, 0, 22, 2, 7, 45, 33, 38], [37, 3, 8, 28, 10, 32, 44], [9, 34, 47, 20, 25, 11], [20, 4, 47, 12], [12, 13, 4, 11, 36, 47, 20], [28, 18, 13, 47, 36, 17, 25, 19], [2, 49, 35, 33, 0, 24, 45], [35, 7, 15, 0, 45, 23, 42], [6, 43, 7, 38, 22, 35, 40, 0, 42], [45, 15, 42, 5, 46, 40, 35, 2, 33, 21, 0, 38], [1, 12, 4, 36, 17, 20], [41, 28, 8, 3], [48, 14, 8, 37, 3, 32, 44, 28], [20, 26, 30, 44, 16, 27, 31], [3, 44, 31, 10, 8, 39, 48, 37], [28, 37, 32, 14, 8], [10, 32, 29, 37, 39, 14, 28, 8], [8, 31, 30, 10, 41, 27, 37, 16], [40, 38, 6, 42, 35, 24, 21, 5, 15], [17, 36, 12, 11], [0, 22, 42, 24, 21, 2, 33, 23, 46, 5], [34, 11, 13, 25, 12, 20, 9, 19], [30, 16, 14, 31, 48, 27, 8, 32, 29], [33, 5, 49, 45, 23, 43, 15, 6, 24], [10, 41, 8, 29, 31, 48, 3], [43, 33, 24, 2, 45, 23], [39, 26, 8, 3, 32], [46, 2, 0, 5, 33, 6, 24, 35, 49, 22, 7, 43, 23], [23, 40, 46, 45, 38, 42], [29, 48, 28, 14, 3, 27, 16], [49, 24, 7, 38, 5, 2, 43, 22, 15, 40, 46, 21], [5, 42, 43, 24, 2, 35, 45, 0], [11, 1, 18, 20, 17, 19], [44, 27, 8, 37, 3, 14, 29, 39], [10, 45, 21, 38, 0, 42, 2]]

graph=[[1,3],[2],[0], [4], [5], [3]]

num = [-1 for i in range(50)]
low = [-1 for i in range(50)]
cnt = 0


wolves = []
def dfs(u, par):
    global cnt, wolves, graph
    cnt += 1 
    num[u] = cnt
    low[u] = cnt 
    for v in graph[u]:
        if v != par :
            if num[v] != -1:
                low[u] = min(low[u], num[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                print(f"u: {u} v: {v}")
                print(f"num[u]: {num[u]} low[u]: {low[u]}")
                print(f"num[v]: {num[v]} low[v]: {low[v]}")
                if num[v] == low[v]:
                    
                    if not (v in wolves):
                        wolves.append(v)
                    if not (u in wolves):
                        wolves.append(u)

dfs(0, -1)
                   
print(wolves)