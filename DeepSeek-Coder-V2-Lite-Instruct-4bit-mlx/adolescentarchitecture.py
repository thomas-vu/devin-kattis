def can_stack(blocks):
    cubes = []
    cylinders = []
    
    for block in blocks:
        typ, size = block.split()
        if typ == 'cube':
            cubes.append(int(size))
        else:  # typ == 'cylinder'
            cylinders.append(int(size))
    
    cubes.sort()
    cylinders.sort()
    
    result = []
    while cubes and cylinders:
        if cubes[-1] >= cylinders[-1]:
            result.append('cube')
            cubes.pop()
        else:
            result.append('cylinder')
            cylinders.pop()
    
    while cubes:
        result.append('cube')
        cubes.pop()
    
    while cylinders:
        result.append('cylinder')
        cylinders.pop()
    
    return result[::-1]

n = int(input())
blocks = [input().strip() for _ in range(n)]
result = can_stack(blocks)
if result:
    for block in result:
        print(block)
else:
    print('impossible')