def can_paint(colors, preferences):
    n = len(colors)
    for i in range(n - 1):
        if colors[i] == preferences and colors[i + 1] == preferences:
            return False
    return True

def count_paintings(N, color_preferences, preferences):
    if N == 1:
        return [[colors[0]], 1]
    
    def backtrack(index, current_painting):
        if index == N:
            return [current_painting, 1]
        
        for color in colors:
            if can_paint(current_painting + [color], preferences[index]):
                result = backtrack(index + 1, current_painting + [color])
                if result[1] == 1:
                    return [[color] + result[0], 1]
        return [None, 0]
    
    colors = color_preferences[0]
    preferences = color_preferences[1:]
    result = backtrack(0, [])
    
    return [result[1], result[0]]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        color_preferences = [input().split()]
        M = int(input())
        preferences = []
        for _ in range(M):
            c1, c2 = input().split()
            preferences.append((c1, c2))
        
        result = count_paintings(N, color_preferences, preferences)
        print(result[0])
        if result[1]:
            print(" ".join(result[1]))

if __name__ == "__main__":
    main()