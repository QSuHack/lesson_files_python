print("Szyfr Vigenère’a \nSzyfrowanie dla wielkich liter ze spacjami, klucz dowolny >1")
word = input("Podaj słowo: ")
key = input("Podaj klucz: ")


def encryption(word, key):
    index = 0
    encrypted = ""
    for char in word:
        if char == " ":
            encrypted += " "
            continue
        if index > (len(key) - 1):
            index %= (len(key) - 1)
        encrypted += chr(((ord(char) - 65 + ord(key[index]) - 65) % 26) + 65)
        index += 1
    return encrypted


def decryption(word, key):
    index = 0
    decrypted = ""
    for char in word:
        if char == " ":
            decrypted += " "
            continue
        if index > (len(key) - 1):
            index %= (len(key) - 1)
        decrypted += chr(((ord(char) - 65 - ord(key[index]) - 65) % 26) + 65)
        index += 1
    return decrypted


print(encryption(word, key))
print(decryption(encryption(word, key), key))
