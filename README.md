# 🧩🔒 - Vigenere Cipher

This Python script implements the Vigenere cipher for encrypting and decrypting text based on a provided keyword.

## Usage

1. **Clone the Repository:**
   ```bash
   https://github.com/d4v1-sudo/vigenere-cipher.git
   cd vigenere-cipher
   ```

2. **Run the Script:**
   ```bash
   python3 vigenere_cipher.py
   ```

3. **Follow the Prompts:**
   - Enter the text to be processed.
   - Enter the keyword for encryption or decryption.
   - Choose to encrypt or decrypt by typing 'e' or 'd' accordingly.

## Script Description

The Python script consists of two functions:

### `generateKey(string, key)`

This function generates a key of the same length as the input string by repeating the provided keyword. If the lengths are already equal, the key is returned as is.

### `vigenere(string, key, mode)`

This function performs the Vigenere cipher operation on the input string using the provided key and specified mode ('e' for encryption or 'd' for decryption).

- Encryption (`mode == "e"`): Encrypts the input text using the Vigenere cipher.
- Decryption (`mode == "d"`): Decrypts the input text using the Vigenere cipher.

## Example

```bash
Text to process: HelloWorld
Keyword: KEY
Encrypt or decrypt? (Type 'e' or 'd'): e
Ciphertext: RiJvsPvyG
```

## Note

- Make sure to only enter alphabetic characters in the input text.
- The keyword should consist of alphabetic characters only.

Feel free to use and modify the script for your cryptographic needs. If you encounter any issues or have suggestions for improvements, please let us know.

<a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2Fvigenere-cipher"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2Fvigenere-cipher&label=Thanks%20for%20dropping%20in&labelColor=%23000000&countColor=%23FFFFFF" /></a>
