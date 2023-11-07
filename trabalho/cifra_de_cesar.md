### Algoritmo 1: Cifra de César

#### Descrição:
O Algoritmo 1 é baseado na Cifra de César, uma técnica de criptografia de substituição simples que desloca cada letra do texto original por um número fixo de posições no alfabeto. Este é um exemplo básico e inseguro de criptografia, usado apenas para fins educacionais.

#### Explicação:
- `cifra_de_cesar`: Esta função recebe um texto e uma chave como entrada e retorna o texto cifrado usando a Cifra de César. A cifra funciona deslocando cada letra do texto pelo valor da chave. Se o caractere não for uma letra, ele é deixado inalterado.

- A interface gráfica é criada usando a biblioteca tkinter. Ela inclui campos de entrada para o texto original e a chave, um botão para cifrar o texto e um rótulo para exibir o resultado.

#### Execução:

1. Abra o prompt de comando e navegue até a pasta onde você salvou o arquivo `cifra_de_cesar.py`.

2. Execute o script com o comando:

```
python cifra_de_cesar.py
```

3. A interface gráfica será aberta. Você verá os seguintes campos:

   - "Texto Original": Digite o texto que deseja cifrar. Por exemplo, digite "HELLO" (sem as aspas).

   - "Chave (deslocamento)": Insira um número inteiro que servirá como chave de deslocamento. Por exemplo, insira "3".

4. Clique no botão "Cifrar" para executar o algoritmo.

5. O campo "Texto Cifrado" mostrará o resultado da cifração. No exemplo acima, o resultado seria "KHOOR" como saída, pois cada letra foi deslocada 3 posições no alfabeto.

