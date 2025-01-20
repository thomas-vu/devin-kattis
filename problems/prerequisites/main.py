def can_graduate(k, m, courses, categories):
    category_taken = {i: 0 for i in range(1, m + 1)}
    
    for course in courses:
        for category in categories:
            if course in category[2:]:
                category_taken[category[0]] += 1
    
    for cat in category_taken:
        if category_taken[cat] < categories[cat - 1][1]:
            return "no"
    return "yes"

def main():
    while True:
        k, m = map(int, input().split())
        if k == 0 and m == 0:
            break
        
        courses = list(map(int, input().split()))
        categories = []
        
        for _ in range(m):
            cat_info = list(map(int, input().split()))
            categories.append(cat_info)
        
        result = can_graduate(k, m, courses, categories)
        print(result)

if __name__ == "__main__":
    main()