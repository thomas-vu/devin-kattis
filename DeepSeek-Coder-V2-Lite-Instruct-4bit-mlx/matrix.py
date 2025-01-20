def matrix_inverse(a, b, c, d):
    det = a * d - b * c
    if det == 0:
        return None
    inv_det = 1 / det
    return [[int(d * inv_det), int(-b * inv_det)], [int(-c * inv_det), int(a * inv_det)]]

def main():
    case_number = 1
    while True:
        try:
            a, b = map(int, input().split())
            c, d = map(int, input().split())
            input()  # consume the blank line
        except EOFError:
            break
        
        inverse_matrix = matrix_inverse(a, b, c, d)
        if inverse_matrix:
            print("Case {}:".format(case_number))
            for row in inverse_matrix:
                print("{} {}".format(row[0], row[1]))
        case_number += 1

if __name__ == "__main__":
    main()