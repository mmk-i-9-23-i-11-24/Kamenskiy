import random
pc_numba = random.randint(1, 10)
man_numba = int(input("Загадано число от 1 до 10.\nУгадай что загадал: "))
if man_numba == pc_numba:
    print("Угадал, это " + str(pc_numba))
else:
    print("Не угадал, " + str(man_numba) + " - неправильное число.")

input("Вы хотите выйти из программы?\n-")