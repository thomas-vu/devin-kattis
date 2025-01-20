def merge_lists(ann_list, ben_list):
    merged = []
    i, j = 0, 0
    
    while i < len(ann_list) and j < len(ben_list):
        if ann_list[i] < ben_list[j]:
            merged.append(ann_list[i])
            i += 1
        else:
            merged.append(ben_list[j])
            j += 1
    
    while i < len(ann_list):
        merged.append(ann_list[i])
        i += 1
    
    while j < len(ben_list):
        merged.append(ben_list[j])
        j += 1
    
    return ''.join(merged)

# Read input from stdin
ann_list = input().strip()
ben_list = input().strip()

# Output the merged list
print(merge_lists(ann_list, ben_list))