stringus = input("Введите слово: ")
count = 0
glasnie = set("aeiouуеаоэяиюё")
for letter in stringus:
    if letter in glasnie:
        count += 1
print("Гласных букв: " + str(count))

input("Вы хотите выйти из программы?\n-")