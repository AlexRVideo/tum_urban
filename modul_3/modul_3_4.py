def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for word in other_words:
        word_lower = word.lower()
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)

    return same_words

result1 = single_root_words('шич', 'шичме', 'модыш', 'локшичмыла', 'шичшыжла')
result2 = single_root_words('Мод', 'Модыш', 'Модыкташ', 'Нимодымо', 'Омыдымо')

print(result1)
print(result2)