def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    i = 0
    while True:
        n = int(data[i])
        if n == 0:
            break
        
        animals = {}
        for j in range(i + 1, i + n + 1):
            animal = data[j].split()[-1].lower()
            if animal in animals:
                animals[animal] += 1
            else:
                animals[animal] = 1
        
        ordered_animals = sorted(animals.items())
        print("List {}:".format(i // (n + 1) + 1))
        for animal, count in ordered_animals:
            print(animal, "|", count, end=" ")
        print()
        
        i += n + 1