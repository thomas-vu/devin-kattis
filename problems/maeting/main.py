def attendance_on_both_days():
    n, m = map(int, input().split())
    attendance_monday = set(map(int, input().split()))
    attendance_tuesday = set(map(int, input().split()))
    
    common_attendance = attendance_monday.intersection(attendance_tuesday)
    
    result = [str(student) for student in sorted(common_attendance)]
    
    print(' '.join(result))

# Call the function to execute the solution
attendance_on_both_days()