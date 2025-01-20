import sys

def parse_class(cls):
    parts = cls.split('-')
    return len(parts), tuple(parts)

def compare_classes(cls1, cls2):
    l1, t1 = parse_class(cls1)
    l2, t2 = parse_class(cls2)
    
    min_length = min(l1, l2)
    for i in range(min_length):
        if t1[i] != t2[i]:
            return -1 if t1[i] < t2[i] else 1
    return len(t1) - len(t2)

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        people = []
        for _ in range(n):
            name, cls = input().split(': ')
            people.append((name, cls))
        
        # Sort by class hierarchy and then by name if classes are the same
        people.sort(key=lambda x: (-parse_class(x[1])[0], x[0]))
        
        # Output the sorted list of names
        for name, _ in people:
            print(name)
        
        # Output the separator line after each case
        if _ < T - 1:
            print('=' * 30)

if __name__ == "__main__":
    main()