if __name__ == '__main__':
    n = int(input())
    
    if(n >= 1 and n <= 20):
        numbers = [*range(0, n)]
        
        for n in numbers:
            if(n >= 0):
                print(n * n)
                
        
    
