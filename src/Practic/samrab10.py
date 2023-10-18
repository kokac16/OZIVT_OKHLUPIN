#НАпишите программу для вввода предложения и подсчета слов в нём
input_string = input("Введите строку: ")
words = input_string.split()
word_count = len(words)
print(f"Количество слов в строке: {word_count}")