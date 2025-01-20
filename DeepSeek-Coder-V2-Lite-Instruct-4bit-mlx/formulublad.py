def main():
    n, L = map(int, input().split())
    formulas = []
    for i in range(n):
        li, mi = map(int, input().split())
        formulas.append((li, mi, i + 1))
    
    # Sort formulas by importance in descending order, then by number of lines
    formulas.sort(key=lambda x: (-x[1], x[0]))
    
    max_importance = 0
    chosen_formulas = []
    
    for i in range(n):
        current_lines = 0
        current_importance = 0
        for j in range(i, n):
            if current_lines + formulas[j][0] <= L:
                current_lines += formulas[j][0]
                current_importance += formulas[j][1]
                chosen_formulas.append(formulas[j][2])
            else:
                break
        if current_importance > max_importance:
            max_importance = current_importance
    
    chosen_formulas.sort()
    print(len(chosen_formulas), max_importance)
    print(' '.join(map(str, chosen_formulas)))

if __name__ == "__main__":
    main()