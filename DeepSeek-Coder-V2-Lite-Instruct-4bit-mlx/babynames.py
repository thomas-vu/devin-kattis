class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.gender_count = [0, 0]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, gender):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if gender == 1:
                node.gender_count[0] += 1
            elif gender == 2:
                node.gender_count[1] += 1
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return [0, 0]
            node = node.children[char]
        return node.gender_count

    def remove(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
        if node.is_end_of_word:
            node.is_end_of_word = False
            while node and not node.children:
                parent = node
                char_to_remove = None
                for key, child in parent.children.items():
                    char_to_remove = key
                    node = child
                del parent.children[char_to_remove]

def main():
    trie = Trie()
    while True:
        command = input().split()
        if command[0] == '0':
            break
        elif command[0] == '1':
            _, babyName, genderSuitability = command
            trie.insert(babyName, int(genderSuitability))
        elif command[0] == '2':
            _, babyName = command
            trie.remove(babyName)
        elif command[0] == '3':
            _, start, end, genderSuitability = command
            count_male = 0
            count_female = 0
            if genderSuitability == '0':
                count_male, count_female = trie.search(start)
            elif genderSuitability == '1':
                count_male = trie.search(start)[0]
            elif genderSuitability == '2':
                count_female = trie.search(start)[1]
            print(count_male if genderSuitability == '1' else count_female)

if __name__ == "__main__":
    main()