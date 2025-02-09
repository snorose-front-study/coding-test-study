w, h = map(int, input().split())
while (w!=0 and h!=0):
    graph = []
    islands = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for y in range(h):
        for x in range(w):
            queue = []
            if graph[y][x]==1:
                queue.append([x,y])
                graph[y][x]=0
                while queue:
                    a,b = queue.pop(0)
                    if a>0 and graph[b][a-1]==1:
                        graph[b][a-1]=0
                        queue.append([a-1,b])
                    if a<w-1 and graph[b][a+1]==1:
                        graph[b][a+1]=0
                        queue.append([a+1,b])
                    if b>0 and graph[b-1][a]==1:
                        graph[b-1][a]=0
                        queue.append([a,b-1])
                    if b<h-1 and graph[b+1][a]==1:
                        graph[b+1][a]=0
                        queue.append([a,b+1])
                    if a>0 and b>0 and graph[b-1][a-1]==1:
                        graph[b-1][a-1]=0
                        queue.append([a-1,b-1])
                    if a>0 and b<h-1 and graph[b+1][a-1]==1:
                        graph[b+1][a-1]=0
                        queue.append([a-1,b+1])
                    if a<w-1 and b>0 and graph[b-1][a+1]==1:
                        graph[b-1][a+1]=0
                        queue.append([a+1,b-1])
                    if a<w-1 and b<h-1 and graph[b+1][a+1]==1:
                        graph[b+1][a+1]=0
                        queue.append([a+1,b+1])
                islands += 1
    print(islands)
    w, h = map(int, input().split())