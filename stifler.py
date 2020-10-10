import random

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']  # список слов для игры


def make_secret_word(words):
    """Return one of 6 words"""

    arbitrary_number = random.randint(0, len(words) - 1)
    return words[arbitrary_number]


def view_world(word_list):
    """Print current state of the word"""

    word = ''.join(word_list)
    return print('\nWord: \n', word + '\n')


def transform_word(secret_word):
    """Transform wold in list with '_' instead letters"""

    word_list = []  # Создаём список равный длине загаданного слова c '_' вместо букв
    i = 0
    while i < len(secret_word):
        word_list.append(' _ ')
        i += 1
    return word_list


def guess_word(word_list, secret_word):
    """Game engine"""

    tries = 0  # Счётчик попыток
    letters_box = []  # Список для вводимых букв

    while tries < 4:
        view_world(word_list)
        guess_letter = input("Введите букву: \n").lower()
        check = False  # Флаг для счётчика попыток

        if guess_letter in letters_box:  # Проверка вводилась ли такая буква ранее
            tries += 1
            message = '\nТакая буква уже называлась! Попыток осталось: {}'.format(4 - tries)
            print(message)

        else:

            for i, l in enumerate(secret_word):  # Перебираем загаданное слово и сверяем с введённой буквой
                letters_box.append(guess_letter)
                if l == guess_letter:
                    word_list[i] = ' {} '.format(guess_letter)
                    check = True
                    if ''.join(word_list).replace(' ', '').isalpha():
                        view_world(word_list)
                        return 'Вы победили! :)\n'

            if check == False:
                tries += 1
                message = '\nНет такой буквы! Попыток осталось: {}'.format(4 - tries)
                print(message)

    return 'Вы проиграли... :(\n'


def main():
    """Main function - destributor"""

    print("""

    «Загадано» одно из следующих слов: skillfactory, testing, blackbox, pytest, unittest, coverage.
    На отгадывание даётся 4 попытки. """)

    secret_word = make_secret_word(words)
    word_list = transform_word(secret_word)
    result = guess_word(word_list, secret_word)
    print(result)


if __name__ == "__main__":
    main()
