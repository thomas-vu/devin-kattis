def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        first_list = [int(input()) for _ in range(n)]
        second_list = [int(input()) for _ in range(n)]
        
        # Create a dictionary to map the values from the first list to their positions in the second list
        position_map = {value: index for index, value in enumerate(first_list)}
        
        # Reorder the second list based on the positions in the first list
        reordered_second_list = [0] * n
        for index, value in enumerate(second_list):
            reordered_index = position_map[value]
            reordered_second_list[reordered_index] = value
        
        # Print the reordered second list
        for value in reordered_second_list:
            print(value)
        print()

if __name__ == "__main__":
    main()