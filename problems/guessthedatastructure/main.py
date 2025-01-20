class DataStructureChecker:
    def __init__(self):
        self.stack = []
        self.queue = []
        self.priority_queue = []

    def push(self, x):
        self.stack.append(x)
        self.queue.append(x)
        self.priority_queue.append(-x)  # Use negative for max-heap simulation

    def pop(self):
        if self.stack:
            return self.stack.pop()
        elif self.queue:
            return self.queue.pop(0)
        else:
            return -self.priority_queue.pop()  # Use negative for max-heap simulation

    def check(self):
        stack_possible = self.stack == sorted(self.stack, reverse=True)
        queue_possible = self.queue == list(reversed(self.queue))
        priority_queue_possible = self.priority_queue == sorted(-x for x in self.priority_queue)

        if stack_possible and queue_possible:
            return 'not sure'
        elif stack_possible:
            return 'stack'
        elif queue_possible:
            return 'queue'
        elif priority_queue_possible:
            return 'priority queue'
        else:
            return 'impossible'

def main():
    while True:
        try:
            n = int(input())
            checker = DataStructureChecker()
            for _ in range(n):
                op = list(map(int, input().split()))
                if op[0] == 1:
                    checker.push(op[1])
                else:
                    if checker.pop() != op[1]:
                        print('impossible')
                        break
            else:
                print(checker.check())
        except EOFError:
            break

if __name__ == "__main__":
    main()