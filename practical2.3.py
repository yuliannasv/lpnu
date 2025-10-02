def caesar_cipher(text, shift, encrypt=True):
    ukrainian_uppercase = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    ukrainian_lowercase = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

    result = ""

    if not encrypt:
        shift = -shift

    for char in text:
        if char in ukrainian_uppercase:
            index = (ukrainian_uppercase.index(char) + shift) % len(ukrainian_uppercase)
            result += ukrainian_uppercase[index]
        elif char in ukrainian_lowercase:
            index = (ukrainian_lowercase.index(char) + shift) % len(ukrainian_lowercase)
            result += ukrainian_lowercase[index]
        else:
            result += char

    return result


if __name__ == "__main__":
    text_to_encrypt = "Привіт, світ!"
    shift_value = 3

    encrypted_text = caesar_cipher(text_to_encrypt, shift_value, encrypt=True)
    print(f"Зашифрований текст: {encrypted_text}")

    decrypted_text = caesar_cipher(encrypted_text, shift_value, encrypt=False)
    print(f"Розшифрований текст: {decrypted_text}")