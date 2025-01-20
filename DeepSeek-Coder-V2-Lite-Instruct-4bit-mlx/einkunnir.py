def calculate_grade(key, answers):
    score = 0
    for k, a in zip(key, answers):
        if k == a:
            score += 1
    return (score * 10) / len(key)

def main():
    S, N = map(int, input().split())
    key = input().split()
    
    students_grades = {}
    
    for _ in range(N):
        name = input()
        answers = input().split()
        
        if len(answers) == S and all(len(a) == 1 for a in answers):
            grade = calculate_grade(key, answers)
            students_grades[name] = grade
    
    for name, grade in sorted(students_grades.items(), key=lambda x: x[0]):
        print(f"{name}: {grade:.1f}")

if __name__ == "__main__":
    main()