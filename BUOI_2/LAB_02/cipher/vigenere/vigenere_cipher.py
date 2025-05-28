class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()  # Lưu trữ khóa, thường viết hoa để nhất quán

    def encrypt(self, plaintext):
        ciphertext = ""
        key_len = len(self.key)
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[key_index % key_len]) - ord('A')
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
                ciphertext += shifted_char
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        key_len = len(self.key)
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[key_index % key_len]) - ord('A')
                shifted_char = chr((ord(char) - start - shift + 26) % 26 + start)
                plaintext += shifted_char
                key_index += 1
            else:
                plaintext += char
        return plaintext