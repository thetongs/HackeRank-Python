if __name__ == '__main__':
    n = int(input())
    if(n >= 2 and n <= 100):
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()

            if(len(line) == 3):
                scores = list(map(float, line))
                for elm in scores:
                    if(elm >= 0 and elm <= 100):
                        student_marks[name] = scores
                    else:
                        break
        
        query_name = input()
        
        avg = 0
        for key, value in student_marks.items():
            if(key == query_name):
                avg = sum(value) / len(value)
                
        
        print("{0:.2f}".format(avg))
