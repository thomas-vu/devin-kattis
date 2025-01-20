class Quest:
    def __init__(self, energy, gold):
        self.energy = energy
        self.gold = gold

    def __lt__(self, other):
        if self.energy == other.energy:
            return self.gold > other.gold
        return self.energy < other.energy

import heapq

N = int(input())
quest_pool = []

for _ in range(N):
    command = input().split()
    
    if command[0] == 'add':
        E = int(command[1])
        G = int(command[2])
        heapq.heappush(quest_pool, Quest(-E, G))  # Use negative energy to simulate max-heap
    elif command[0] == 'query':
        X = int(command[1])
        available_energy = X
        total_gold = 0
        
        while quest_pool and available_energy > 0:
            top_quest = heapq.heappop(quest_pool)
            if -top_quest.energy <= available_energy:
                total_gold += top_quest.gold
                available_energy -= -top_quest.energy
        
        print(total_gold)