def min_time_to_watch(videos):
    from collections import defaultdict
    
    categories = set()
    video_data = []
    
    # Read input and extract data
    for _ in range(int(input())):
        d_i, categories_str = input().split()
        video_data.append((int(d_i), set(categories_str)))
        categories.update(categories_str)
    
    # Create a bitmask for each video's categories
    category_bitmask = {cat: 1 << i for i, cat in enumerate(categories)}
    
    # Initialize the minimum time to a large number
    min_time = float('inf')
    
    # Check all subsets of videos to find the minimum time needed
    for mask in range(1, 1 << len(videos)):
        current_categories = set()
        total_time = 0
        
        for i in range(len(videos)):
            if mask & (1 << i):
                total_time += video_data[i][0]
                current_categories.update(video_data[i][1])
        
        if len(current_categories) == len(categories):
            min_time = min(min_time, total_time)
    
    return min_time

# Read the number of videos and call the function to get the result
print(min_time_to_watch([]))