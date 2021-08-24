if __name__ == '__main__':
    data = []
    n = int(input())
    if(n >= 2 and n <= 5):
        for _ in range(n):
            name = input()
            score = float(input())
        
            data.append([name, score])
    
    data.sort(key=lambda x:x[1])
          
    values = []
    for lis in data:
        values.append(lis[1])

    values = set(values)
    values = list(values)
    val = values[1]
    
    for el in sorted(data[::-1]):
        if(val in el):
            print(el[0])
