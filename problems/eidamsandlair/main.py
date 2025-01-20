def min_time(Yp, Lp, Ys, Ls):
    # Calculate the time to walk directly to 0 from your floor
    walk_to_zero = Yp * Ls
    
    # Calculate the time to wait for the lift and then travel with it
    floors_to_lift = abs(Lp - Yp)
    lift_wait_time = floors_to_lift * Ls
    
    # Calculate the time to call the lift and walk up to 0 after waiting for it
    floors_to_call_lift = abs(Lp - Yp)
    call_lift_time = floors_to_call_lift * Ls + 10
    lift_travel_time = (Lp - Yp) * Ls
    
    # Choose the minimum time between walking directly and using the lift
    return min(walk_to_zero, call_lift_time + lift_travel_time)

# Read number of test cases
T = int(input())
for _ in range(T):
    Yp, Lp, Ys, Ls = map(int, input().split())
    print(min_time(Yp, Lp, Ys, Ls))