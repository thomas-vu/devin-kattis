T = int(input())
for _ in range(T):
    recording = input().split()
    
    animals_sounds = {}
    while True:
        line = input().strip()
        if line == "what does the fox say?":
            break
        animal, _, sound = line.split()
        animals_sounds[animal] = sound
    
    fox_says = []
    for word in recording:
        if word not in animals_sounds.values():
            fox_says.append(word)
    
    print(' '.join(fox_says))