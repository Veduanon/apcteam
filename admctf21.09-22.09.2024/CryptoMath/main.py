N = 300
encoded = ['440', '30', '282', '432', '348', '420', '254', '432', '272', '66', '280', '416', '545', '315', '282', '540', '525', '412', '315', '432', '292', '540', '284', '372', '545', '366', '294', '545', '250']

flag = ''

for target in encoded:
    # Перебор всех возможных значений ASCII от 1 до 127
    for ascii_val in range(1, 127):
        if str(N // ascii_val) + str(N % ascii_val) == target:
            flag += chr(ascii_val)
            break

print(f"Recovered flag: {flag}")
