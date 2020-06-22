# All recursion problems could be solved with non-recursive ways
# advantage:
# ''' Simple way to solve a problem
# disadvantage:
# ''' Slower than iterative solution
# ''' May cause stack overflow if goes into too deep
# ''' Difficult to debug and trace into each recursion step

"""This programme solve the problem of Hanoi of n levels"""
def move(index, start, mid, end):
    if index == 1:
        print("{}->{}".format(start,end))
        # return
    else:
        move(index-1,start,end,mid)
        print("{}->{}".format(start,end))
        move(index-1,mid,start,end)


if __name__ =="__main__":
    move(5,"A","B","C")
