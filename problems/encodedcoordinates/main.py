def calculate_y(Px, Ay, By, Cy, Ky, Ny, x):
    def F(n):
        if n == 1:
            return Ax % Px
        elif n == 2:
            return (Ax + Bx + Cx) % Px
        for i in range(2, n):
            F_n = (G(i) + H(i - 1)) % Px
            G_n = (Ky * F(i) + H(i - 1)) % Px
            H_n = (F(i) + Ky * G(i)) % Px
            F_n, G_n, H_n = F(i), G_n, H_n
        return F(n) % Px
    
    def G(n):
        if n == 1:
            return Bx % Px
        elif n == 2:
            return (Ky * F(1) + Cx) % Px
        for i in range(2, n):
            F_n = (G(i) + H(i - 1)) % Px
            G_n = (Ky * F(i) + H(i - 1)) % Px
            H_n = (F(i) + Ky * G(i)) % Px
            F_n, G_n, H_n = F(i), G_n, H_n
        return G(n) % Px
    
    def H(n):
        if n == 1:
            return Cx % Px
        elif n == 2:
            return (F(1) + Ky * G(1)) % Px
        for i in range(2, n):
            F_n = (G(i) + H(i - 1)) % Px
            G_n = (Ky * F(i) + H(i - 1)) % Px
            H_n = (F(i) + Ky * G(i)) % Px
            F_n, G_n, H_n = F(i), G_n, H_n
        return H(n) % Px
    
    Ax, Bx, Cx, Kx, Nx = Ax, Bx, Cx, Kx, Nx
    Ay, By, Cy, Ky, Ny = Ay, By, Cy, Ky, Ny
    Px = Ax % Px
    
    if Nx == 1:
        y_coordinate = Ax % Px
    elif Nx == 2:
        y_coordinate = (Ax + Bx + Cx) % Px
    else:
        F_values = [Ax, (Ax + Bx + Cx) % Px]
        G_values = [Bx, (Ky * F_values[0] + Cx) % Px]
        H_values = [Cx, (F_values[0] + Ky * G_values[0]) % Px]
        for i in range(2, Nx):
            F_values.append((G_values[i - 1] + H_values[i - 2]) % Px)
            G_values.append((Ky * F_values[i] + H_values[i - 1]) % Px)
            H_values.append((F_values[i] + Ky * G_values[i]) % Px)
        y_coordinate = F_values[-1]
    
    return y_coordinate

# Read number of test cases
T = int(input())
for _ in range(T):
    Px = int(input())
    Ax, Bx, Cx, Kx, Nx = map(int, input().split())
    Ay, By, Cy, Ky, Ny = map(int, input().split())
    x_coordinate = int(input())
    
    y_coordinate = calculate_y(Px, Ay, By, Cy, Ky, Ny, x_coordinate)
    print(y_coordinate)