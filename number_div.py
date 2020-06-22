"""This programme find all the summation combinations of a given number"""
num = 7
result = 0
datas = []

def sums(n):
    if n <= 0:
        global result
        result = result+1
        print(result)
        print(datas)
    else:
        for i in range(1,n+1):
            # step 1： setting the scene
            # n = n-i
            datas.append(i)
            # step 2：recurring function
            sums(n-i)
            # step 3: restore the scene
            # n = n+i
            datas.pop()

if __name__ == "__main__":
    sums(7)
