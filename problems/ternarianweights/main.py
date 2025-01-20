def ternarian_weighing(n, weights):
    for i in range(n):
        weight = int(input())
        left_pan, right_pan = [], []
        
        while weight > 0:
            for w in weights:
                if (weight - w) >= 0:
                    weight -= w
                    left_pan.append(w)
                else:
                    right_pan.append(w)
        
        left_pan = [str(x) for x in sorted(left_pan, reverse=True)]
        right_pan = [str(x) for x in sorted(right_pan, reverse=True)]
        
        print("left pan:", " ".join(left_pan))
        print("right pan:", " ".join(right_pan))
        if i < n - 1:
            print()

# Define the weights for base 3 powers up to 27 (3^3)
weights = [1, 3, 9, 27, 81, 243]
n = int(input())
ternarian_weighing(n, weights)