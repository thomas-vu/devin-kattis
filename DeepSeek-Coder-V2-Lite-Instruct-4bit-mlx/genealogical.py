class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.death_date = None
        self.parents = []
        self.children = []

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child.parents.append(self)

    def is_alive(self):
        return self.death_date is None

class FamilyTree:
    def __init__(self):
        self.people = {}

    def add_person(self, name, birth_date, mother_name, father_name):
        if name not in self.people:
            mother = self.get_person(mother_name)
            father = self.get_person(father_name)
            person = Person(name, birth_date)
            self.people[name] = person
            if mother:
                mother.add_child(person)
            if father:
                father.add_child(person)

    def get_person(self, name):
        return self.people.get(name)

    def list_ancestors(self, person):
        ancestors_list = []
        for parent in person.parents:
            if parent.is_alive():
                ancestors_list.append((parent.name, parent.birth_date))
            ancestors_list.extend(self.list_ancestors(parent))
        return ancestors_list

    def list_descendants(self, person):
        descendants_list = []
        for child in person.children:
            if child.is_alive():
                descendants_list.append((child.name, child.birth_date))
            descendants_list.extend(self.list_descendants(child))
        return descendants_list

    def process_command(self, command):
        parts = command.split()
        if parts[0] == 'BIRTH':
            _, name, birth_date, mother_name, father_name = parts
            self.add_person(name, birth_date, mother_name, father_name)
        elif parts[0] == 'DEATH':
            _, name, death_date = parts
            person = self.get_person(name)
            if person:
                person.death_date = death_date
        elif parts[0] == 'ANCESTORS':
            person_name = parts[1]
            person = self.get_person(person_name)
            if person:
                ancestors = self.list_ancestors(person)
                self._print_ancestors_descendants('ANCESTORS', person_name, ancestors)
        elif parts[0] == 'DESCENDANTS':
            person_name = parts[1]
            person = self.get_person(person_name)
            if person:
                descendants = self.list_descendants(person)
                self._print_ancestors_descendants('DESCENDANTS', person_name, descendants)

    def _print_ancestors_descendants(self, type, person_name, entries):
        print(f"{type} of {person_name}")
        for entry in entries:
            name, date = entry
            if not self.get_person(name):
                print(f"  {name}")
            else:
                status = f"{date} -" if self.get_person(name).is_alive() else date
                print(f"  {name} {status}")
        print()

# Main loop to read commands and process the family tree
tree = FamilyTree()
while True:
    command = input().strip()
    if command == 'QUIT':
        break
    tree.process_command(command)