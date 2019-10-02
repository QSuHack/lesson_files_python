from typing import List


def input_date(name_of_file: str):
    with open(name_of_file, "r") as f:
        return f.readline().split(" ")


def find_words(list_of_words: List[str]) -> List[str]:
    result = []
    for element in list_of_words:
        if element[-1] == "d" and element[0] == "d":
            result.append(element)
    return result


def encrypt(word: str, key: tuple) -> str:
    """

    :param word: string
    :param key: tuple or list of two integers
    :return: string
    """
    encrypted = ""
    for char in word:
        encrypted += chr(((ord(char) - 97) * key[0] + key[1]) % 26 + 97)
    return encrypted


def find_encrypt_key(text: str, encrypted_text: str) -> tuple:
    for A in range(0, 26):
        for B in range(0, 26):
            if encrypt(text, (A, B)) == encrypted_text.replace("\n", ""):
                return A, B


def find_decrypt_key(decrypted_text: str, text: str) -> tuple:
    for A in range(0, 26):
        for B in range(0, 26):
            if encrypt(text.replace("\n", ""), (A, B)) == decrypted_text:
                return A, B


if __name__ == "__main__":
    with open("wyniki.txt", mode="w+") as wyniki:
        input_ = input_date("tekst.txt")
        wyniki.write("Zadanie 75.1\n")
        wyniki.write(" ".join(find_words(input_)))
        wyniki.write("\nZadanie 75.2\n")
        for x in input_:
            if len(x) >= 10:
                wyniki.write(encrypt(x, (5, 2)))
                wyniki.write(" ")
        wyniki.write("\nZadanie 75.3\nSłowo  (Klucz Szyfrujący) (Klucz Deszyfrujący)\n")
        with open("probka.txt", mode="r") as sample:
            for line in sample.readlines():
                wyniki.write(
                    f"{line.split(' ')[0]} {find_encrypt_key(*line.split(' '))} {find_decrypt_key(*line.split(' '))}\n")
