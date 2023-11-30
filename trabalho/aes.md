# AES - Criptografia e Descriptografia

Este é um exemplo simples de implementação do algoritmo AES (Advanced Encryption Standard) em Python. O código permite criptografar e descriptografar mensagens usando o AES.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, instale a biblioteca `cryptography`:

```bash
pip install cryptography
```

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/apcavalheiro/OtimizComplexAlgoritmos.git
cd OtimizComplexAlgoritmos/trabalho/

```

2. Execute o script `aes.py` com argumentos da linha de comando:

```bash
python aes.py criptografar "Mensagem a ser criptografada" "chave-secreta"
```

Substitua `"Mensagem a ser criptografada"` pela mensagem que você deseja criptografar e `"chave-secreta"` pela sua chave secreta.

Para descriptografar:

```bash
python aes.py descriptografar "ciphertext-hexadecimal" "chave-secreta"
```

Substitua `"ciphertext-hexadecimal"` pelo texto criptografado em hexadecimal e `"chave-secreta"` pela mesma chave usada para criptografar.

**Nota:** A chave deve ter 16, 24 ou 32 caracteres.

## Exemplo

### Criptografar

```bash
python aes.py criptografar "Hello, AES!" "mysecretpassword"
```

Saída:

```
Mensagem Criptografada: 2e5a7c46d22c55e74086463d6221b12e
```

### Descriptografar

```bash
python aes.py descriptografar "2e5a7c46d22c55e74086463d6221b12e" "mysecretpassword"
```

Saída:

```
Mensagem Descriptografada: Hello, AES!
```

## Observações

- Este é um exemplo educacional. Em ambientes de produção, use bibliotecas de criptografia robustas e siga as melhores práticas de segurança.
- A saída da mensagem criptografada é fornecida em formato hexadecimal para facilitar a visualização.
- Mantenha suas chaves seguras e não as compartilhe de maneira inadequada.