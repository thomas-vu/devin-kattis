def main():
    n = int(input())
    students = []
    for _ in range(n):
        callout = input()
        if callout.startswith("Present!"):
            continue
        students.append(callout)
    
    if not students:
        print("No Absences")
    else:
        for student in sorted(students):
            print(student)

if __name__ == "__main__":
    main()