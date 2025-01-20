def main():
    m = int(input())
    f_values = list(map(int, input().split()))
    
    # Sort the f_values to find the median of the subtree sizes
    f_values.sort()
    
    # The size of the tree
    n = 2 * m - 1
    
    # The median of the subtree sizes should be equal to the size of the root's subtrees
    if f_values[m - 1] == m:
        print("yes")
    else:
        print("no")

main()