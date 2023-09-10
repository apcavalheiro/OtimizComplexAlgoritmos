**Resumo do capítulo 3 - Estruturas de dados**

As estruturas de dados podem ser classificadas como contíguas ou vinculadas, dependendo se são baseadas em arrays ou ponteiros:

• Estruturas alocadas contiguamente são compostas de blocos únicos de memória e incluem arrays, matrizes, heaps e tabelas hash.
• Estruturas de dados vinculadas são compostas de pedaços distintos de memória unidos por ponteiros e incluem listas, árvores e listas de adjacências de gráficos.

**Matrizes**

Matrizes são estruturas de registros de dados de tamanho fixo, de modo que cada elemento possa ser localizado de forma eficiente por seu índice ou endereço (equivalente).

• Acesso em tempo constante dado o índice – Como o índice de cada elemento é mapeado diretamente para um endereço de memória específico, podemos acessar itens de dados arbitrários instantaneamente, desde que conheçamos o índice.
• Eficiência de espaço – Os arrays consistem exclusivamente em dados, portanto nenhum espaço é desperdiçado com links ou outras informações de formatação. Além disso, as informações de fim de registro não são necessárias porque os arrays são construídos a partir de registros de tamanho fixo.
• Localidade de memória – Uma linguagem de programação comum envolve a iteração através de todos os elementos de uma estrutura de dados. Matrizes são boas para isso porque exibem excelente localidade de memória. A continuidade física entre acessos sucessivos aos dados ajuda a explorar a memória cache de alta velocidade nas arquiteturas de computadores modernas.
Ponteiros e estruturas vinculadas
Ponteiros são as conexões que mantêm unidas as peças das estruturas vinculadas. Os ponteiros representam o endereço de um local na memória.
A lista é a estrutura vinculada mais simples. As três operações básicas suportadas pelas listas são pesquisa, inserção e exclusão. Nas listas duplamente vinculadas, cada nó aponta tanto para seu antecessor quanto para seu elemento sucessor.

```
   lista *lista_pesquisa(lista *l, tipo_item x) {
           if (l == NULO) return(NULO);
           if (l->item == x) return(l);
           return(lista_pesquisa(l->próximo, x));
}
   ```

A inserção em uma lista vinculada individualmente é um bom exercício de manipulação de ponteiros, conforme mostrado abaixo.

```
void insert_list(lista **l, item_type x) {
lista *p;                                                       /* ponteiro temporário */
p = malloc(tamanho(lista)); p->item = x; p-
>próximo = *l; *eu
= p;
}
```
A exclusão de uma lista vinculada é um pouco mais complicada. Primeiro, devemos encontrar um ponteiro para o antecessor do item a ser excluído.

```
lista *lista_predecessor(lista *l, item_type x) {
if ((l == NULO) || (l->próximo == NULO)) {
//predecessor procurado na lista nula return(NULL);
}
if ((l->próximo)->item == x) return(l);
return(lista_predecessor(l->próximo, x));
}
```
```
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
• Com registros grandes, mover ponteiros é mais fácil e rápido do que mover os próprios itens.
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

```
typedef struct tree {item_type item;                           /* item de dados */ /
árvore de estrutura *pai;                                             * ponteiro para o pai */ /*
árvore de estrutura *esquerda;                                    ponteiro para o filho esquerdo */ /*
árvore de estrutura *direita;                                        ponteiro para o filho direito */
} árvore;
```

**Procurando em uma árvore**

A rotulagem da árvore de pesquisa binária identifica exclusivamente onde cada chave está localizada. Comece pela raiz. A menos que contenha a chave de consulta x, prossiga para a esquerda ou para a direita, dependendo se x ocorre antes ou depois da chave raiz. Este algoritmo funciona porque as subárvores esquerda e direita de uma árvore de pesquisa binária são árvores de pesquisa binária. Esta estrutura recursiva produz o algoritmo de pesquisa recursiva abaixo:

```
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

```
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

```
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



