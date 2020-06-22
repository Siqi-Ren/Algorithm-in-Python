"""This programe returns a combination of all sequence in a given array"""
data_list = [1, 2, 3, 4, 5]
total = 0
data = []


def search(data_list):
    if len(data_list) == 0:
        print(data)
        global total
        total = total + 1
    else:
        for i in data_list:
            # 1. add in i, set new setting
            data.append(i)
            # 2. set recurrence
            new_data = data_list[:]
            new_data.remove(i)
            search(new_data)
            # 3. remove to current setting
            data.pop()
        # return print(data)


if __name__ == "__main__":
    search(data_list)
    print("Total ", total, " combinations")
