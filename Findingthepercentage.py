from decimal import Decimal
n = int(input())

student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
    
query_scores = student_marks[query_name]
mysum = sum(query_scores) 
average_marks = Decimal(mysum/3)
print(round(average_marks,2))