 
if __name__ == '__main__':
    grades = []
    students =[]
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        students+=[[name,score]]
        grades+=[score]
        grades =list(set(grades))
        grades = sorted(grades)
    b=grades[1]
    for a,c in sorted(students):
        if c==b:
            print(a)