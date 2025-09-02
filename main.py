def caesar_cipher(text, shift):
    lower_text = "" # Stocke le texte en minuscule
    upper_cases = [] # Stocke les positions des lettres majuscules
    result = "" # Stocke le texte chiffré


    for char in text: # recupere la position de tous les caractere majuscule et les convertit en minuscule
            if char.isupper():
                position = text.index(char)
                upper_cases.append((position))
                char = char.lower()
                
            lower_text += char


    for char in lower_text: # chiffre chaque caractere sauf 'espace'
        number = ord(char)

        if number == 32:
            result += " "
            continue
        else:
            cipher_number = number + shift
        
        if cipher_number > 122:
            cipher_number = -122 + cipher_number
            cipher_number += 96
        result += chr(cipher_number)


    for index in upper_cases: # remet les majuscules a leur position initiale
        result = result[:index] + result[index].upper() + result[index + 1:]
    return result


cipher_text = caesar_cipher("ContribUteur", 3)
print(cipher_text)