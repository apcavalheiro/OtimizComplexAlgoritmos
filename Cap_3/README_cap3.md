**Resumo do capítulo 3 - Estruturas de dados**

As estruturas de dados podem ser classificadas como contíguas ou vinculadas, dependendo se são baseadas em arrays ou ponteiros:

• Estruturas alocadas contiguamente são compostas de blocos únicos de memória e incluem arrays, matrizes, heaps e tabelas hash.

• Estruturas de dados vinculadas são compostas de pedaços distintos de memória unidos por ponteiros e incluem listas, árvores e listas de adjacências de gráficos.

**Matrizes**

Matrizes são estruturas de registros de dados de tamanho fixo, de modo que cada elemento possa ser localizado de forma eficiente por seu índice ou endereço (equivalente).

• Acesso em tempo constante dado o índice – Como o índice de cada elemento é mapeado diretamente para um endereço de memória específico, podemos acessar itens de dados arbitrários instantaneamente, desde que conheçamos o índice.

• Eficiência de espaço – Os arrays consistem exclusivamente em dados, portanto nenhum espaço é desperdiçado com links ou outras informações de formatação. Além disso, as informações de fim de registro não são necessárias porque os arrays são construídos a partir de registros de tamanho fixo.

• Localidade de memória – Uma linguagem de programação comum envolve a iteração através de todos os elementos de uma estrutura de dados. Matrizes são boas para isso porque exibem excelente localidade de memória. A continuidade física entre acessos sucessivos aos dados ajuda a explorar a memória cache de alta velocidade nas arquiteturas de computadores modernas.

**Ponteiros e estruturas vinculadas**

Ponteiros são as conexões que mantêm unidas as peças das estruturas vinculadas. Os ponteiros representam o endereço de um local na memória.
A lista é a estrutura vinculada mais simples. As três operações básicas suportadas pelas listas são pesquisa, inserção e exclusão. Nas listas duplamente vinculadas, cada nó aponta tanto para seu antecessor quanto para seu elemento sucessor.

```python
lista *lista_pesquisa(lista *l, tipo_item x) {
                   if (l == NULO) return(NULO);
                   if (l->item == x) return(l);
                   return(lista_pesquisa(l->próximo, x));
}
   ```

A inserção em uma lista vinculada individualmente é um bom exercício de manipulação de ponteiros, conforme mostrado abaixo.

```python
void insert_list(lista **l, item_type x) {
lista *p;                                                       /* ponteiro temporário */
p = malloc(tamanho(lista)); p->item = x; p-
>próximo = *l; *eu
= p;
}
```
A exclusão de uma lista vinculada é um pouco mais complicada. Primeiro, devemos encontrar um ponteiro para o antecessor do item a ser excluído.

```python
lista *lista_predecessor(lista *l, item_type x) {
if ((l == NULO) || (l->próximo == NULO)) {
//predecessor procurado na lista nula return(NULL);
}
if ((l->próximo)->item == x) return(l);
return(lista_predecessor(l->próximo, x));
}
```

```python
delete_list(lista **l, item_type x) {
            *p; /*                                       /* ponteiro de item */ lista
                     ponteiro antecessor */ list *pred; lista *lista_pesquisa(), *lista_predecessora();
p = lista_pesquisa(*l,x); if (p !=
NULL) { pred =
               lista_predecessora(*l,x); if (pred == NULL) /
               * separar da lista */ *l = p->next;
               pred->próximo = p->próximo;
grátis(p);                                              /* memória livre usada pelo nó */
}
}
```

As vantagens relativas das listas vinculadas sobre matrizes estáticas incluem:

• Overflow em estruturas vinculadas nunca pode ocorrer a menos que a memória esteja realmente completo.

• Inserções e exclusões são mais simples do que em listas contíguas (array).

Com registros grandes, mover ponteiros é mais fácil e rápido do que mover os próprios itens.
Enquanto as vantagens relativas dos arrays incluem:

• Estruturas vinculadas requerem espaço extra para armazenar campos de ponteiro.

• Listas vinculadas não permitem acesso aleatório eficiente aos itens.

• Os arrays permitem melhor localização de memória e desempenho de cache do que saltos aleatórios de ponteiro.

**Pilhas e Filas**

Usamos o termo contêiner para denotar uma estrutura de dados que permite o armazenamento e a recuperação de itens de dados independentemente do conteúdo.

• Pilhas – Suporta recuperação por ordem LIFO (último a entrar, primeiro a sair).

• Filas – Suporta recuperação na ordem FIFO (primeiro a entrar, primeiro a sair).

**Dicionários**

O tipo de dados dicionário permite acesso a itens de dados por conteúdo. Você coloca um item em um dicionário para poder encontrá-lo quando precisar.
As principais operações de suporte de dicionário são:

• Search(D,k) – Dada uma chave de pesquisa k, retorna um ponteiro para o elemento em dicionário D cujo valor chave é k, se existir.

• Insert(D,x) – Dado um item de dados x, adicione-o ao conjunto no dicionário D.

• Delete(D,x) – Dado um ponteiro para um determinado item de dados x no dicionário D, remova-o de D.

**Árvores de Pesquisa Binária**

A pesquisa binária requer acesso rápido a dois elementos – especificamente os elementos medianos acima e abaixo de um determinado nó. Para combinar essas ideias, precisamos de uma “lista vinculada” com dois ponteiros por nó. Esta é a ideia básica por trás das árvores de busca binária.

**Implementando Árvores de Pesquisa Binária**

As operações básicas suportadas por árvores binárias são busca, travessia, inserção e exclusão.

```python
typedef struct tree {item_type item;                           /* item de dados */ /
árvore de estrutura *pai;                                             * ponteiro para o pai */ /*
árvore de estrutura *esquerda;                                    ponteiro para o filho esquerdo */ /*
árvore de estrutura *direita;                                        ponteiro para o filho direito */
} árvore;
```

**Procurando em uma árvore**

A rotulagem da árvore de pesquisa binária identifica exclusivamente onde cada chave está localizada. Comece pela raiz. A menos que contenha a chave de consulta x, prossiga para a esquerda ou para a direita, dependendo se x ocorre antes ou depois da chave raiz. Este algoritmo funciona porque as subárvores esquerda e direita de uma árvore de pesquisa binária são árvores de pesquisa binária. Esta estrutura recursiva produz o algoritmo de pesquisa recursiva abaixo:

```python
árvore *árvore_pesquisa(árvore *l, tipo_item x) {
if (l == NULO) return(NULO);
if (l->item == x) return(l);
if (x item) 
              return(search_tree(l->esquerda, x) );
else
             return( search_tree(l->direita, x) );
}
```

**Encontrando elementos mínimos e máximos em uma árvore**

A implementação da operação encontrar o mínimo requer saber onde está o elemento mínimo na árvore. Da mesma forma, o elemento máximo deve ser o descendente mais à direita da raiz.

```python
árvore *encontrar_mínimo(árvore *t) {
árvore *min;                                                            /* ponteiro para o mínimo */
if (t == NULO) return(NULO);
min = t; 
while (min->esquerda!=NULO)
                       min = min->esquerda;
return(min);
}
```

**Travessia em uma árvore**

Visitar todos os nós em uma árvore binária enraizada prova ser um componente importante de muitos algoritmos. Por definição, todas as chaves menores que a raiz devem estar na subárvore esquerda da raiz e todas as chaves maiores que a raiz na subárvore direita. Assim, visitar os nós recursivamente de acordo com tal política produz uma travessia ordenada da árvore de busca:

```python
void traverse_tree(árvore *l) {
                         if (l != NULL)
                                              { traverse_tree(l->esquerda); 
                                                 item_processo(l->item); 
                                                 traverse_tree(l->direita);
                       }
}
```

**Inserção em uma árvore**

Existe apenas um lugar para inserir um item x em uma árvore binária de busca T onde sabemos que podemos encontrá-lo novamente. Devemos substituir o ponteiro NULL encontrado em T após uma consulta malsucedida pela chave k.

**Exclusão de uma árvore**

A exclusão é um pouco mais complicada do que a inserção, porque remover um nó significa vincular adequadamente suas duas subárvores descendentes de volta à árvore em algum outro lugar.

**Quão boas são as árvores de pesquisa binária?**

Quando implementadas usando árvores de busca binária, todas as três operações do dicionário levam tempo O(h), onde h é a altura da árvore. A menor altura que podemos esperar ocorre quando a árvore está perfeitamente equilibrada, onde h = log n. Isso é muito bom, mas a árvore deve estar perfeitamente equilibrada.
Este argumento é um exemplo importante do poder da randomização. Muitas vezes podemos desenvolver algoritmos simples que oferecem bom desempenho com alta probabilidade. Veremos que uma ideia semelhante está subjacente ao algoritmo de classificação mais rápido conhecido, quicksort.

**Árvores de pesquisa balanceadas**

Árvores de busca aleatória geralmente são boas. Mas se não tivermos sorte com a nossa ordem de inserção, podemos acabar com uma árvore de altura linear no pior dos casos. Este pior caso está fora do nosso controle direto, uma vez que devemos construir a árvore em resposta às solicitações feitas pelo nosso usuário potencialmente desagradável.
Do ponto de vista do projeto de algoritmos, é importante saber que essas árvores existem e que podem ser usadas como caixas pretas para fornecer uma implementação eficiente de dicionário. Ao calcular os custos das operações de dicionário para análise de algoritmos, podemos assumir que as complexidades do pior caso das árvores binárias balanceadas são uma medida justa.

**Resumo do capítulo 3 continuação**

**Filas Prioritárias**

Filas prioritárias são estruturas de dados que permitem processar itens em uma ordem específica, baseada em suas chaves ou prioridades. Filas prioritárias suportam três operações principais: inserir, encontrar-mínimo (ou máximo) e excluir-mínimo (ou máximo). Filas prioritárias podem ser implementadas de diferentes formas, como matrizes não ordenadas, matrizes ordenadas ou árvores de busca binária balanceadas. Filas prioritárias podem ser usadas para resolver vários problemas algorítmicos, como classificação, agendamento e modelagem de processos naturais. Filas prioritárias são frequentemente usadas em algoritmos de grafos, como Dijkstra e Prim, para encontrar o caminho mais curto e a árvore geradora mínima, respectivamente. A operação de inserção em uma fila prioritária tem complexidade de tempo O(1) para uma matriz não ordenada e O(log n) para uma árvore de busca binária balanceada. A operação de encontrar-mínimo tem complexidade de tempo O(n) para uma matriz não ordenada e O(1) para uma árvore de busca binária balanceada. A operação de excluir-mínimo tem complexidade de tempo O(n) para uma matriz não ordenada e O(log n) para uma árvore de busca binária balanceada. Portanto, a escolha da implementação da fila prioritária depende das necessidades específicas do problema que está sendo resolvido. Por exemplo, se as operações de inserção são mais frequentes do que as operações de encontrar-mínimo e excluir-mínimo, uma matriz não ordenada pode ser a escolha ideal. Por outro lado, se as operações de encontrar-mínimo e excluir-mínimo são mais frequentes, uma árvore de busca binária balanceada pode ser mais eficiente.

**História de Guerra: Removendo Triangulações**

Este tópico descreve um problema de particionar uma malha triangular em tiras de triângulos adjacentes para reduzir o custo de renderização em computação gráfica. O tópico apresenta uma heurística gananciosa que usa uma fila de prioridade para selecionar a tira mais longa a ser removida a cada passo. O tópico mostra que a heurística gananciosa melhora significativamente a qualidade da solução em relação à heurística ingênua e destaca a importância de escolher a estrutura de dados correta para o problema.

**Hashing e Strings**

Este tópico explica o conceito de hashing, que é uma técnica para representar um objeto grande por um número inteiro único.
O tópico discute como escolher uma boa função hash e como lidar com colisões usando encadeamento ou endereçamento aberto.
O tópico também apresenta algumas aplicações de hashing, como pesquisa de substring, detecção de duplicatas e verificação de integridade.

**Resolução de Colisões**

Este sub-tópico detalha as duas abordagens principais para resolver colisões em tabelas hash: encadeamento e endereçamento aberto. O sub-tópico compara as vantagens e desvantagens de cada abordagem em termos de complexidade de tempo, espaço e implementação.

**Correspondência eficiente de strings via hash**

Este sub-tópico apresenta um algoritmo aleatório para correspondência de strings chamado algoritmo Rabin-Karp, que usa hashing para acelerar a pesquisa de substrings. O sub-tópico explica como o algoritmo calcula os valores de hash das janelas sobrepostas do texto em tempo constante usando uma função hash baseada em potências de um número primo. O sub-tópico analisa o tempo esperado e o pior caso do algoritmo e discute as probabilidades de falsas colisões.

**Detecção de duplicatas via hash**

Este sub-tópico ilustra algumas aplicações práticas de hashing para detectar duplicatas em documentos, leilões ou sequências de DNA. O sub-tópico mostra como usar códigos hash para verificar se um documento é diferente de todos os outros em um grande corpus, se parte dele foi plagiada ou se ele foi alterado. O sub-tópico também menciona o conceito de hashing criptográfico, que é uma forma mais segura e robusta de hashing.

**Estruturas de Dados Especializadas**

Este tópico introduz algumas estruturas de dados especializadas para representar tipos mais estruturados ou especializados de objetos, como strings, dados geométricos, gráficos e conjuntos. O tópico fornece alguns exemplos dessas estruturas de dados, como árvores/matrizes de sufixo, kd-árvores, matrizes/listas de adjacência e vetores de bits. O tópico também indica onde encontrar mais detalhes sobre essas estruturas no catálogo.

**História de Guerra: Amarre-os**

Este tópico descreve um problema de biologia computacional relacionado ao sequenciamento por hibridização (SBH), que é uma técnica proposta para sequenciar DNA usando sondas que detectam substrings do DNA alvo. O tópico apresenta um algoritmo para identificar todas as strings possíveis de comprimento 2k que são substrings do DNA alvo, dado o conjunto de todas as substrings de comprimento k do DNA alvo. O tópico mostra como usar uma estrutura de dados combinando uma fila prioritária e um dicionário para acelerar o algoritmo e relata os desafios e resultados da implementação.

