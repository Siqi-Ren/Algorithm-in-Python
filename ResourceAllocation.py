""" This program solves problem of investment resource allocation for maximum profit.
Allocate $600，000 to n factories.
"""
invest_return = [[0, 20, 50, 65, 80, 85, 85],
                 [0, 20, 40, 50, 55, 60, 65],
                 [0, 25, 60, 85, 100, 110, 115],
                 [0, 25, 40, 50, 60, 65, 70]]


def search():
    """ This function takes total resource for allocation,
    return the best possible allocation strategy"""
    pre_max = invest_return[3]
    for k in range(len(invest_return)-1, -1, -1):
        new_pre_max = [0]
        for i in range(1, len(invest_return[0]), 1):
            max_temp = []
            for j in range(0, i + 1, 1):
                max_temp.append(invest_return[k-1][i - j] + pre_max[j])
            new_pre_max.append(max(max_temp))
        pre_max = new_pre_max
    return pre_max


if __name__ == "__main__":
    print(max(search()))