def is_palindrom(word):
    if " " in word:
        word = "".join(word.split(" "))

    word = word.lower()
    
    i = 0
    word_len = len(word) - 1
    
    while word_len >= i:
        if word[word_len] == word[i]:
            word_len -= 1
            i = i + 1
        else:
            return False
    return True

while True:
    word = input('Enter word: ')
    if word == '0':
        break
    
    print(is_palindrom(word))