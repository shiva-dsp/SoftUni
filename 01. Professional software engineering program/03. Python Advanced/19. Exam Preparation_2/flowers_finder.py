from collections import deque

rose = {
    'r': 1,
    'o': 1,
    's': 1,
    'e': 1
}

tulip = {
    't': 1,
    'u': 1,
    'l': 1,
    'i': 1,
    'p': 1
}

lotus = {
    'l': 1,
    'o': 1,
    't': 1,
    'u': 1,
    's': 1
}

daffodil = {
    'd': 2,
    'a': 1,
    'f': 2,
    'o': 1,
    'i': 1,
    'l': 1
}

words = [rose, tulip, lotus, daffodil]

idx_map = {
    0: 'rose',
    1: 'tulip',
    2: 'lotus',
    3: 'daffodil'
}

vowels = deque(input().split(' '))
consonants = (input().split(' '))

is_found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for idx, word in enumerate(words):
        if current_vowel in word and word[current_vowel] > 0:
            word[current_vowel] -= 1
        if current_consonant in word and word[current_consonant] > 0:
            word[current_consonant] -= 1

        if sum(word.values()) == 0:
            word_found = idx_map[idx]
            is_found = True
            print(f'Word found: {word_found}')
            break
    if is_found:
        break

if not is_found:
    print(f'Cannot find any word!')

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")