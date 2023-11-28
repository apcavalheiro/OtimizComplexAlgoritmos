# Cifragem e Decifragem usando AES em Python

Este é um exemplo simples de um script Python que usa a biblioteca `cryptography` para cifrar e decifrar mensagens usando o algoritmo AES.

## Instalação

Antes de executar o script, certifique-se de ter a biblioteca `cryptography` instalada. Você pode instalá-la usando o seguinte comando:

```bash
pip install cryptography
```

## Por que Utilizar uma Biblioteca?

A implementação direta do algoritmo AES pode ser complexa e propensa a erros. O uso de uma biblioteca como `cryptography` oferece várias vantagens:

1. **Segurança**: Bibliotecas amplamente utilizadas, como `cryptography`, são mantidas e atualizadas por especialistas em segurança para garantir robustez e correção.
2. **Desempenho**: Implementações otimizadas em bibliotecas podem oferecer melhor desempenho do que implementações feitas do zero em Python puro.
3. **Padrões e Melhores Práticas**: Bibliotecas seguem padrões e melhores práticas estabelecidos, reduzindo a probabilidade de erros e vulnerabilidades.
4. **Facilidade de Uso**: Bibliotecas fornecem interfaces de alto nível que simplificam a implementação e utilização dos algoritmos criptográficos.

## Execução

Execute o script `aes.py` para cifrar e decifrar usando o algoritmo AES.

```bash
python aes.py
```

O script gerará uma chave AES de 16 bytes (128 bits), cifrará a palavra original "Admin" e, em seguida, decifrará a palavra cifrada, exibindo os resultados na console.

## Estrutura do Projeto

- `aes.py`: Script para cifrar e decifrar usando o algoritmo AES.

## Notas Adicionais

- Certifique-se de manter as chaves seguras, pois elas são necessárias para decifrar os dados cifrados.
- Este é um exemplo educativo e não deve ser usado como implementação de segurança em produção.