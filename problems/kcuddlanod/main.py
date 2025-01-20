def mirror_reversal(num):
    return int(str(num).replace('2', 'x').replace('5', '2').replace('x', '5'))

def compare_bags(N, M):
    reversed_N = mirror_reversal(N)
    reversed_M = mirror_reversal(M)
    
    if reversed_N > reversed_M:
        return 1
    else:
        return 2

# Read input
N, M = map(int, input().split())
print(compare_bags(N, M))