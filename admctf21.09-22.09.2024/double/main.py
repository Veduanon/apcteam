# Открываем исходный файл в бинарном режиме для чтения
with open('output.txt', 'rb') as f_in:
    data = f_in.read()

# Удаляем каждый второй байт
cleaned_data = data[::3]

# Записываем очищенные данные в новый файл
with open('output2.txt', 'wb') as f_out:
    f_out.write(cleaned_data)
