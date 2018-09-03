if __name__ == '__main__':
    n = int(input())
    res = 0
    student_marks = {}
    student_data = ["Math: ", "Physics: ", "Chemistry: "]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #print("Enter the student name: ")
    query_name = input()
    if query_name in student_marks.keys():
        res = float((student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2]))/3
    print("%.2f" % res)
    """
    res = 0
    if(query_name==student_marks[name]):
        res = (scores[0]+scores[1]+scores[2])/3
    
    """
    
    #print("%.2f" % x)