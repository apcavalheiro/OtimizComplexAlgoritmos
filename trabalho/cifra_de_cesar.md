# Cifra de César em Python

Este é um simples implementação em Python da Cifra de César, um algoritmo de criptografia clássico.

## Funcionalidades

- Cifrar uma mensagem usando a Cifra de César.
- Decifrar uma mensagem usando a Cifra de César.

## Como usar

1. Navegue até o diretório do projeto:

    ```bash
    cd cifra-de-cesar-python
    ```

2. Execute o script Python:

    ```bash
    python cifra_cesar.py
    ```

3. Siga as instruções para inserir a palavra a ser cifrada, a chave de cifra e escolher entre cifrar ou decifrar.

# Cifra de César

Este é um simples exemplo de uma função Python que implementa a Cifra de César para cifrar e decifrar mensagens.

## Função `cifra_cesar`

A função `cifra_cesar` realiza a cifragem ou decifragem de um texto usando o algoritmo de Cifra de César.

### Parâmetros:

- `texto (str)`: O texto a ser cifrado ou decifrado.
- `chave (int)`: A chave de cifra, determinando o número de posições a serem deslocadas.
- `modo (str)`: 'cifrar' para cifrar o texto, 'decifrar' para decifrar o texto.

### Retorno:

- `str`: O texto cifrado ou decifrado.

## Exemplo de Uso

```python
# Importa a função
from cifra_cesar import cifra_cesar

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
```

## Notas Adicionais

- A Cifra de César é um método de criptografia simples que desloca as letras do alfabeto por um número fixo de posições.
- Este é um exemplo educativo e não deve ser usado como implementação de segurança em produção.
