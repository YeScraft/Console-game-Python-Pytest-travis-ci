# Skillfactory-module-e1_12-YeSergey (Игра Виселица - Python, Pytest, travis-ci)
[![Build Status](https://travis-ci.org/YeScraft/Skillfactory-module-e1_12-YeSergey.svg?branch=main)](https://travis-ci.org/YeScraft/Skillfactory-module-e1_12-YeSergey)

Для работы с приложением:
1. Скачайте приложение.
2. В cmd ввести: cd путь до папки с проектом;
3. Создать окружение: python –m venv имя_окружения;
4. Войти в окружение: имя_окружения\Scripts\activate.bat
5. Установить библиотеки: pip install -r requirements.txt;
6. Запустить приложение: python stifler.py

Задание:

В этом модуле нужно будет написать приложение, создать к нему pull request на github, написать тесты, посчитать покрытие ими кода и настроить непрерывную интеграцию с travis-ci.
Мы будем реализовывать игру в виселицу. Приложение «загадывает» одно из следующих слов: skillfactory, testing, blackbox, pytest, unittest, coverage. И показывает количество букв в нём.
Игрок пытается угадать слово буква за буквой. Если человек называет букву, которой нет в слове, у него появляется штрафное очко. А если букву, которая есть в слове, то она открывается (и все её вхождения).
Например, было загадано слово testing. На первом ходу игроку показывают: _ _ _ _ _ _ _.
Допустим, пользователь предположил, что в этом слове есть буква a. Изображение слова остаётся такое же: _ _ _ _ _ _ _, но у пользователя появляется штрафное очко.
Допустим, на следующем ходу пользователь предлагает букву t. Тогда изображение слова меняется, игроку открывается буква t: T _ _ T _ _ _.
Если набирается 4 штрафных очка и слово не отгадано, игра проиграна.
Приложение должно управляться через командную строку.
