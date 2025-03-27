string = input("Введите слово: ")
new_string = ""
count = 0
for character in string:
    count += 1
    if count == 1:
        new_string += character
    elif count % 3 == 0:
        new_string += "*"
    else:
        new_string += character
print(new_string)

input("Вы хотите выйти из программы?\n- ")