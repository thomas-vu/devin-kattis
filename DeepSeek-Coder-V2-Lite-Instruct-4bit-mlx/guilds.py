def find_top_level_guild(member_to_boss):
    boss_of = {}
    for member, boss in member_to_boss:
        while member in boss_of:
            member = boss_of[member]
        boss_of[member] = boss
    return boss_of

def main():
    n = int(input())
    member_to_boss = [input().split() for _ in range(n)]
    
    top_level_guild = find_top_level_guild(member_to_boss)
    
    for member, boss in member_to_boss:
        while top_level_guild[member] != top_level_guild[boss]:
            boss = top_level_guild[boss]
        print(member, top_level_guild[member])

if __name__ == "__main__":
    main()