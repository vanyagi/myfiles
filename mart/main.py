alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦУШЩЪЬЭЮЯ"
alphabet = alphabet * 3
message = input("\nВведите сообщение для шифрования: ")
message = message.upper()
key = int(input("Введите значение ключа для смещения: "))
new_message = ""
for letter in message:
    if letter == " ":
        new_message = new_message + " "
    else:
        index = alphabet.find(letter)
        new_ind = index + key
        new_message = new_message + alphabet[new_ind]

print(new_message)
old_message = ""
for letter in new_message:
    if letter == " ":
        old_message = old_message + " "
    else:
        index = alphabet.find(letter)
        new_ind = index - key
        old_message = old_message + alphabet[new_ind]

print(old_message)