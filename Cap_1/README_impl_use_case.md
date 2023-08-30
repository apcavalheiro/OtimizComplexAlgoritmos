**Dijkstra's algorithm:**
O algoritmo de Dijkstra é um algoritmo para encontrar os caminhos mais curtos entre nós em um grafo ponderado, que pode representar, por exemplo, redes rodoviárias. Foi concebido pelo cientista da computação Edsger W. Dijkstra.
Link: https://g.co/kgs/vW1FNn


![Dijkstra_Animation](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/36688038/eb8e7e64-e994-482f-beb3-c311489e2e6d)

**Exemplo de Implementação do Algoritmo de Dijkstra em Python**

Neste arquivo, você encontrará um exemplo completo da implementação do algoritmo de Dijkstra em Python. Vamos abordar passo a passo a implementação do algoritmo, além de fornecer uma explicação detalhada para cada parte do código. O algoritmo de Dijkstra é usado para encontrar o caminho mais curto entre dois pontos em um grafo ponderado. 

**1. Importar Bibliotecas:**
Crie um novo arquivo chamado dijkstra_algorithm.py.

Neste arquivo vamos começar importando a biblioteca `heapq` para lidar com a fila de prioridade (heap) e auxiliar na escolha dos nós mais próximos.

```python
import heapq
```

**2. Definir o Grafo:**
Aqui, definimos nosso grafo como um dicionário de adjacências. As chaves representam os nós, e os valores são dicionários que mapeiam os nós vizinhos para as distâncias.

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
```

**3. Implementar o Algoritmo de Dijkstra:**
Função que implementa o algoritmo de Dijkstra.

```python
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    shortest_path = []
    node = end
    while node != start:
        shortest_path.append(node)
        node = min(graph[node], key=lambda x: distances[x] + graph[node][x])
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, distances[end]
```

**4. Utilizando a Função:**
Agora, vamos usar a função `dijkstra` para encontrar o caminho mais curto entre dois pontos.

```python
start_node = 'A'
end_node = 'D'
shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)

print("Caminho mais curto:", shortest_path)
print("Distância:", shortest_distance)
```

**5. Executar o Código:**
Abra seu terminal, navegue até o diretório onde o arquivo dijkstra_algorithm.py está localizado e execute o código com o comando:
python dijkstra_algorithm.py

**Explicação Detalhada da Implementação:**

- Começamos importando a biblioteca `heapq` para gerenciar a fila de prioridade.
- Definimos o grafo como um dicionário de adjacências, onde cada nó é mapeado para seus vizinhos e as distâncias.
- A função `dijkstra` calcula o caminho mais curto e a distância usando a fila de prioridade.
- O loop principal explora os nós, atualiza as distâncias mínimas e escolhe os próximos nós a serem visitados.
- A reconstrução do caminho segue de volta a partir do nó de destino até o ponto de partida.
- Ao final, chamamos a função `dijkstra` com os pontos de partida e destino, imprimindo o caminho mais curto e a distância.

Este arquivo fornece um exemplo prático do algoritmo de Dijkstra em Python, desde a definição do grafo até a utilização da função para encontrar o caminho mais curto. Use esse guia para entender o processo passo a passo e como aplicar o algoritmo em seu próprio código.

**Explicação Do Algoritmo:**

Imagine que você está planejando uma viagem de carro e deseja encontrar o caminho mais curto entre duas cidades em um mapa, levando em conta as distâncias das estradas. O algoritmo de Dijkstra é como ter um assistente que ajuda você a escolher a rota mais rápida.

1. **Preparação:** Suponha que você começa na cidade A e quer chegar à cidade D. Você olha para o mapa e anota as distâncias entre as cidades e as estradas que as conectam.

2. **Exploração Inicial:** Você começa na cidade A e a marca como ponto de partida. Você verifica as estradas que saem da cidade A e anota as distâncias para as cidades vizinhas B e C.

3. **Escolha Inteligente:** Agora, você escolhe a cidade mais próxima, que é a cidade B. Ela está a apenas 1 unidade de distância de A. Você vai até lá e a marca como visitada.

4. **Expansão:** Uma vez na cidade B, você verifica suas estradas para as outras cidades. Você vê que a cidade C está a 2 unidades de distância de B. Você compara essa distância com a que você tinha anotado anteriormente para C (4 unidades) e atualiza, porque agora você encontrou um caminho mais curto.

5. **Escolha Novamente:** Agora, você escolhe a cidade C como a próxima cidade a visitar, já que é a mais próxima. Você vai até C e a marca como visitada.

6. **Continuação:** Na cidade C, você verifica suas estradas e vê que a cidade D é a única opção restante. Você vê que a distância total para D é 3 unidades, que é a menor distância que você encontrou até agora.

7. **Chegando ao Destino:** Você finalmente chegou à cidade D, seguindo o caminho mais curto. Você sabe que escolheu sabiamente as cidades a visitar para chegar mais rápido ao seu destino.

O algoritmo de Dijkstra faz algo semelhante, escolhendo as cidades (ou nós) de maneira inteligente para calcular o caminho mais curto. Ele mantém uma lista das distâncias mais curtas já encontradas e ajusta essa lista à medida que explora novas opções. Isso garante que ele sempre escolha o caminho mais curto possível e é uma maneira eficaz de encontrar rotas rápidas em mapas.
