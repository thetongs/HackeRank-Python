if __name__ == '__main__':
    n = int(input())
    if(n >= 1 and n <= 150):
        numbers = [*range(1, n+1)]
    
        final = ''.join(str(n) for n in numbers)
        print(final)
