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


def get_path(neighbors, start, dist_node):
    frontier = {}
    explored = {}


def main():
    _, in_file, out_file = sys.argv
    words = read_file(in_file).strip().split('\n')
    neighbors = get_neighbors_dict(len(words[0]))
    result = ''
    for word in words:
        length = len(neighbors[word])
        result += '{word},{length}\n'.format(word=word, length=length)
    write_file(out_file, result)


if __name__ == "__main__":
    main()

