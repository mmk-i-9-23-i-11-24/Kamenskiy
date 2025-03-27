import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    #string.ascii_letters = конкатенация ascii_lowercase и ascii_uppercase
    #string.digits - понятно
    #string.punctuation - тоже понянто
    password = ''.join(random.choice(characters) for _ in range(length))
    # ''--- это что будет между элементами списка, конкат. в строку(ничего
    # .join(characters) ---конкатенировать эл. списка characters
    # random.choice --- случ. выбранные функцией модуля random
    # for _ in range(length) -- в длину равен length
    return password
password_length = int(input("Введите желаемую длину пароля: "))
generated_password = generate_password(password_length)
print("Ваш сгенерированный пароль:", generated_password)

input("Вы хотите выйти из программы?\n-")