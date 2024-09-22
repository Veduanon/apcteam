from pwn import *
import time
from letters import LETTER_PATTERNS  # Импортируем шаблоны букв из файла letters.py

# Функция для разделения строки капчи на отдельные буквы по пробелам между ними
def save_letters_to_2d_array(captcha_response):
    lines = captcha_response.splitlines()

    if len(lines) < 3:
        print("Недостаточно строк для капчи")
        return []

    relevant_lines = lines[1:4]  # Используем первые 3 строки для анализа букв

    captcha_letters = []
    current_letter = []

    max_width = len(relevant_lines[0])  # Максимальная длина строки
    i = 0  # Индекс текущего столбца

    while i < max_width:
        # Проверяем, состоит ли текущий столбец из пробелов
        if all(line[i] == ' ' for line in relevant_lines):
            # Если буква завершена, добавляем её в captcha_letters
            if current_letter:
                captcha_letters.append(current_letter)
                current_letter = []
            i += 1  # Пропускаем пробел и двигаемся дальше
        else:
            # Если буква продолжается, добавляем столбец к текущей букве
            for j, line in enumerate(relevant_lines):
                if len(current_letter) <= j:
                    current_letter.append([])
                current_letter[j].append(line[i])
            i += 1

    # Добавляем последнюю букву, если она не была добавлена
    if current_letter:
        captcha_letters.append(current_letter)

    return captcha_letters

# Функция для сравнения двумерного массива буквы с шаблонами
def compare_letter_with_patterns(letter_array):
    for letter, pattern in LETTER_PATTERNS.items():
        if letter_array == pattern:
            return letter  # Возвращаем букву, если шаблон совпал
    return '?'  # Возвращаем "?", если буква не найдена

# Функция для распознавания капчи с учетом ограничения на 5 букв
def recognize_captcha(captcha_letters):
    recognized_text = ""
    max_letters = 5

    for letter in captcha_letters[:max_letters]:  # Ограничение на 5 букв
        recognized_letter = compare_letter_with_patterns(letter)
        recognized_text += recognized_letter

    # Если букв меньше 5, добавляем "?"
    if len(captcha_letters) < max_letters:
        recognized_text += '?' * (max_letters - len(captcha_letters))

    return recognized_text[:max_letters]  # Возвращаем ровно 5 букв

# Подключение к серверу и сбор капчи с использованием Pwntools
def connect_to_server(host, port):
    while True:
        try:
            # Подключаемся к серверу
            io = remote(host, port)
            print(f"Подключено к {host} на порту {port}")

            while True:
                # Отправляем запрос "start" для получения капчи
                io.sendline(b"start")
                
                # Задержка перед получением данных
                time.sleep(0.5)

                # Получаем данные с сервера
                response = io.recv(1024).decode('utf-8')
                if response:
                    print(f"Ответ сервера:\n{response}")
                    
                    # Разбираем капчу на буквы
                    captcha_letters = save_letters_to_2d_array(response)

                    # Выводим распознанные буквы (ровно 5 символов)
                    if captcha_letters:
                        recognized_text = recognize_captcha(captcha_letters)
                        print(f"Распознанный текст капчи: {recognized_text}")
                        
                        # Отправляем распознанный текст обратно на сервер
                        io.sendline(recognized_text.encode('utf-8'))
                        print(f"Отправлено на сервер: {recognized_text}")
                    else:
                        print("Капча не была распознана.")
                    
                    # Задержка в 1 секунду между запросами
                    time.sleep(1)
                else:
                    print("Нет ответа от сервера. Попробую переподключиться...")
                    break  # Выход из внутреннего цикла и попытка переподключения

            io.close()
        except Exception as e:
            print(f"Ошибка при подключении: {e}")
            time.sleep(5)  # Задержка перед повторной попыткой подключения

# Пример использования
if __name__ == "__main__":
    host = "212.34.152.215"
    port = 50090
    connect_to_server(host, port)
