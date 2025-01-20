n = int(input())
correct_answers = [input().strip() for _ in range(n)]
hanh_answers = [''] * n
for i in range(1, n + 1):
    hanh_answers[i - 1] = correct_answers[i - 2]
score = sum(hanh_answers[i] == correct_answers[i] for i in range(n))
print(score)