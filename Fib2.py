""" This programme use search in memory method to solve fibonacci number """
from collections import defaultdict
total = defaultdict(int)
def fib(k):
    assert k > 0, "k is greater than 0"
    if k in [1, 2]:
        return 1
    global total
    if k in total:
        result = total[k]
    else:
        result = fib(k-1)+fib(k-2)
        total[k] = result
    return result

if __name__ == "__main__":
    print(fib(50))
    print(total)
