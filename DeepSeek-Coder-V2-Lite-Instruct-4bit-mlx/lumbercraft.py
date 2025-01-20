def parse_input():
    while True:
        h, w, n = map(int, input().split())
        if h == 0 and w == 0 and n == 0:
            break
        board = [input().strip() for _ in range(h)]
        turns = n
        yield board, turns

def find_closest_tree(board, mill):
    min_dist = float('inf')
    closest_tree = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '!':
                dist = abs(i - mill[0]) + abs(j - mill[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_tree = (i, j)
                elif dist == min_dist and j > closest_tree[1]:
                    closest_tree = (i, j)
    return closest_tree

def update_board(board, mills):
    for mill in mills:
        trees = []
        while True:
            tree = find_closest_tree(board, mill)
            if tree is None:
                break
            trees.append(tree)
            board[tree[0]][tree[1]] = '.'
        if trees:
            num_trees = len(trees)
            for tree in trees:
                board[tree[0]][tree[1]] = '!'
            lumber_per_tree = 1.0 / num_trees
            for tree in trees:
                mills[chr(ord('A') + mill[2] - 1)] += lumber_per_tree
    return board

def main():
    mills = {chr(ord('A') + i): 0 for i in range(26)}
    for board, turns in parse_input():
        for _ in range(turns):
            board = update_board(board, mills)
        for mill in sorted(mills.keys()):
            print(f"{mill} {mills[mill]:.6f}")
        mills = {chr(ord('A') + i): 0 for i in range(26)}

if __name__ == "__main__":
    main()