def main():
    n = int(input())
    requests = {}
    
    for _ in range(n):
        name, course = input().split()[:2]
        if course not in requests:
            requests[course] = set([name])
        else:
            requests[course].add(name)
    
    sorted_courses = sorted(requests.keys())
    for course in sorted_courses:
        print(f"{course} {len(requests[course])}")

if __name__ == "__main__":
    main()