def main():
    N = int(input())
    answers = input()
    
    def count_correct_answers(sequence, answers):
        correct = 0
        for i in range(len(answers)):
            if answers[i] == sequence[i % len(sequence)]:
                correct += 1
        return correct
    
    sequences = [
        "A" * (N // 3 + 1),
        "B" * (N // 4 + 1) if N % 4 == 0 else "B" * (N // 4 + 1) + "A",
        "C" * (N // 6 + 1) if N % 6 == 0 else "C" * (N // 6 + 1) + "A" * (N % 6 // 2) + "B" * (N % 6 // 2)
    ]
    
    max_correct = 0
    winners = []
    
    for i, sequence in enumerate(sequences):
        correct_count = count_correct_answers(sequence, answers)
        if correct_count > max_correct:
            max_correct = correct_count
            winners = [["Adrian", "Bruno", "Goran"][i]]
        elif correct_count == max_correct:
            winners.append(["Adrian", "Bruno", "Goran"][i])
    
    winners = sorted(winners)
    
    print(max_correct)
    for winner in winners:
        print(winner)

if __name__ == "__main__":
    main()