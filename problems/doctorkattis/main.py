class Cat:
    def __init__(self, name, infection_level):
        self.name = name
        self.infection_level = infection_level

class Clinic:
    def __init__(self):
        self.cats = []
    
    def arrive_at_clinic(self, cat_name, infection_level):
        self.cats.append(Cat(cat_name, infection_level))
    
    def update_infection_level(self, cat_name, increase_infection):
        for cat in self.cats:
            if cat.name == cat_name:
                cat.infection_level += increase_infection
                break
    
    def treated(self, cat_name):
        self.cats = [cat for cat in self.cats if cat.name != cat_name]
    
    def query(self):
        if not self.cats:
            return "The clinic is empty"
        highest_infection = max(self.cats, key=lambda cat: (-cat.infection_level, self.cats.index(cat)))
        return highest_infection.name

clinic = Clinic()
n = int(input())
for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 0:
        clinic.arrive_at_clinic(command[1], command[2])
    elif command[0] == 1:
        clinic.update_infection_level(command[1], command[2])
    elif command[0] == 2:
        clinic.treated(command[1])
    elif command[0] == 3:
        print(clinic.query())