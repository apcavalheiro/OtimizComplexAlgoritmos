from cryptography.fernet import Fernet

# Gera uma chave Fernet válida
chave = Fernet.generate_key()

# Imprime a chave
print(chave)

