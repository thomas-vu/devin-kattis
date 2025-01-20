def can_place(plot_radius, house_radius):
    return plot_radius > house_radius

def can_place_square(plot_radius, square_side):
    diagonal = 2 ** 0.5 * square_side / 2
    return plot_radius > diagonal

def main():
    N, M, K = map(int, input().split())
    plots_radii = list(map(int, input().split()))
    circular_houses_radii = list(map(int, input().split()))
    square_houses_sides = list(map(int, input().split()))
    
    plots_radii.sort()
    circular_houses_radii.sort()
    square_houses_sides.sort()
    
    plot_index = 0
    house_index = 0
    square_house_index = 0
    
    while plot_index < N and (house_index < M or square_house_index < K):
        if house_index < M and can_place(plots_radii[plot_index], circular_houses_radii[house_index]):
            plot_index += 1
            house_index += 1
        elif square_house_index < K and can_place_square(plots_radii[plot_index], square_houses_sides[square_house_index]):
            plot_index += 1
            square_house_index += 1
        else:
            plot_index += 1
    
    print(house_index + square_house_index)

if __name__ == "__main__":
    main()