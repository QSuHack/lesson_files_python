from typing import List


def encrypt(information: List[str], key: List[int]) -> str:
    for num in range(0, len(information)):
        index = key[num % (len(key))] - 1
        information[num], information[index] = information[index], information[num]
        print("".join(information))
    return "".join(information)


def load_key(key: str) -> List[int]:
    return [int(x) for x in key.replace("\n", "").split(" ")]


if __name__ == "__main__":
    import os

    print(os.getcwd())
    with open("wyniki76.txt", mode="w+")as result_file:
        result_file.write("\nZadanie 76.1\n")
        with open("szyfr1.txt") as encrypted_one:
            napisy = []
            for x in range(0, 6):
                napisy.append(encrypted_one.readline().replace("\n", ""))
            first_key = load_key(encrypted_one.readline())
            for x in napisy:
                result_file.write(f'{encrypt(list(x), first_key)}\n')

        with open("szyfr2.txt") as encrypted_one:
            result_file.write("\nZadanie 76.2\n")
            result_file.write(f"{encrypt(list(encrypted_one.readline()[0:-1]), load_key(encrypted_one.readline()))}")
        with open("szyfr3.txt") as encrypted_one:
            enc = encrypted_one.readline().replace("\n", "")
            print(encrypt(list(enc.replace("\n", "")), [6, 2, 4, 1, 5, 3]))
