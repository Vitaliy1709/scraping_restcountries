# Country Information Scraper

Этот проект предназначен для получения, сортировки и отображения информации о странах, таких как официальное название, 
столица и ссылка на изображение флага. Данные загружаются из открытого API и выводятся в виде таблицы с использованием 
библиотеки `PrettyTable`.

## Описание

Скрипт загружает данные о странах с REST API, сортирует их по алфавиту по официальному названию страны, а затем 
отображает результат в виде таблицы. 
В таблице содержатся следующие столбцы:
- Назва країни (Официальное название страны)
- Назва столиці (Название столицы)
- Посилання на зображення прапору (png) (Ссылка на изображение флага)

### Используемые технологии

- `requests`: для отправки HTTP-запросов и получения данных.
- `PrettyTable`: для форматированного вывода данных в виде таблицы.

## Установка

1. Клонируйте репозиторий или скачайте файлы проекта.
2. Убедитесь, что у вас установлен Python 3.11 или выше.
3. Установите необходимые зависимости, используя `pip`:

    ```bash
    pip install requests prettytable
    ```

## Файлы

- `main.py`: основной скрипт, который загружает и отображает информацию о странах.
- `requirements.txt`: файл, содержащий список всех необходимых зависимостей.

## Использование

1. Запустите скрипт:

    ```bash
    python main.py
    ```

2. Скрипт загрузит данные о странах, отсортирует их и выведет в консоль таблицу с информацией о каждой стране.

## Пример вывода

```plaintext
+-----------------------------------+-------------------------+-------------------------------------------------+
|             Назва країни          |        Назва столиці     |   Посилання на зображення прапору (png)        |
+-----------------------------------+-------------------------+-------------------------------------------------+
|  Afghanistan                      | Kabul                   | https://flagcdn.com/w320/af.png                 |
|  Albania                          | Tirana                  | https://flagcdn.com/w320/al.png                 |
|  Algeria                          | Algiers                 | https://flagcdn.com/w320/dz.png                 |
|  ...                               | ...                     | ...                                            |
+-----------------------------------+-------------------------+-------------------------------------------------+
