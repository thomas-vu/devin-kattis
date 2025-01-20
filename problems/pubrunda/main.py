N = int(input())
max_time = 0
pub_with_longest_queue = ""
total_waiting_time = 0

for i in range(N):
    pub_name, queue_length, time_per_person = input().split()
    total_waiting_time = int(queue_length) * int(time_per_person)
    if total_waiting_time > max_time:
        max_time = total_waiting_time
        pub_with_longest_queue = pub_name

print(pub_with_longest_queue, max_time)