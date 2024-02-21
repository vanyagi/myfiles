def exc1_1():
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦУШЩЪЬЭЮЯ"
    alphabet = alphabet * 12
    message = input("\nВведите сообщение для шифрования: ")
    message = message.upper()
    key = int(input("Введите значение ключа для смещения: "))

    if (key < 0 or key > 300):
        print("Ошибка, задайте ключу значение в диапазоне целых чисел от 0 до 300")
        return

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

def exc1_2():
    message = input("\nВведите сообщение: ")
    key = input("Введите ключ: ")
    if len(message) != len(key):
        print("Ошибка! Строки должны совпадать по длине")

    enc_str = ""
    for i in range(0, len(message)):
        if message[i] == key[i]:
            enc_str = enc_str + "0"
        else:
            enc_str = enc_str + "1"
    print("Зашифрованное: " + enc_str)

    un_enc = ""
    for i in range(0, len(message)):
        if enc_str[i] == key[i]:
            un_enc = un_enc + "1"
        else:
            un_enc = un_enc + "0"
    print("Расшифрованное: " + un_enc)