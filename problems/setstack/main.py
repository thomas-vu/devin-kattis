class SetStackAlpha:
    def __init__(self):
        self.stack = []
    
    def push_empty_set(self):
        self.stack.append({})
    
    def duplicate_topmost_set(self):
        if self.stack:
            top = self.stack[-1]
            self.stack.append(top)
    
    def union_topmost_sets(self):
        if len(self.stack) >= 2:
            set2 = self.stack.pop()
            set1 = self.stack.pop()
            merged_set = set1 | set2
            self.stack.append(merged_set)
    
    def intersect_topmost_sets(self):
        if len(self.stack) >= 2:
            set2 = self.stack.pop()
            set1 = self.stack.pop()
            intersect_set = set1 & set2
            self.stack.append(intersect_set)
    
    def add_topmost_sets(self):
        if len(self.stack) >= 2:
            set2 = self.stack.pop()
            set1 = self.stack.pop()
            added_set = set1 | set2
            self.stack.append(added_set)
    
    def get_topmost_cardinality(self):
        if self.stack:
            top = self.stack[-1]
            return len(top)
        return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        set_stack = SetStackAlpha()
        for _ in range(N):
            command = data[index]
            index += 1
            if command == 'PUSH':
                set_stack.push_empty_set()
            elif command == 'DUP':
                set_stack.duplicate_topmost_set()
            elif command == 'UNION':
                set_stack.union_topmost_sets()
            elif command == 'INTERSECT':
                set_stack.intersect_topmost_sets()
            elif command == 'ADD':
                set_stack.add_topmost_sets()
            results.append(set_stack.get_topmost_cardinality())
        results.append('***')
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()