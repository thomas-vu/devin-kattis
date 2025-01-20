MOD = 10**9 + 7

def factorial(n):
    f = [1] * (n + 1)
    for i in range(2, n + 1):
        f[i] = (f[i - 1] * i) % MOD
    return f

def count_ways(n, word_lengths, dictionary):
    word_count = {}
    for word in dictionary:
        word_count[len(word)] = word_count.get(len(word), 0) + 1
    
    ways = 1
    for w_i in word_lengths:
        if w_i not in word_count or word_count[w_i] == 0:
            return 0
        ways = (ways * word_count[w_i]) % MOD
        word_count[w_i] -= 1
    
    return ways

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        word_lengths = list(map(int, input().split()))
        d = int(input())
        dictionary = [input().strip() for _ in range(d)]
        print(count_ways(n, word_lengths, dictionary))

if __name__ == "__main__":
    main()