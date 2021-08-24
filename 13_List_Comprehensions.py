if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Without List Comprehension
    # dataset = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             dataset.append([i, j, k])
    
    # final = []
    # for box in dataset:
    #     if((box[0] + box[1] + box[2]) != n):
    #         final.append(box)
    
    # print(final)

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])





