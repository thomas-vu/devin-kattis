import sys
from collections import defaultdict

class Runner:
    def __init__(self, first_name, last_name, bib):
        self.first_name = first_name
        self.last_name = last_name
        self.bib = bib
        self.split1 = None
        self.split2 = None
        self.finish = None
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.bib}"
    
    def calculate_times(self, timing):
        if timing['location'] == 'S1':
            self.split1 = timing['time']
        elif timing['location'] == 'S2':
            self.split2 = timing['time']
        elif timing['location'] == 'F':
            self.finish = timing['time']
    
    def overall_time(self):
        if self.split1 is None or self.finish is None:
            return float('inf')
        split1_minutes, split1_seconds = map(int, self.split1.split(':'))
        finish_minutes, finish_seconds = map(int, self.finish.split(':'))
        split1_time = split1_minutes * 60 + split1_seconds
        finish_time = finish_minutes * 60 + finish_seconds
        return split1_time + (finish_time - split1_time)
    
    def __lt__(self, other):
        return self.overall_time() < other.overall_time()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.bib}"

def process_race(data):
    runners = defaultdict(Runner)
    n = int(data[0])
    for i in range(1, n + 1):
        first_name, last_name, bib = data[i].split()
        runners[bib] = Runner(first_name, last_name, bib)
    
    for i in range(n + 1, len(data)):
        bib, location, time = data[i].split()
        timing = {'bib': bib, 'location': location, 'time': time}
        runners[bib].calculate_times(timing)
    
    sorted_runners = sorted([r for r in runners.values() if r.split1 is not None and r.finish is not None])
    for i, runner in enumerate(sorted_runners):
        if runner.split2 is not None:
            sorted_runners[i].rank = i + 1
        else:
            break
    
    sorted_runners = sorted([r for r in runners.values() if r.split2 is not None])
    for i, runner in enumerate(sorted_runners):
        sorted_runners[i].rank = i + 1
    
    return runners

def print_race_results(runners):
    headers = ["NAME", "BIB", "SPLIT1", "RANK", "SPLIT2", "RANK", "FINISH", "RANK"]
    print(f"| {' | '.join(headers)} |")
    for runner in sorted(runners.values(), key=lambda r: (r.last_name, r.first_name)):
        split1_rank = runner.split1_rank if hasattr(runner, 'split1_rank') else ""
        split2_rank = runner.split2_rank if hasattr(runner, 'split2_rank') else ""
        print(f"| {runner.first_name} {runner.last_name: <14} | {runner.bib} | {runner.split1: >6} | {split1_rank} | {runner.split2: >6} | {split2_rank} | {runner.finish: >6} | {runner.overall_rank} |")
    print()

data = []
for line in sys.stdin:
    data.append(line.strip())
    if line.strip() == "0":
        break

race_index = 0
while race_index < len(data):
    if data[race_index] == "0":
        break
    n = int(data[race_index])
    race_data = data[race_index+1:race_index+n+1]
    timings = data[race_index+n+1:]
    all_data = race_data + timings
    runners = process_race(all_data)
    print_race_results(runners)
    race_index += len(all_data) + 1