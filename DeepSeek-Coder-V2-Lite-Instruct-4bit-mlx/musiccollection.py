def find_shortest_substring(songs):
    def unique_identifier(song):
        song = song.lower()
        min_substring = None
        for i in range(len(song)):
            for j in range(i + 1, len(song) + 1):
                substring = song[i:j]
                if all(substring in s.lower() for s in songs):
                    if min_substring is None or len(substring) < len(min_substring):
                        min_substring = substring
                    elif len(substring) == len(min_substring):
                        min_substring = min(min_substring, substring)
        return min_substring
    
    results = []
    for song in songs:
        identifier = unique_identifier(song)
        if identifier is not None:
            results.append('"' + identifier + '"')
        else:
            results.append(':(')
    return results

def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        songs = [input().strip() for _ in range(N)]
        results = find_shortest_substring(songs)
        print("Case #{}:".format(t))
        for result in results:
            print(result)

if __name__ == "__main__":
    main()