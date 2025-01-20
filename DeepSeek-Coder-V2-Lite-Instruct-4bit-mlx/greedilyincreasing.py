import sys

def read_ints():
    return list(map(int, input().split()))

N = int(input())
A = read_ints()

# Initialize the GIS list with the first element of A
GIS = [A[0]]

# Iterate through the permutation to find the GIS
for i in range(1, N):
    for j in range(len(GIS)):
        if GIS[j] > A[i]:
            GIS[j] = A[i]
            break
    else:
        GIS.append(A[i])

# Output the length of the GIS and the elements of the GIS
print(len(GIS))
print(' '.join(map(str, GIS)))