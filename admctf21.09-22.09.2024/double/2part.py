# Открываем исходный файл в бинарном режиме для чтения
with open('haha.txt', 'rb') as f_in:
    data = f_in.read()

# Извлекаем каждый второй байт, начиная с байта с индексом 0 (чётные байты)
data_even = data[::2]

# Извлекаем каждый второй байт, начиная с байта с индексом 1 (нечётные байты)
data_odd = data[1::2]

# Сохраняем данные в отдельные файлы
with open('output_even.png', 'wb') as f_out_even:
    f_out_even.write(data_even)

with open('output_odd.png', 'wb') as f_out_odd:
    f_out_odd.write(data_odd)
