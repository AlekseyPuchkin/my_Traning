import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']  # Символы для удаления
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    # Удаляем только указанные символы
                    for p in punctuation:
                        text = text.replace(p, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # Позиция начинается с 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[name] = count
        return result

if __name__ == "__main__":
    # Создание тестовых файлов
    with open('file1.txt', 'w', encoding='utf-8') as f1:
        f1.write("It's a text for task Найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\n"
                 "text")

    with open('file2.txt', 'w', encoding='utf-8') as f2:
        f2.write("Это TeXt, tExT, tEXt из файла номер 2\nОн тоже тестовый.\n"
                 "Цель: применить на практике оператор with\n"
                 "вспомнить написание кода в парадигме ООП.")

    with open('file3.txt', 'w', encoding='utf-8') as f3:
        f3.write("Это TEXT, TEXT, TEXT, TEXT из файла 3.\nОн дружественный,\nОн знает своё место.")

    # Тестирование класса
    finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')

    # Получаем все слова
    all_words_result = finder.get_all_words()
    print("Все слова из файлов:")
    for file_name, words in all_words_result.items():
        print(f"{file_name}: {words}")

    # Поиск слова 'text'
    find_result = finder.find('text')
    print("\nРезультат поиска слова 'text':")
    for file_name, position in find_result.items():
        print(f"{file_name}: позиция {position}")

    # Подсчёт слова 'text'
    count_result = finder.count('text')
    print("\nКоличество найденных слов 'text':")
    for file_name, count in count_result.items():
        print(f"{file_name}: {count} раз(а)")