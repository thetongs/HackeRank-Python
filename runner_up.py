if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    if(n >= 2 and n <= 10):
        for val in arr:
            if(val in range(-100, 101)):
                flag = True
            else:
                flag = False
                break

    if(flag):
        arr = set(arr)
        arr = list(arr)
        arr.sort()
        print(arr[-2])
