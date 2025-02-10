N = int(input())
visited = []
complex_num = 0
apartment_num_list = []

for i in range(N):
    houses = list(map(int, list(input())))
    visited.append(houses)

for y in range(N):
    for x in range(N):
        if visited[x][y]==1:
            queue = [[x,y]]
            visited[x][y] = 0
            apartment_num = 1
            while queue:
                a,b = queue.pop(0)
                if a>0 and visited[a-1][b] == 1:
                    visited[a-1][b] = 0
                    queue.append([a-1, b])
                    apartment_num += 1
                if a<N-1 and visited[a+1][b] == 1:
                    visited[a+1][b] = 0
                    queue.append([a+1,b])
                    apartment_num += 1
                if b>0 and visited[a][b-1] == 1:
                    visited[a][b-1] = 0
                    queue.append([a, b-1])
                    apartment_num += 1
                if b<N-1 and visited[a][b+1] == 1:
                    visited[a][b+1] = 0
                    queue.append([a,b+1])
                    apartment_num += 1
            complex_num += 1
            apartment_num_list.append(apartment_num)    

print(complex_num)
apartment_num_list.sort()
for x in apartment_num_list:
    print(x)