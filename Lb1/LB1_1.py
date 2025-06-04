def word_count(text):
    words = text.lower().split()

    count_dict = {}
    for word in words:
        word = word.strip('.,!?":;()[]{}')
        if word:
            count_dict[word] = count_dict.get(word, 0) + 1

    frequent_words = [word for word, count in count_dict.items() if count > 3]

    return count_dict, frequent_words

text = "Це приклад тексту, в якому слово тексту з’являється більше ніж просто текст. Текст, текст, текст!"
result_dict, frequent_words = word_count(text)

print("Словник частоти слів:")
print(result_dict)

print("\nСлова, що зустрічаються більше 3 разів:")
print(frequent_words)
