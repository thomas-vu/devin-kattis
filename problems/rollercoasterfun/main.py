def calculate_max_fun(N, roller_coasters, Q, times):
    for i in range(N):
        a_i, b_i, t_i = roller_coasters[i]
        fun_values = []
        for k in range(1, t_i + 1):
            fun = a_i - (k - 1) ** 2 * b_i
            if fun > 0:
                fun_values.append(fun)
        roller_coasters[i] = (a_i, b_i, t_i, sum(fun_values))
    
    results = []
    for time in times:
        max_fun = 0
        for a_i, b_i, t_i, total_fun in roller_coasters:
            if time >= t_i:
                max_fun = max(max_fun, total_fun)
            else:
                fun_values = []
                for k in range(1, time + 1):
                    fun = a_i - (k - 1) ** 2 * b_i
                    if fun > 0:
                        fun_values.append(fun)
                max_fun = max(max_fun, sum(fun_values))
        results.append(max_fun)
    return results

# Read input
N = int(input())
roller_coasters = []
for _ in range(N):
    a_i, b_i, t_i = map(int, input().split())
    roller_coasters.append((a_i, b_i, t_i))
Q = int(input())
times = []
for _ in range(Q):
    times.append(int(input()))

# Calculate and print results
results = calculate_max_fun(N, roller_coasters, Q, times)
for result in results:
    print(result)