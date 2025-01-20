def min_score(n, rounds):
    scores = [1] * 3
    for i in range(n):
        player, num = rounds[i]
        if player == 'O':
            if num % 2 != 0:
                while num > 1 and (num % 2 == 0 or num % 3 == 0):
                    if num % 2 == 0:
                        num //= 2
                    else:
                        num -= 1
                scores[0] += min(num, scores[0])
            else:
                while num > 1 and (num % 2 == 0 or num % 3 == 0):
                    if num % 3 == 0:
                        num //= 3
                    else:
                        num -= 1
                scores[0] += min(num, scores[0])
        elif player == 'E':
            if num % 2 == 0:
                while num > 1 and (num % 2 == 0 or num % 3 == 0):
                    if num % 2 == 0:
                        num //= 2
                    else:
                        num -= 1
                scores[1] += min(num, scores[1])
            else:
                while num > 1 and (num % 2 == 0 or num % 3 == 0):
                    if num % 3 == 0:
                        num //= 3
                    else:
                        num -= 1
                scores[1] += min(num, scores[1])
        elif player == 'I':
            while num > 1 and (num % 2 == 0 or num % 3 == 0):
                if num % 3 == 0:
                    num //= 3
                else:
                    num -= 1
            scores[2] += min(num, scores[2])
    return f"Odd {scores[0]-1} Even {scores[1]-1} Ingmariay {scores[2]-1}"

n = int(input())
rounds = [input().split() for _ in range(n)]
print(min_score(n, rounds))