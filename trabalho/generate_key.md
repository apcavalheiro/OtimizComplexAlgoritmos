**Gerar e substituir a chave Fernet no arquivo `aes.py`**

1. Abra um terminal ou prompt de comando e navegue até o diretório onde estão localizados os arquivos `generate_key.py` e `aes.py`.

2. Execute o código em `generate_key.py` para gerar a chave Fernet:

```bash
python generate_key.py
```

Isso imprimirá a chave Fernet no formato base64 no terminal.

3. Copie a chave gerada. Deve ter uma saída semelhante a:

```
MWVqsaTYKCg3sWVQZ22NE8KUxW_6SpOybkN-CRFdaSo=
```

4. Abra o arquivo `aes.py` no seu editor de código.

5. No início do arquivo `aes.py`, substitua a variável `chave` pela chave Fernet que você gerou. Certifique-se de que a chave seja definida no formato base64 e inclua o prefixo `b` para indicar que é uma sequência de bytes.

```python
# Chave Fernet válida (substitua pela chave gerada)
chave = b'MWVqsaTYKCg3sWVQZ22NE8KUxW_6SpOybkN-CRFdaSo='
```

6. Salve o arquivo `aes.py` após substituir a chave.

Agora, a chave Fernet válida está definida no arquivo `aes.py`, e você pode usar essa chave para cifrar e decifrar o texto no programa AES. Certifique-se de manter essa chave em segurança, pois ela é essencial para descriptografar os dados criptografados com ela.