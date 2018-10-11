def main():
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = [float(i) for i in line]
        student_marks[name] = scores

    query_name = input()
    print(f"{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}")

if __name__ == '__main__':
    main()