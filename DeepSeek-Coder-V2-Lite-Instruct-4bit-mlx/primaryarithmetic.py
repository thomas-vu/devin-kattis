def count_carry_operations(num1, num2):
    carry = 0
    carry_count = 0
    while num1 > 0 or num2 > 0:
        digit_sum = (num1 % 10) + (num2 % 10) + carry
        if digit_sum >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
        num1 //= 10
        num2 //= 10
    return carry_count

while True:
    line = input()
    if line == "0 0":
        break
    num1, num2 = map(int, line.split())
    carry_count = count_carry_operations(num1, num2)
    if carry_count == 0:
        print("No carry operation.")
    else:
        print(f"{carry_count} carry operations.")