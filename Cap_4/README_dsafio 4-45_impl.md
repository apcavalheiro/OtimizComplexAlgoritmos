**Desafio 4-45:** Neste desafio, você precisa encontrar o menor trecho (snippet) de um documento que contenha três palavras-chave, dadas as posições das palavras no documento. Este problema é um ótimo exercício para trabalhar com manipulação de strings, algoritmos de busca e estruturas de dados

O código em snippet_finder.py tem como funcionalidade resolver o desafio de encontrar o menor snippet (trecho) em um documento de texto que contenha todas as palavras-chave especificadas, considerando as posições das palavras no documento.

Aqui está uma explicação passo a passo do código:

1. A função `find_smallest_snippet(document, word_positions)` recebe dois argumentos: `document` (o conteúdo do documento de texto) e `word_positions` (um dicionário que mapeia palavras-chave para suas posições no documento).

2. A função começa inicializando uma lista vazia chamada `positions`, que será usada para armazenar todas as posições das palavras-chave no documento.

3. Em seguida, ela cria uma lista de todas as posições das palavras no documento. Ela faz isso percorrendo todas as palavras-chave especificadas em `word_positions` e estendendo a lista `positions` com as posições de cada palavra-chave no documento. Isso cria uma lista de todas as posições das palavras-chave, que é então ordenada.

4. Um dicionário chamado `word_count` é inicializado para rastrear quantas vezes cada palavra-chave foi encontrada no snippet atual.

5. As variáveis `min_snippet_length` e `min_snippet_start` são inicializadas com valores "infinito" e 0, respectivamente, para acompanhar o menor snippet encontrado.

6. Em seguida, o código percorre as posições das palavras no documento. Para cada posição, verifica se a palavra naquela posição é uma das palavras-chave.

7. Quando uma palavra-chave é encontrada, seu contador é incrementado e o código entra em um loop `while` para verificar se todas as palavras-chave foram encontradas dentro do snippet atual.

8. Se todas as palavras-chave forem encontradas, o código calcula o comprimento do snippet atual e verifica se é menor do que o menor snippet encontrado até agora. Se for, atualiza as variáveis `min_snippet_length` e `min_snippet_start` com os valores do snippet atual.

9. Em seguida, o snippet é movido para a direita, removendo a palavra mais à esquerda e decrementando seu contador no dicionário `word_count`.

10. O código continua a percorrer as posições das palavras no documento até encontrar o menor snippet que contenha todas as palavras-chave.

11. Finalmente, a função retorna o menor snippet encontrado no formato de uma lista de palavras.

O desafio que este código resolve é encontrar o menor trecho no documento de texto que contenha todas as palavras-chave especificadas e fornecidas em `word_positions`. Isso é útil em casos em que você deseja destacar ou extrair uma parte específica de um texto que contém todas as palavras-chave desejadas.