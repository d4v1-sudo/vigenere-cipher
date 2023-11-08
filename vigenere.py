def generateKey(string, key):
    key = list(key)
    key_length = len(key)
    if len(string) == key_length:
        return key
    else:
        extended_key = [key[i % key_length] for i in range(len(string))]
        return ''.join(extended_key)

def vigenere(string, key, mode):
    result = []
    for i in range(len(string)):
        if string[i].isalpha():
            shift = ord('A' if string[i].isupper() else 'a')
            key_shift = ord(key[i]) - shift
            if mode == "e":
                x = (ord(string[i]) - shift + key_shift) % 26
            elif mode == "d":
                x = (ord(string[i]) - shift - key_shift + 26) % 26
            x += shift
            result.append(chr(x))
        else:
            result.append(string[i])
    return ''.join(result)

if __name__ == "__main__":
    string = input("Text to process: ")
    keyword = input("Keyword: ")
    mode = input("Encrypt or decrypt? (Type 'e' or 'd'): ").lower()
    if mode not in ["e", "d"]:
        print("Invalid mode. Please enter 'e' or 'd'.")
    else:
        key = generateKey(string, keyword)
        result = vigenere(string, key, mode)
        if mode == "e":
            print("Ciphertext:", result)
        else:
            print("Original/Decrypted Text:", result)
