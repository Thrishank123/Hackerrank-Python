if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks[query_name]
    sum=0
    for i in range(0,len(marks)):
        sum+=marks[i]
    output=sum/len(marks)
    output="{:.2f}".format(output)
    print(output)
