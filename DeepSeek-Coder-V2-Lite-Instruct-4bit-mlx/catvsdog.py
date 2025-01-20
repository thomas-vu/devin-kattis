def read_ints():
    return list(map(int, input().split()))

def parse_pet(pet):
    return (pet[0], int(pet[1:]))

def main():
    t = int(input())
    for _ in range(t):
        c, d, v = read_ints()
        cat_votes = [0] * (v + 1)
        dog_votes = [0] * (v + 1)
        
        for _ in range(v):
            keep_pet, remove_pet = input().split()
            keep_type, keep_id = parse_pet(keep_pet)
            remove_type, remove_id = parse_pet(remove_pet)
            
            if keep_type == 'C':
                cat_votes[keep_id] += 1
            else:
                dog_votes[keep_id] += 1
            
            if remove_type == 'C':
                cat_votes[remove_id] += 1
            else:
                dog_votes[remove_id] += 1
        
        max_satisfied = 0
        for i in range(1, v + 1):
            for j in range(i + 1, v + 2):
                satisfied_voters = cat_votes[i] + dog_votes[j] + cat_votes[j] + dog_votes[i]
                max_satisfied = max(max_satisfied, satisfied_voters)
        
        print(max_satisfied)

if __name__ == "__main__":
    main()