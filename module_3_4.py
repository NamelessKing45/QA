def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word or root_word.lower() in word or root_word.upper() in word:same_words.append(word)
        elif word in root_word or word.lower() in root_word or word.upper() in root_word:same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'{result1}\n{result2}')
