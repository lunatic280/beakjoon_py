word = input()

alphabet_count = 26

alphabet = [-1] * alphabet_count

for i in range(len(word)):
    char = word[i]
    found = ord(char) - ord('a')
    if alphabet[found] == -1:
        alphabet[found] = i

for i in alphabet:
    print(i, end=" ")