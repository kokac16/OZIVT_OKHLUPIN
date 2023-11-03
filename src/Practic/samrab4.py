forbidden_words = []
with open('zapret_slov.txt', 'r', encoding='utf-8') as file:
    forbidden_words = file.read().split()

sentence = input("Введите предложение: ")

words = sentence.split()
censored_sentence = []

for word in words:
    lowercase_word = word.lower()
    if lowercase_word in forbidden_words:
        censored_word = '*' * len(word)
        censored_sentence.append(censored_word)
    else:
        censored_sentence.append(word)

censored_text = ' '.join(censored_sentence)
print("Замененное предложение:", censored_text)