def can_take(a, b):
    if a['sex'] == b['sex']:
        return False
    if abs(a['height'] - b['height']) > 40:
        return False
    if a['music'] == b['music']:
        return False
    if a['sport'] == b['sport']:
        return False
    return True

def max_students(students):
    n = len(students)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if can_take(students[j], students[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) if n > 0 else 0

def main():
    while True:
        try:
            N = int(input())
            students = []
            for _ in range(N):
                data = input().split()
                height, sex, music, sport = int(data[0]), data[1], data[2], data[3]
                students.append({
                    'height': height,
                    'sex': sex,
                    'music': music,
                    'sport': sport
                })
            print(max_students(students))
        except EOFError:
            break

if __name__ == "__main__":
    main()