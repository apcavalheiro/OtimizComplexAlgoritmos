from cryptography.fernet import Fernet

def fernet_cifrar(texto, chave):
    cipher_suite = Fernet(chave)
    ciphertext = cipher_suite.encrypt(texto)
    return ciphertext

def fernet_decifrar(texto_cifrado, chave):
    cipher_suite = Fernet(chave)
    texto_decifrado = cipher_suite.decrypt(texto_cifrado)
    return texto_decifrado

# Palavra a ser cifrada
palavra_original = b"Admin"

# Gere uma chave Fernet
chave = Fernet.generate_key()

# Cifra a palavra
palavra_cifrada = fernet_cifrar(palavra_original, chave)

# Exibe os resultados da cifragem
print(f"Palavra Original: {palavra_original}")
print(f"Chave de Cifra: {chave}")
print(f"Palavra Cifrada: {palavra_cifrada}")

# Decifra a palavra
palavra_decifrada = fernet_decifrar(palavra_cifrada, chave)

# Exibe os resultados da decifragem
print(f"Palavra Decifrada (Bytes): {palavra_decifrada}")
print(f"Palavra Decifrada (UTF-8): {palavra_decifrada.decode('utf-8')}")
