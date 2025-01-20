import sys
from heapq import heappush, heappop

class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.waiting_time = 0
    
    def priority(self):
        return self.severity + K * self.waiting_time
    
    def __lt__(self, other):
        if self.priority() == other.priority():
            return self.name < other.name
        return self.priority() > other.priority()

# Read input
N, K = map(int, sys.stdin.readline().split())
queries = [list(map(int, sys.stdin.readline().strip().split())) + [sys.stdin.readline().strip()] for _ in range(N)]

# Process queries
heap = []
patient_dict = {}
for query in queries:
    Q = query[0]
    if Q == 1:
        T, M, S = query[1], query[2], query[3]
        patient = Patient(M, S, T)
        heappush(heap, patient)
        patient_dict[M] = patient
    elif Q == 2:
        T = query[1]
        while heap and heap[0].arrival_time <= T:
            patient = heappop(heap)
            patient.waiting_time += 1
            print(patient.name)
        if not heap:
            print("doctor takes a break")
    elif Q == 3:
        T, M = query[1], query[2]
        if M in patient_dict:
            del patient_dict[M]