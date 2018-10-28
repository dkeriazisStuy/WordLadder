#!/usr/bin/python3
import sys
import heapq


def read_file(filename):
    with open(filename) as f:
        return f.read()


def write_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


def get_words():
    return read_file('dictall.txt').split('\n')


def remove_letter(word, i):
    return word[:i] + word[i+1:]


def get_neighbors(words, check_word):
    neighbors = set()
    for i in range(len(check_word)):
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        for c in ascii_lowercase:
            mod_word = check_word[:i] + c + check_word[i+1:]
            if mod_word != check_word and mod_word in words:
                neighbors.add(mod_word)
    return neighbors


def get_neighbors_dict(length):
    neighbors_dict = {}
    words = set(word for word in get_words() if len(word) == length)
    for word in words:
        neighbors_dict[word] = get_neighbors(words, word)
    return neighbors_dict


class Node:
    def __init__(self, val, cost, path):
        self.val = val
        self.cost = cost
        self.path = path

    def __repr__(self):
        return '({val};{cost};{path_str})'.format(
            val=self.val,
            cost=self.cost,
            path_str=','.join(self.path)
        )

    def __lt__(self, n):
        return self.cost < n.cost


def char_difference(a, b):
    """
    Return the number of different characters between strings `a` and `b`
    This requires `a` and `b` to be the same length
    """
    count = 0
    for i, c in enumerate(a):
        if b[i] != c:
            count += 1
    return count



def get_path(neighbors_dict, start, end):
    # Setup
    frontier = []
    explored = set()
    heapq.heappush(frontier, Node(start, 0, []))
    # Begin search
    while True:
        # If frontier is empty, give up
        if frontier == []:
            return None
        # Pop from frontier
        cur_node = heapq.heappop(frontier)
        # Check if current node is target
        if cur_node.val == end:
            return cur_node.path + [cur_node.val]
        # Neighbors into frontier
        neighbors = neighbors_dict[cur_node.val]
        for neighbor in neighbors:
            if neighbor not in explored:
                # Get cost so far
                cost = cur_node.cost + 1
                # Add in optimistic distance until target
                cost += char_difference(neighbor, end)
                n = Node(neighbor,
                        cost,
                        cur_node.path + [cur_node.val])
                heapq.heappush(frontier, n)
        # Push into explored
        explored.add(cur_node.val)


def main():
    _, in_file, out_file = sys.argv
    words = read_file(in_file).strip().split('\n')
    length = len(words[0].split(',')[0])
    paths = ((word.split(',')[0], word.split(',')[1]) for word in words)
    neighbors = get_neighbors_dict(length)
    result = ''
    for start, end in paths:
        print(start, end)
        path = get_path(neighbors, start, end)
        if path is None:
            path = [start, end]
        print(path)
        result += '{path_str}\n'.format(path_str=','.join(path))
    write_file(out_file, result)


if __name__ == "__main__":
    main()

