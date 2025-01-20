def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    m, q = int(data[0]), int(data[1])
    employees = {}
    
    for i in range(2, m + 2):
        id_num = data[i*3-2]
        salary = int(data[i*3-1])
        height = int(data[i*3])
        employees[id_num] = {'salary': salary, 'height': height}
    
    queries = [data[m*3 + i] for i in range(1, q + 1)]
    
    def find_boss(id_num):
        for e in employees.values():
            if id_num == e['height']:
                return 0
            elif id_num > e['height'] and id_num < e['salary']:
                return e['id']
    
    def count_subordinates(id_num):
        subord_count = 0
        for e in employees.values():
            if find_boss(e['height']) == id_num:
                subord_count += 1
        return subord_count
    
    for query in queries:
        if find_boss(query) == 0:
            print("0")
        else:
            boss_id = find_boss(query)
            subord_count = count_subordinates(query)
            print(f"{boss_id} {subord_count}")

if __name__ == "__main__":
    main()