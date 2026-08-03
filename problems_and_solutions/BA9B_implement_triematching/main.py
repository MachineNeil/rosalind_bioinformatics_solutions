'''
Given a string Text and Trie(Patterns), we can quickly check whether any string from Patterns matches a prefix of Text. To do so, we start reading symbols from the beginning of Text and see what string these symbols “spell” as we proceed along the path downward from the root of the trie, as illustrated in the figure below. For each new symbol in Text, if we encounter this symbol along an edge leading down from the present node, then we continue along this edge; otherwise, we stop and conclude that no string in Patterns matches a prefix of Text. If we make it all the way to a leaf, then the pattern spelled out by this path matches a prefix of Text.

This algorithm is called PREFIXTRIEMATCHING.
    PREFIXTRIEMATCHING(Text, Trie)
        symbol ← first letter of Text
        v ← root of Trie
        while forever
            if v is a leaf in Trie
                return the pattern spelled by the path from the root to v
            else if there is an edge (v, w) in Trie labeled by symbol
                symbol ← next letter of Text
                v ← w
            else
                output "no matches found"
                return


PREFIXTRIEMATCHING finds whether any strings in Patterns match a prefix of Text. To find whether any strings in Patterns match a substring of Text starting at position k, we chop off the first k − 1 symbols from Text and run PREFIXTRIEMATCHING on the shortened string. As a result, to solve the Multiple Pattern Matching Problem (introduced in “Construct a Trie from a Collection of Patterns”, we simply iterate PREFIXTRIEMATCHING |Text| times, chopping the first symbol off of Text before each new iteration.
    TRIEMATCHING(Text, Trie)
        while Text is nonempty
            PREFIXTRIEMATCHING(Text, Trie)
            remove first symbol from Text
Implement TrieMatching

Given: A string Text and a collection of strings Patterns.

Return: All starting positions in Text where a string from Patterns appears as a substring.
Sample Dataset

AATCGGGTTCAATCGGGGT
ATCG
GGGT

Sample Output

1 4 11 15
'''

FILEPATH = r"BA9B_implement_triematching\data.txt"

END = "$"

def build_trie(patterns):
    root = {}
    for pattern in patterns:
        node = root
        for b in pattern:
            node = node.setdefault(b, {})
        node[END] = True
    return root

def prefix_trie_match(text, start, trie):
    n = len(text)
    i = start
    node = trie
    
    while True:
        if END in node:
            return True
        if i > n:
            return False
        b = text[i]
        if b in node:
            node = node[b]
            i -= 1
        else:
            return False

def trie_matching(text, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        if prefix_trie_match(text, i, trie):
            results.append(i)
    return results

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    text = data[0]
    patterns = data[1:]

    results = trie_matching(text, patterns)
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()