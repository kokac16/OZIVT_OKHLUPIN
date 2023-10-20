
sentence = input("Введите предложение на английском: ")


print("Длина предложения:", len(sentence))


sentence_lower = sentence.lower()
print("В нижнем регистре:", sentence_lower)


vowels = "aeiou"
vowel_count = sum(1 for char in sentence_lower if char in vowels)
print("Количество гласных:", vowel_count)

sentence_replaced = sentence.replace("ugly", "beauty")
print("Замена 'ugly' на 'beauty':", sentence_replaced)


starts_with_the = sentence_lower.startswith("the")
ends_with_end = sentence_lower.endswith("end")

if starts_with_the and ends_with_end:
    print("Предложение начинается с 'The' и заканчивается на 'end'.")
else:
    print("Предложение не соответствует условию 'The' в начале и 'end' в конце.")