import pytest
import stifler
import input_test_base

test_list = ['one', 'two', 'three', 'four']
result_list = []
test_word = 'test'
test_word_list = [' _ ', ' _ ', ' _ ', ' _ ']


def test_get_arbitrary_world():
    i = 0
    while i < len(test_list):
        chosen_word = stifler.make_secret_word(test_list)
        result_list.append(chosen_word)
        i += 1
    assert result_list != test_list and set(result_list).issubset(test_list)


@pytest.mark.xfail()
def test_get_not_arbitrary_world():
    i = 0
    while i < len(stifler.words):
        chosen_word = stifler.make_secret_word(stifler.words)
        result_list.append(chosen_word)
        i += 1
    assert stifler.words == stifler.words and set(result_list).issubset(stifler.words)


def test_transform_word():
    result = stifler.transform_word(test_word)
    assert result == test_word_list


def test_guess_word_success():
    input_test_base.set_keyboard_input(['t', 'e', 's', 't'])
    result = stifler.guess_word(test_word_list, test_word)
    assert result == 'Вы победили! :)\n'


def test_guess_word_double_letter():
    test_word_d = 'ab'
    test_word_list_d = [' _ ', ' _ ']
    input_test_base.set_keyboard_input(['a', 'a', 'b'])
    stifler.guess_word(test_word_list_d, test_word_d)
    result = input_test_base.get_display_output()
    assert result == ['\nWord: \n _  _ \n',
                      "Введите букву: \n",
                      '\nWord: \n a  _ \n',
                      "Введите букву: \n",
                      '\nТакая буква уже называлась! Попыток осталось: 3',
                      '\nWord: \n a  _ \n',
                      'Введите букву: \n',
                      '\nWord: \n a  b \n']


def test_guess_word_nope_letter():
    test_word_d = 'ab'
    test_word_list_d = [' _ ', ' _ ']
    input_test_base.set_keyboard_input(['a', 'c', 'b'])
    stifler.guess_word(test_word_list_d, test_word_d)
    result = input_test_base.get_display_output()
    assert result == ['\nWord: \n _  _ \n',
                      "Введите букву: \n",
                      '\nWord: \n a  _ \n',
                      "Введите букву: \n",
                      '\nНет такой буквы! Попыток осталось: 3',
                      '\nWord: \n a  _ \n',
                      'Введите букву: \n',
                      '\nWord: \n a  b \n']


def test_guess_word_fail():
    input_test_base.set_keyboard_input(['z', 'v', 'z', 'y'])
    result = stifler.guess_word(test_word_list, test_word)
    print(result)
    assert result == 'Вы проиграли... :(\n'


def test_guess_word_4_tries():
    input_test_base.set_keyboard_input(['z', 'z', 'z', 'z', 'z'])
    stifler.guess_word(test_word_list, test_word)
    result = input_test_base.get_display_output()
    result_str = ''.join(result)
    assert result_str.count('Попыток осталось') == 4

