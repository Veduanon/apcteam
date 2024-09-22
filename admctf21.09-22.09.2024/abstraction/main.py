from stegano import lsb

def extract_message(image_path):
    try:
        secret_message = lsb.reveal(image_path)
        if secret_message:
            return f"Скрытое сообщение: {secret_message}"
        else:
            return "Скрытых сообщений не найдено."
    except IndexError as e:
        return f"Ошибка: индекс пикселя выходит за границы изображения. {e}"
    except Exception as e:
        return f"Произошла ошибка при извлечении: {str(e)}"

# Пример использования
image_path = 'Abstraction.png'
print(extract_message(image_path))
