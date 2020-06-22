import time
import random
def random_list(start, end, length):
    data_list = []
    for i in range(length):
        data_list.append(random.randint(start,end))
    return data_list

data = random_list(1,10000000,100000000)
data = sorted(data)

# solution using non-recursion
def search(data_list, target):
    left = 0
    right = len(data_list) - 1
    mid = int((left + right) / 2)
    pos = -1
    while left <= right:
        if data_list[mid] == target:
            pos = mid
            break
        elif data_list[mid] > target:
            # search on the left list
            right = mid
            mid=int((left+right)/2)
        else:
            # search on the right list
            left = mid
            mid=int((left+right)/2)
    return pos

# solution using recursion
def search_2(left, right, data_list,target):
    mid = int((left+right)/2)
    pos = -1
    if data_list[mid] == target:
        pos = mid
        return pos
    elif data_list[mid] < target:
        # search in right list
        return search_2(mid+1, right, data_list, target)
    else:
        return search_2(left, mid-1, data_list, target)


if __name__ == '__main__':
    target = random.randint(0,len(data)-1)
    print(data)
    print(data[target])


    start = time.time()
    pos = search(data, data[target])
    end = time.time()
    start2 = time.time()
    pos2 = search_2(0, len(data) - 1, data, data[target])
    end2 = time.time()

    if pos < 0:
        print("Cannot find data. ")
    else:
        print("Data is found at position", pos)
    if pos2 < 0:
        print("Cannot find data. ")
    else:
        print("Data is found at position", pos2)
    n = 100000000000000000
    print("Time take for non-recursion method: ", (end-start)*n)
    print("Time take for recursion method:     ", (end2-start2)*n)