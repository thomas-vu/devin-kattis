def main():
    while True:
        n = input()
        if n == '0':
            break
        projects = {}
        while n != '1':
            project_name = n
            students = set()
            while True:
                student_id = input()
                if student_id == '1':
                    break
                students.add(student_id)
            projects[project_name] = len(students)
        sorted_projects = sorted(projects.items(), key=lambda x: (-x[1], x[0]))
        for project, count in sorted_projects:
            print(f"{project} {count}")

if __name__ == "__main__":
    main()