class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.level = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            curr_node.level += 1
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.level += 1
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        count = 0
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return count

        if curr_node.level == 1:
            return True
        else:
            return False


def solution(words):
    T = Trie()

    for w in words:
        T.insert(w)




print(solution(["abc","def","ghi","jklm"]))
