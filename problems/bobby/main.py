def should_bobby_take_the_bet(R, S, X, Y, W):
    # Calculate the probability of not rolling at least R in a single roll
    prob_not_roll_at_least_R = (S - R) / S
    # Calculate the probability of not rolling at least R in Y rolls
    prob_not_roll_at_least_R_Y = (prob_not_roll_at_least_R) ** Y
    # Calculate the probability of rolling at least R in X out of Y rolls
    prob_roll_at_least_R_X = 1 - prob_not_roll_at_least_R_Y
    # Calculate the expected return in terms of W times the original bet
    expected_return = (W * prob_roll_at_least_R_X) - 1
    if expected_return > 0:
        return "yes"
    elif expected_return < 0:
        return "no"
    else:
        return "no"

# Read the number of cases
N = int(input())
for _ in range(N):
    R, S, X, Y, W = map(int, input().split())
    result = should_bobby_take_the_bet(R, S, X, Y, W)
    print(result)