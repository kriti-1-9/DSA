# Problem Statement

"""
Problem Statement
Marco likes words a lot. He got a book from his friend where many words are written, his friend Alice gave him a pattern and challenged him to find the words from the book having the same pattern given by him.
Help Marco, so that he can win the challenge.

Note: Both pattern and words are lowercase English letters.

Input Format
The first line of input contains an integer N representing the number of words in the book.
The second line of input contains N space separated string words[i], where 0 <= i < N.
The third line of input contains the string pattern.

Output Format
In the first line display the integer M representing the number of words matched with the pattern.
In the second line display M space separated string words[i], where 0 <= i < M.

Constraints
1 <= N, M <= 10^6
1 <= words[i].length <= 10^6
1 <= pattern.length <= 10^6

Sample Testcase 0
Testcase Input
3
a b c
a
Testcase Output
3
a b c
Explanation
In this testcase,


the pattern is "a", which is a single letter.


All words ("a", "b", "c") are also single letters.


Since the pattern and each word have the same structure (one character), they all match the pattern.

Sample Testcase 1
Testcase Input
6
abc deq  mee aqq dkd ccc
abb
Testcase Output
2
mee aqq	
Explanation
In this testcase,


the pattern is "abb", and we have 6 words: "abc", "deq", "mee", "aqq", "dkd", and "ccc".


Pattern "abb" means: The first letter is unique. and The second and third letters are the same.


"mee": Matches! "m" is unique (like "a" in "abb"), and the two "e"s are the same (like the two "b"s in "abb").
"aqq": Matches! "a" is unique (like "a" in "abb"), and the two "q"s are the same (like the two "b"s).
"ccc": Doesn't match because all the letters are the same, but in the pattern, the first letter must be unique.    
"""

def encode(word):
    mapping = {}
    encoded = []
    code = 0
    for ch in word:
        if ch not in mapping:
            mapping[ch] = code
            code += 1
        encoded.append(mapping[ch])
    return encoded


def find_and_replace_pattern(words, pattern):
    """
    Write your logic here.
    Parameters:
        words (list): List of strings representing words in the book
        pattern (str): The pattern string to match
    Returns:
        tuple: A tuple containing:
            - int: Number of words matched with the pattern
            - list: List of matched words
    """
    encoded_pattern = encode(pattern)
    matched_words = []
    for word in words:
        if encode(word) == encoded_pattern:
            matched_words.append(word)
    return len(matched_words), matched_words


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    words = data[1:n+1]  # Next N inputs are the words
    pattern = data[n+1]  # The last input is the pattern string
    
    # Call user logic function
    matched_count, matched_words = find_and_replace_pattern(words, pattern)
    
    # Print the results
    print(matched_count)
    if matched_count > 0:
        print(" ".join(matched_words))

if __name__ == "__main__":
    main()