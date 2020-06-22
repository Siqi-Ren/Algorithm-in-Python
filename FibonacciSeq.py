"""This programme is to implement Fibonacci Sequence, to find kth number in a sequence"""
"""Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13... """

# solution using recursion, disadvantage is that its calculating repeatedly. Memory consumption is high.
def fib(k):
    assert k>0, "k is greater than 0"
    # if k == 1 or k==2 :
    if k in [1, 2]:
        return 1
    return fib(k-1)+fib(k-2)

# solution using non-recursion
def fib_2(k):
    if k in [1, 2]:
        return 1
    k_1 = 1
    k_2 = 1
    for i in range(3, k+1):
        i_value = k_1 + k_2
        k_2 = k_1
        k_1 = i_value

    return k_1

if __name__ == "__main__":
    print(fib(7))
    print(fib_2(7))
