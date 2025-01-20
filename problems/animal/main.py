def count_common_groups(tree1, tree2):
    def parse_tree(tree_str):
        stack = []
        nums = set()
        for char in tree_str:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    sub_tree = stack.pop()
                    if sub_tree not in nums:
                        nums.add(sub_tree)
                stack.pop()  # Remove '(' from the stack
            elif char == ',':
                continue
            else:  # It's a number
                while stack and stack[-1] != '(':
                    sub_tree = stack.pop()
                    if sub_tree not in nums:
                        nums.add(sub_tree)
                stack.append(char)  # Push the number onto the stack
        while stack:
            sub_tree = stack.pop()
            if sub_tree not in nums:
                nums.add(sub_tree)
        return nums
    
    groups1 = parse_tree(tree1)
    groups2 = parse_tree(tree2)
    common_groups = groups1.intersection(groups2)
    return len(common_groups)

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
tree1 = data[1]
tree2 = data[2]

# Output the result
print(count_common_groups(tree1, tree2))