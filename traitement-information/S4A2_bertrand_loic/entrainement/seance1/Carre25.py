def encrypt(carre, message):
    encrypted_message = ""
    message = message.upper()
    message = message.replace('W', 'VV')
    for char in message:
        if char.isalpha():
            for y in range(0, len(carre)):
                for x in range(0, len(carre[y])):
                    if carre[x][y] == char:
                        encrypted_message += (str(x+1)+str(y+1)).strip()
    return encrypted_message


def decrypt(carre, message):
    decrypted_message = ""
    for position in range(0, len(message) - 2, 2):
        x = int(message[position])
        y = int(message[position + 1])
        decrypted_message += carre[x-1][y-1]
    return decrypted_message


def main():
    carre = [['A', 'B', 'C', 'D', 'E'],
              ['F', 'G', 'H', 'I', 'J'],
              ['K', 'L', 'M', 'N', 'O'],
              ['P', 'Q', 'R', 'S', 'T'],
              ['U', 'V', 'X', 'Y', 'Z']]

    message = "Le code de Polybe"
    encrypted_message = "3215133514151415413532541215"

    print(encrypt(carre, message))
    print(decrypt(carre, encrypted_message))


main()
