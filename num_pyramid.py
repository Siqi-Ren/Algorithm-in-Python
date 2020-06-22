""" This programme finds the optimised sum of path for a number pyramid"""
pyramid =[
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,17,13,24,11]
]
# Method 1: trace all paths and find the max path.
datas = [13]
total = 0
total_paths = []
def search(depth, y):
    if depth == 4:
        # using data slicing to append copied datas into total_paths
        total_paths.append(datas[:])
        global total
        total+=1
        return print(datas)
    # loop number below pyramid[depth][y]
    datas.append(pyramid[depth+1][y])
    search(depth+1, y)
    datas.pop()
    # loop number right and below pyramid[depth][y]
    datas.append(pyramid[depth+1][y+1])
    search(depth+1, y+1)
    datas.pop()

def max_path(total_paths):
    max = 0
    # sums =[]
    for index, i in enumerate(total_paths):
        # sums.append(sum(i))
        if sum(i) > max:
            max = sum(i)
            max_index = index
    print("Max path is index {},\npath is {},\nsum of path is {}".format(max_index,
                                                                         total_paths[max_index],
                                                                         max))

# Method 2: Use recursion to find max on tree.left and tree.right.
max_value = 0
info = {}
def search_max(depth,y):
    if depth == 4:
        return pyramid[depth][y]
    if "{}_{}".format(depth,y) in info:
        return info["{}_{}".format(depth,y)]
    else:
        left_max = search_max(depth+1, y)
        right_max = search_max(depth+1, y+1)
        max_value = max(pyramid[depth][y]+left_max, pyramid[depth][y]+right_max)
        info["{}_{}".format(depth,y)] = max_value
        return max_value
        # return max_value


# Method 3: using Dynamic programming
"""Dynamic programming different from recursion. Don't call self function within function"""
def search_dp():
    # if depth == 4:
    #     return pyramid[depth][y]
    for j in range(4, 0, -1):
        for i in range(j):
            pyramid[j-1][i] += max(pyramid[j][i], pyramid[j][i+1])
            # pyramid[depth][y] += max(search_dp(depth+1, y), search_dp(depth+1, y+1))
    return pyramid[0][0]


if __name__ == "__main__":
    print("Method 1")
    # Method 1: trace all paths and find the max path.
    search(0, 0)
    print("There are total {} paths.".format(total))
    max_path(total_paths)

    # Method 2: Use recursion to find max on tree.left and tree.right.
    print("\nMethod 2")
    print(search_max(0,0))
    print(info)

    # Method 3: using Dynamic programming
    print("\nMethod 3")
    print(search_dp())