def cifra_cesar(texto, chave, modo='cifrar'):
    """
    Cifra ou decifra o texto usando o algoritmo de Cifra de César.

    Parameters:
    texto (str): O texto a ser cifrado ou decifrado.
    chave (int): A chave de cifra, determina o número de posições a serem deslocadas.
    modo (str): 'cifrar' para cifrar o texto, 'decifrar' para decifrar o texto.

    Returns:
    str: O texto cifrado ou decifrado.
    """
    resultado = ""

    # Determina a operação com base no modo
    if modo == 'decifrar':
        chave = -chave  # Inverte a chave para decifrar

    for char in texto:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina se o caractere é maiúsculo ou minúsculo
            is_upper = char.isupper()
            
            # Converte o caractere para minúsculo para facilitar a cifragem
            char = char.lower()

            # Aplica a cifra de César
            codigo = ord(char) - ord('a')
            novo_codigo = (codigo + chave) % 26
            novo_char = chr(novo_codigo + ord('a'))

            # Converte de volta para maiúsculo, se necessário
            if is_upper:
                novo_char = novo_char.upper()

            resultado += novo_char
        else:
            # Se não for uma letra, mantém o caractere inalterado
            resultado += char

    return resultado

# Palavra a ser cifrada
palavra_original = "Admin"

# Chave de cifra (por exemplo, 3)
chave = 3

# Cifra a palavra
palavra_cifrada = cifra_cesar(palavra_original, chave, modo='cifrar')

# Exibe os resultados
print(f"Palavra Original: {palavra_original}")
print(f"Chave de Cifra: {chave}")
print(f"Palavra Cifrada: {palavra_cifrada}")

# Decifra a palavra
palavra_decifrada = cifra_cesar(palavra_cifrada, chave, modo='decifrar')

# Exibe os resultados da decifragem
print(f"Palavra Decifrada: {palavra_decifrada}")
