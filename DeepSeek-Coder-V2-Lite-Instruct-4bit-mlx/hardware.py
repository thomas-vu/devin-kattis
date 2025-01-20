def count_digits(house_numbers):
    digit_count = [0] * 10
    for number in house_numbers:
        for digit in str(number):
            digit_count[int(digit)] += 1
    return digit_count

def main():
    n = int(input())
    for _ in range(n):
        road_name = input()
        addresses = int(input().split()[2])
        house_numbers = []
        
        while True:
            line = input().strip()
            if not line or line[0] == '+':
                break
            house_numbers.append(int(line))
        
        while line[0] == '+':
            _, first, last, interval = map(int, line.split()[1:])
            while first <= last:
                house_numbers.append(first)
                first += interval
            line = input().strip()
        
        digit_count = count_digits(house_numbers)
        print(road_name)
        print("{} addresses".format(addresses))
        
        for i in range(10):
            print("Make {} digit {}".format(digit_count[i], i))
        total_digits = sum(digit_count)
        if total_digits == 1:
            print("In total {} digit".format(total_digits))
        else:
            print("In total {} digits".format(total_digits))
        
        if _ < n - 1:
            print()

if __name__ == "__main__":
    main()