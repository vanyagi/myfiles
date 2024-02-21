message = input("\nВведите сообщение: ")
key = input("Введите ключ: ")

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