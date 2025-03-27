def reversed1(variable):
    res = ''
    for i in range(len(variable)-1,-1,-1):
        res += variable[i]
    return res
n = input("Введите слово, которое нужно проверить на палиндромность: ")
fff = reversed1(n)
if n == fff:
    print(n + " - это палиндром.")
else:
    print(n + " - это не палиндром.")


input("Вы хотите выйти из программы?\n-")