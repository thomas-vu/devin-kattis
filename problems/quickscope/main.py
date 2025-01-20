N = int(input())
lines = [input().strip() for _ in range(N)]

class Block:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

    def declare(self, name, type_):
        if name in self.variables:
            print("MULTIPLE DECLARATION")
            exit()
        self.variables[name] = type_

    def query(self, name):
        if name in self.variables:
            print(self.variables[name])
        elif self.parent is not None:
            self.parent.query(name)
        else:
            print("UNDECLARED")

block_stack = [Block()]
for line in lines:
    parts = line.split()
    if parts[0] == "{":
        block_stack.append(Block(block_stack[-1]))
    elif parts[0] == "}":
        block_stack.pop()
    elif parts[0] == "DECLARE":
        _, name, type_ = parts
        block_stack[-1].declare(name, type_)
    elif parts[0] == "TYPEOF":
        _, name = parts
        block_stack[-1].query(name)