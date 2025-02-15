N, M = map(int, input().split())
trees = list(map(int, input().split()))
max_height = max(trees)
min_height = 0

def cut_tree(height):
    log = 0
    for tree in trees:
        if (tree>height):
            log += (tree-height)
    return log

while min_height<=max_height:
    mid_height = (max_height+min_height)//2
    if (M>cut_tree(mid_height)):
        #자른 나무가 부족해서 자르는 높이를 낮춰야함
        max_height = mid_height-1
    elif (M<=cut_tree(mid_height)):
        #자른 나무가 많아서 자르는 높이를 높여야함
        min_height = mid_height+1
print(max_height)

