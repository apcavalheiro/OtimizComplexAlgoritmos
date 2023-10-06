import sys

def find_smallest_snippet(document, word_positions):
    # Inicialize uma lista para armazenar todas as posições das palavras
    positions = []

    # Crie uma lista de todas as posições das palavras no documento
    for word in word_positions:
        positions.extend(word_positions[word])

    # Ordene as posições para que possamos procurar um snippet mínimo
    positions.sort()

    # Inicialize um dicionário para rastrear quantas vezes cada palavra apareceu
    word_count = {word: 0 for word in word_positions}
    
    # Inicialize as variáveis para acompanhar o menor snippet encontrado
    min_snippet_length = sys.maxsize
    min_snippet_start = 0
    snippet_start = 0

    # Percorra as posições das palavras no documento
    for position in positions:
        word = document[position]
        
        # Verifique se a palavra é uma das palavras-chave
        if word in word_count:
            word_count[word] += 1

            # Quando todas as palavras-chave forem encontradas
            while all(word_count[word] > 0 for word in word_count):
                # Atualize o snippet mínimo, se necessário
                if position - snippet_start + 1 < min_snippet_length:
                    min_snippet_length = position - snippet_start + 1
                    min_snippet_start = snippet_start

                # Mova o snippet para a direita, removendo a palavra mais à esquerda
                left_word = document[snippet_start]
                word_count[left_word] -= 1
                snippet_start += 1

    # Retorne o snippet mínimo encontrado
    min_snippet_start = int(min_snippet_start)
    min_snippet_length = int(min_snippet_length)
    return document[min_snippet_start:min_snippet_start + min_snippet_length]


# Função para ler um arquivo de texto
def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().split()  # Divide o texto em palavras
    except FileNotFoundError:
        print(f"O arquivo '{filename}' não foi encontrado.")
        return []

# Nome do arquivo de texto que você deseja ler
filename = 'arquivo_de_texto.txt'  # Substitua pelo nome do seu arquivo

# Palavras-chave e suas posições (exemplo)
word_positions = {"word1": [0, 7], "word2": [1, 5], "word3": [2, 6]}

# Ler o conteúdo do arquivo de texto
document = read_text_file(filename)

# Verifique se o arquivo foi lido com sucesso
if document:
    result = find_smallest_snippet(document, word_positions)
    print("Menor Snippet:", " ".join(result))
