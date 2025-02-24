number = int(input())
paint_cost = []
for _ in range(number):
    paint_cost.append(list(map(int, input().split())))

for i in range(1,len(paint_cost)):
    for j in range(3):
        if (j==0):
            paint_cost[i][j] += min(paint_cost[i-1][1], paint_cost[i-1][2])
        elif (j==1):
            paint_cost[i][j] += min(paint_cost[i-1][0], paint_cost[i-1][2])
        elif (j==2):
            paint_cost[i][j] += min(paint_cost[i-1][0], paint_cost[i-1][1])

print(min(paint_cost[len(paint_cost)-1]))
    
        