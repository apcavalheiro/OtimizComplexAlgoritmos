
### Algoritmo 2: AES (Advanced Encryption Standard)

#### Descrição:
O Algoritmo 2 utiliza o Advanced Encryption Standard (AES) para criptografar dados de forma segura. O AES é um algoritmo de criptografia simétrica amplamente adotado e considerado seguro para proteção de dados confidenciais.

#### Explicação:
- `gerar_chave_aes`: Esta função gera uma chave AES usando o módulo Fernet da biblioteca `cryptography`. A chave é uma sequência aleatória que será usada para criptografar e descriptografar o texto.

- `cifrar_aes`: Esta função recebe um texto e uma chave AES como entrada e retorna o texto cifrado usando o AES. A biblioteca Fernet facilita a cifragem e decifragem dos dados.

- A interface gráfica para o AES é semelhante à do Algoritmo 1, mas inclui a geração de uma chave AES e usa essa chave para cifrar o texto.

#### Execução:

Certifique-se de ter a biblioteca `cryptography` instalada. Se você ainda não instalou, você pode instalar via `pip`:

Abra o terminal e execute o comando:
```bash
pip install cryptography
```

Isso instalará a biblioteca `cryptography` necessária para o Algoritmo 2.

### Execução do Algoritmo 2: AES (Advanced Encryption Standard)

1. Abra o terminal ou prompt de comando.

2. Navegue até a pasta onde você salvou o arquivo `aes.py` utilizando o comando `cd`.

3. Execute o script com o seguinte comando:
   
```bash
python aes.py
```

Isso iniciará a interface gráfica do algoritmo que utiliza o AES para criptografar texto.

### Utilizando a interface gráfica:

Ao executar o script `aes.py`, uma interface gráfica será aberta.

- Você verá campos para inserir o texto que deseja cifrar e a chave de criptografia.
- Insira o texto e a chave nos campos correspondentes.
- Em seguida, clique no botão apropriado para realizar a criptografia.
- A interface exibirá o texto cifrado resultante na própria interface.

O AES é um algoritmo de criptografia simétrica, amplamente utilizado para criptografar e descriptografar dados. A interface gráfica permitirá que você experimente a funcionalidade de criptografia oferecida por esse algoritmo.
