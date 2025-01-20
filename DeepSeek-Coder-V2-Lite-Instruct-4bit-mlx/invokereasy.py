def parse_input(s):
    a, b = map(int, s.split())
    return complex(a, b)

def main():
    a_str, b_str = input().strip(), input().strip()
    your_source = parse_input(a_str)
    opponent_source = parse_input(b_str)
    
    # Calculate the resulting source after neutralizing the opponent
    resulting_source = your_source / opponent_source
    
    # Output the result in the required format
    print(f"{resulting_source.real:.20f} {resulting_source.imag:.20f}")

if __name__ == "__main__":
    main()