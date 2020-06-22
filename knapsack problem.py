''' Problem statement : https://en.wikipedia.org/wiki/Knapsack_problem#:~:text=The%20knapsack%20problem%20is%20a,is%20as%20large%20as%20possible.
'''

# use 2d list to store items weight and value
info = [[3,8],
        [2,5],
        [5,12]]

# Method 1: use search for all combinations of items to find the optimised knapsack, ie max value.
selected = []
max_selected = []
max_value = 0

def search(depth,rest):
    if depth == 3:
        print(selected)
        # use for loop to get values, alternatively, list comprehension should be working as well.
        values = []
        for index, select in enumerate(selected):
            values.append(select*info[index][1])
        global max_value
        global max_selected
        if sum(values) > max_value:
            max_value = sum(values)
            # use selected[:] to make a copy of selected
            max_selected = selected[:]
    else:
        # if not put in current item
        selected.append(0)
        search(depth+1, rest)
        selected.pop()

        # if put in current item
        if rest >= info[depth][0]:
            selected.append(1)
            search(depth+1, rest - info[depth][0])
            selected.pop()


# Method 2: use search to find the optimised knapsack, max value.
# Function return is weight.
mem = {}
def search_2(depth, rest):
    if "{}_{}".format(depth, rest) in mem:
        return mem["{}_{}".format(depth, rest)]
    if depth == 2:
        if rest >= info[depth][0]:
            data = info[depth][1]
        else:
            data = 0
    else:
        values = []
        values.append(search_2(depth+1, rest))
        if rest >= rest - info[depth][0]:
                values.append(search_2(depth+1, rest-info[depth][0])+info[depth][1])
        print(values)
        data = max(values)

    if "{}_{}".format(depth, rest) not in mem:
        mem["{}_{}".format(depth, rest)] = data

    return data

# Method 3: search dynamic programming, bottom-up
# def search_dp(total):
total = 5
pre_max = []
for k in range(len(info)-1, -1, -1):
    # pre_max = [0]
    new_pre_max = [0]
    start = 1
    if k == 0:
        start = total
    for j in range(start, total + 1):
        value_list = []
        for i in range(0, j + 1):
            if i >= info[k-1][0]:
                value_list.append(info[k-1][1] + pre_max[j - i])
            else:
                value_list.append(pre_max[j - i])
        new_pre_max.append(max(value_list))
pre_max = new_pre_max


# # depth == 2，老三
# total = 5
# pre_max = []
# for i in range(0, info[-1][0]):
#     pre_max.append(0)
# for i in range(info[-1][0], total+1):
#     pre_max.append(info[-1][1])
# # depth == 1 老二
# new_pre_max = [0]
# for j in range(1, total+1):
#     value_list = []
#     for i in range(0, j+1):
#         if i >= info[-2][0]:
#             value_list.append(info[-2][1]+pre_max[j-i])
#         else:
#             value_list.append(pre_max[j-i])
#     new_pre_max.append(max(value_list))
#
#  # depth == 0 老大
# new_pre_max2 = [0]
# for j in range(total, total+1):
#     value_list = []
#     for i in range(0, j+1):
#         if i >= info[-3][0]:
#             value_list.append(info[-3][1]+new_pre_max[j-i])
#         else:
#             value_list.append(new_pre_max[j-i])
#     new_pre_max2.append(max(value_list))


if __name__ == "__main__":
    # Method 1: use search for all combinations to find the optimised knapsack.
    # search(0, 5)
    # print(max_selected, max_value)

    # Method 2
    # print(search_2(0, 5))
    # print(mem)

    # Method 3: search dynamic programming
    search_dp(5)
    print(pre_max)