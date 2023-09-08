**Resumo capítulo 2: Algorithm Analysis**

Os algoritmos são a parte mais importante e durável da ciência da computação porque podem ser estudados de maneira independente da linguagem e da máquina. 
Isso significa que precisamos de técnicas que nos permitam comparar a eficiência dos algoritmos sem implementá-los. Nossas duas ferramentas mais importantes são (1) o modelo de computação RAM e (2) a análise assintótica da complexidade do pior caso.
A avaliação do desempenho algorítmico faz uso da notação “big Oh” que se mostra essencial para comparar algoritmos e projetar outros mais eficientes.
O projeto de algoritmo independente de máquina depende de um computador hipotético chamado Random Access Machine ou RAM. Sob este modelo de computação, somos confrontados com um computador onde:
	Cada operação simples (+, *, –, =, if, call) leva exatamente um passo de tempo.
	Loops e sub-rotinas não são considerados operações simples. Em vez disso, eles são a composição de muitas operações de uma única etapa. O tempo que leva para percorrer um loop ou executar um subprograma depende do número de iterações do loop ou da natureza específica do subprograma.
	Cada acesso à memória leva exatamente um passo de tempo. Além disso, temos tanta memória quanto precisamos. O modelo de RAM não percebe se um item está no cache ou no disco.
        No modelo RAM, medimos o tempo de execução contando o número de etapas que um algoritmo executa em uma determinada instância do problema.
Afinal, multiplicar dois números leva mais tempo do que adicionar dois números na maioria dos processadores, o que viola a primeira suposição do modelo.
Usando o modelo de computação RAM, podemos contar quantos passos nosso algoritmo dá em qualquer instância de entrada ao executá-lo.
Podemos definir três funções interessantes sobre o gráfico desses pontos:
	A complexidade do pior caso do algoritmo é a função definida pelo número máximo de passos dados em qualquer instância de tamanho n. Isso representa a curva que passa pelo ponto mais alto em cada coluna.
	A complexidade de melhor caso do algoritmo é a função definida pelo número mínimo de passos dados em qualquer instância de tamanho n. Isso representa a curva que passa pelo ponto mais baixo de cada coluna.
	A complexidade de caso médio do algoritmo, que é a função definida pelo número médio de etapas em todas as instâncias de tamanho n.
As complexidades de tempo de melhor, pior e caso médio para qualquer algoritmo são funções numéricas sobre o tamanho de possíveis instâncias do problema. No entanto, é muito difícil trabalhar precisamente com essas funções, pois elas tendem a:	Ter muitos solavancos – Um algoritmo como busca binária normalmente roda um pouco mais rápido para arrays de tamanho exatamente n = 2^k-1 (onde k é um inteiro), porque as partições de array funcionam bem. 
Esse detalhe não é particularmente significativo, mas nos adverte que a função de complexidade de tempo exata para qualquer algoritmo pode ser muito complicada, com pequenos saltos para cima e para baixo.
	Exigir muitos detalhes para especificar com precisão – Contar o número exato de instruções de RAM executadas no pior caso exige que o algoritmo seja especificado com detalhes de um programa de computador completo. 
Além disso, a resposta precisa depender de detalhes de codificação desinteressantes (por exemplo, ele usou uma instrução case ou ifs aninhados?). Realizar uma análise precisa do pior caso, como

        T(n) = 12754n² + 4353n + 834〖lg〗_2 n+13546

seria claramente um trabalho muito difícil, mas nos fornece poucas informações extras do que a observação de que “o tempo cresce quadraticamente com n”.
        As definições formais associadas à notação Big O são as seguintes:

	f(n) = O(g(n)) significa que c ⋅ g(n) é um limite superior em f(n). 
Assim, existe alguma constante c tal que f(n) é sempre ≤ c ⋅ g(n), para n suficientemente grande (ou seja, n ≥ n^0 para alguma constante n^0).	f(n) = Ω(g(n)) significa que c ⋅ g(n) é um limite inferior em f(n). Assim existe alguma constante c tal que f(n) é sempre ≥ c ⋅ g(n), para todo n ≥ n^0.
	f(n) = Θ(g(n)) significa que c_1  ⋅ g(n) é um limite superior em f(n) e c_2 · g(n) é um limite inferior em f(n), para todo n ≥ n^0. 
Assim existem constantes c_1   e c_2 tais que f(n) ≤ c_1  ⋅ g(n) e  f(n) ≤ c_2  ⋅ g(n). Isso significa que g(n) fornece um bom e apertado limite em f(n).
        A notação Big O agrupa funções em um conjunto de classes, de modo que todas as funções em uma determinada classe sejam equivalentes em relação ao Big O. 
	A boa notícia é que apenas algumas classes de função tendem a ocorrer no decorrer da análise de algoritmos básicos. Eles são suficientes para cobrir quase todos os algoritmos que discutiremos neste texto e estão listados em ordem crescente de dominância:	
	Funções constantes, f(n)=1 – Tais funções podem medir o custo de adicionar dois números, imprimir “The Star Spangled Banner”, ou o crescimento realizado por funções como f(n) = min(n,100). 
No quadro geral, não há dependência do parâmetro n.
	Funções logarítmicas, f(n)=log n – A complexidade de tempo logarítmica aparece em algoritmos como busca binária. 
Tais funções crescem muito lentamente à medida que n aumenta, mas mais rápido do que a função constante (que está parada, afinal). 
	Funções lineares, f(n)=n – Essas funções medem o custo de olhar para cada item uma vez (ou duas, ou dez vezes) em uma matriz de n elementos, digamos, para identificar o maior item, o menor item ou calcular o valor médio.
	Funções super lineares, f(n)=n lg n – Esta importante classe de funções surge em algoritmos como Quicksort e Mergesort. 
Eles crescem um pouco mais rápido do que linear, apenas o suficiente para ser uma classe de dominância diferente.
	Funções quadráticas, f(n)=n² – Tais funções medem o custo de observar a maioria ou todos os pares de itens em um universo de n elementos. 
Isso surge em algoritmos como ordenação por inserção e ordenação por seleção.
	Funções cúbicas, f(n)=n³ – Tais funções enumeram-se através de todas as triplas de itens em um universo de n elementos. 
	Funções exponenciais, f(n) = c^n para uma dada constante c > 1 – Funções como 2^n surgem ao enumerar todos os subconjuntos de n itens. 
Como vimos, os algoritmos exponenciais tornam-se inúteis rapidamente, mas não tão rápido como. . .
	Funções fatoriais, f(n)=n! – Funções como n! surgem ao gerar todas as permutações ou ordenações de n itens.
A multiplicação é como a adição repetida. 
Considere a multiplicação por qualquer constante c > 0, seja 1,02 ou 1.000.000. 
Multiplicar uma função por uma constante não pode afetar seu comportamento assintótico, porque podemos multiplicar as constantes limitantes na análise Big O de c · f(n) por 1/c para fornecer constantes apropriadas para a análise Big O de f(n) .
O raciocínio grosseiro sobre o tempo de execução de um algoritmo geralmente é fácil, dada uma descrição escrita precisa do algoritmo. Nesta seção, trabalharei com vários exemplos, talvez com mais detalhes do que o necessário.
Uma regra básica na análise Big O é que o tempo de execução do pior caso decorre da multiplicação do maior número de vezes que cada loop aninhado pode iterar.
A correspondência de padrões é a operação algorítmica mais fundamental em strings de texto. 
Este algoritmo implementa o comando find disponível em qualquer navegador web ou editor de texto:

**Problema:**
Correspondência de padrões de substring.

**Entrada:**
Uma string de texto t e uma string de padrão p.

**Saída:**
t contém o padrão p como uma substring e, em caso afirmativo, onde? Talvez você esteja interessado em descobrir onde “Skiena” aparece em um determinado artigo de notícias (bem, eu estaria interessado em tal coisa). 
Esta é uma instância de correspondência de padrões de string com t como o artigo de notícias e p= "Skiena".
As somas aninhadas geralmente surgem na análise de algoritmos com loops aninhados. 
Considere o problema da multiplicação de matrizes:

**Problema:**
Multiplicação de Matrizes.

**Entrada:**
Duas matrizes, A (de dimensão x × y) e B (dimensão y × z).

**Saída:**
Uma matriz x × z C onde C[i][j] é o produto escalar da iésima linha de A e da jésima coluna de B.
Logaritmo é um anagrama de algoritmo, mas não é por isso que precisamos saber o que são logaritmos. 
Você viu o botão em sua calculadora, mas pode ter esquecido por que ele está lá. 
Um logaritmo é simplesmente uma função exponencial inversa. 
Dizer b^x=y é equivalente a dizer que 〖x=log〗_b y. 
Além disso, esta definição é o mesmo que dizer  b^(〖log〗_b y)=y.
Existem dois padrões de bits de comprimento 1 (0 e 1) e quatro de comprimento 2 (00, 01, 10 e 11). 
De quantos bits w precisamos para representar qualquer uma das n possibilidades diferentes, seja um dos n itens ou os inteiros de 1 a n?
Os números Harmônicos surgem como um caso especial de progressão aritmética, ou seja, H(n)=S(n,-1). 
Eles refletem a soma da progressão de recíprocos simples, a saber,

       H(n)=∑_(i=1)^n  1/i  ~ ln n
   
Como vimos, afirmar b^x=y equivale a dizer que  〖x=log〗_b y. 
O termo b é conhecido como a base do logaritmo. 
Três bases são de particular importância por razões matemáticas e históricas:

	Base b=2 – O logaritmo binário, geralmente denotado 〖lg〗_ x, é um logaritmo de base 2. 
 
Vimos como essa base surge sempre que ocorre o halving repetido (ou seja, busca binária) ou duplicação (ou seja, nós em árvores).
A maioria das aplicações algorítmicas de logaritmos implica logaritmos binários.

	Base b=e – O logaritmo natural, normalmente denotado por ln x, é uma base e=2,71828... logaritmo. 
O inverso de ln x é a função exponencial exp(x)=e^x  em sua calculadora. 
Assim, a composição dessas funções nos dá

       〖exp(In x)=x〗^  

	Base b=10 – Menos comum hoje é a b-10 ou logaritmo comum, geralmente denotado como 〖log〗_ x. 
Essa base foi empregada em réguas de cálculo e livros de logaritmos nos dias anteriores às calculadoras de bolso.
Já vimos uma propriedade importante dos logaritmos, a saber, que 

       〖log〗_a (xy)=〖log〗_a (x)+〖log〗_a (y)

O outro fato importante a ser lembrado é que é fácil converter um logaritmo de uma base para outra. 
Isso é uma consequência da fórmula:

       〖log〗_a b=(〖log〗_c b)/(〖log〗_c a)  

Assim, mudar a base de 〖log〗_ b de base-a para base-c envolve simplesmente multiplicar por 〖log〗_c a. 
É fácil converter uma função de log comum em uma função de log natural e vice-versa.
Duas implicações dessas propriedades dos logaritmos são importantes para apreciar de uma perspectiva algorítmica:

A base do logaritmo não tem impacto real na taxa de crescimento - Compare os três valores a seguir:

       log〗_2 (1.000.000)=19,9316, 〖log〗_3 (1.000.000)=12,5754 e 〖log〗_100 (1.000.000)=3. 
       
Uma grande mudança na base do logaritmo produz pouca diferença no valor do logaritmo. 
Mudar a base do logaritmo de a para c envolve dividir por 〖log〗_c a. 
Este fator de conversão é perdido para a notação Big O sempre que a e c são constantes. 
Assim, geralmente temos justificativa para ignorar a base do logaritmo ao analisar algoritmos.
Os logaritmos reduzem qualquer função ao tamanho – A taxa de crescimento do logaritmo de qualquer função polinomial é O(lg n).
Isso segue porque: 
       
       log〗_a  n^b=b.〖log〗_a  n 

**Resumo capítulo 2 continuação**

Este resumo discute a eficiência do tempo de execução de um algoritmo, concentrando-se em vários exemplos. O primeiro exemplo é o algoritmo para selecionar o elemento menos não classificado e colocá-lo no final da parte ordinal do array. O segundo exemplo é o algoritmo de inserção de elementos no array, que é um algoritmo quadrático. Esta análise é crucial porque garante que o limite de tempo obtido pelo algoritmo Big Oh esteja sempre correto. No entanto, pode ser muito geral, o que significa que o tempo real do pior caso pode ser inferior ao obtido através desta análise.
O terceiro exemplo é a correspondência de padrões de cordas. Esta é a operação algébrica mais fundamental em cadeias de texto. Este algoritmo implementa o comando find disponível em qualquer navegador web ou editor de texto. O problema é a correspondência dos padrões de substring. Este é um algoritmo simples que considera a possibilidade de começar em cada posição possível e testa se for o caso.
O quarto exemplo é a comparação dos comprimentos dos elementos de uma lista. Este é um algoritmo simples que verifica se todas as três dimensões são iguais. Se for comum o caso em que todas as três dimensões são iguais, torna-se um algoritmo cúbico.
Concluindo, este resumo fornece uma visão abrangente da eficiência de vários algoritmos, incluindo a seleção de elementos, a correspondência de padrões de strings e a comparação de comprimentos.
Logaritmos são funções exponenciais inversas que crescem gradativamente lentamente, como uma das funções exponenciais em qualquer processo em que as coisas são repetidamente decrescentes à metade. A busca binária é uma das ideias mais poderosas no design de algoritmos, pois são rápidas ou suficientes para serem usadas em instâncias de problemas de tamanho essencialmente ilimitado.
Árvores binárias de altura 1 podem ter até 2 nós de folha, enquanto uma árvore de altura 2 pode ter até quatro folhas. O número de folhas possíveis é multiplicado por cada vez que aumentamos a altura em um, então é a principal razão pela qual as árvores muito curtas podem ter muitas folhas, o que é a principal razão pela que as árvores binárias são fundamentais para o projeto de estruturas de dados rápidos.
Os logaritmos eram particularmente importantes nos dias anteriores às calculadoras de bolso, fornecendo a maneira mais fácil de multiplicar números grandes à mão. Os logaritmos são úteis para multiplicação, particularmente para exponenciação. O logaritmo de um produto é a soma dos logs, e a consequência direta é que o problema é reduzido a uma multiplicação mais uma chamada para cada uma dessas funções.
O algoritmo mais simples executa multiplicações, calculando. Em ambos os casos, reduzimos pela metade o tamanho do nosso expoente ao custo de, no máximo, duas multiplicações, então multiplicações são suficientes para calcular o valor final.
O algoritmo simples ilustra um princípio importante de dividir e conquistar, que seja aplicável à vida real. Quando não é uma potência de dois, o problema não pode ser dividido uniformemente, mas a diferença de um elemento entre os dois lados não pode causar nenhum desequilíbrio sério.
Logaritmos é uma técnica de logaritmo que utiliza um número de números e somas para entender a progressão aritmética. Os números harmônicos surgem como um caso especial de progressão aritmética, relacionando-se à soma da progressão de recíprocos simples. Eles são importantes porque explicam o "de onde vem o tronco" quando um magicamente sai da manipulação algébrica.
As Diretrizes Federais de Sentença para Fraude têm uma função de ponto real para fraude, mapeando dólares roubados em pontos. A segurança aumenta em um nível cada vez que a quantidade de dinheiro descoberto praticamente dobra. O nível de resiliência cresce logaritmicamente com a quantidade de dinheiro roubado.
Os logaritmos surgem sempre que as coisas são repetidamente reduzidas à metade ou duplicadas. O termo b é conhecido como a base do logaritmo, com base b=2 – O logaritmo binário, base b=e – O logaritmo natural, base b=10 – Menores hoje é a b-10 ou logaritmo comum, base b= 10 – O base b=b=b=c.
A propriedade importante dos logaritmos é que é fácil converter um logaritmo de uma base para outra. Uma grande mudança na base do logaritmo produz pouca diferença no valor do logaritmo, em consequência, geralmente temos justificativa para ignorar a base do logaritmo ao analisar algoritmos.
Os logaritmos resultantes de qualquer função ao tamanho, e a taxa de crescimento do logaritmo de qualquer função polinomial é O (lg n). Uma pesquisa binária em uma matriz ordenada de n^2 requer apenas duas vezes mais comparações do que uma pesquisa binária em n coisas. O poder da busca binária em uma ampla gama de problemas é uma consequência dessa observação.
A importância de uma divisão uniforme é importante para a quantidade de consultas ao pesquisa binária em uma lista telefônica realizada em Manhattan. Para a lista telefônica de Manhattan, agora usamos 〖log〗_(3/2) (1.000.000) ≈ 35 consultas no pior caso, não uma mudança significativa de 〖log〗_2 (1.000.000) ≈ 20. O poder da A busca binária vem de sua complexidade logarítmica, não a base do log.
Aquele olhar em seus olhos deveria ter me avisado antes de ele começar a falar. Os supercomputadores são rápidos e a força bruta parecia eliminar a necessidade de algoritmos inteligentes; pelo menos até os problemas ficarem difíceis.
Os primeiros números piramidais são 1,4,10,20,35,56,84,120 e 165. Uma conjectura desde 1928 é que todo número inteiro pode ser representado pela soma de no máximo cinco desses números piramidais. Um programa em supercomputadores funciona muito rápido em números menores, mas leva muito tempo assim que chega a 100.000 ou mais.
Os supercomputadores descobriram o crescimento assintótico, e o programa em que ele foi escrito tinha construído uma matriz de todos os Θ (n^ (1/3)) números piramidais de 1 e inclusive. Para testar cada número nesse intervalo, ele fez um teste de força bruta para estabelecer se era a soma de dois números piramidais.
Os logaritmos planejados com eficiência em avaliar a eficiência dos logaritmos em análise de algoritmos.
Um código de linha foi elaborado por uma criança que enfatizou o desempenho do programa, e o código foi executado em apenas 14 segundos, com um acréscimo de 5,3 vezes no período de quatro anos anteriores. O código foi elaborado com o compilador gcc, e a otimização de números piramidais é uma história primordial.
Ao escrever esta história de guerra, voltei a executar o programa mais de dez anos. No meu desktop SunBlade 150, o número resultante levava a 1.000.000 agora em 27,0 segundos, mas com otimização de nível 4, o trabalho foi executado em 14,0 segundos, tributo à qualidade do otimizador. O tempo de execução em minha máquina desktop melhorou por um fator de cerca de três no período de quatro anos anterior à minha primeira edição deste livro, com um acréscimo de 5,3 vezes nos últimos anos.
Um código foi modificado com a otimização de números piramidais, e um código foi modificado com a otimização de números piramidais.
Os códigos piramidais são da forma ((m³-m))/6, e o maior m tal que o número resultante seja no máximo n é ∛6n. Um código geral foi elaborado com a otimização de números piramidais, e um código foi elaborado com a otimização de números piramidais.
Os códigos piramidais são estruturados em dados classificados, e o código em dados classificados em dados classificados em dados classificados. Um código foi modificado com a otimização de números piramidais e a otimização de números piramidais, e um código foi modificado com a otimização de números piramidais e a otimização de números piramidais.

**Testando Compreensão:**

**Questão 1:** Qual é a importância da análise de algoritmos e por que os engenheiros de software devem se preocupar com ela?

**Resposta 1:** A análise de algoritmos é crucial para entender o desempenho e a eficiência de diferentes abordagens na resolução de problemas. Ela permite aos engenheiros de software escolher a melhor estratégia para otimizar o tempo de execução e o uso de recursos, considerando cenários de entrada variados.

**Questão 2:** O que é a notação Big O (O-grande) e para que ela é usada na análise de algoritmos?

**Resposta 2:** A notação Big O é usada para descrever a complexidade assintótica de algoritmos. Ela estima como o tempo de execução e os recursos aumentam em relação ao tamanho dos dados de entrada. A notação Big O ajuda a comparar algoritmos sem se preocupar com detalhes de implementação ou constantes.

**Questão 3:** Quais são as outras notações de complexidade além de Big O e qual é a diferença entre elas?

**Resposta 3:** Além de Big O, existem as notações Big Omega (Ω) e Big Theta (Θ). Big Omega representa o limite inferior da complexidade de um algoritmo, enquanto Big Theta representa um limite superior e inferior iguais. Enquanto Big O fornece uma estimativa superior do desempenho, Big Omega e Big Theta consideram limites inferiores e médios.

**Questão 4:** Como a análise de tempo e espaço dos algoritmos é realizada?

**Resposta 4:** A análise de tempo envolve a contagem de operações elementares executadas pelo algoritmo, considerando o pior caso. A análise de espaço mede a quantidade de memória necessária para executar o algoritmo. A complexidade de tempo e espaço é geralmente expressa em notação Big O.

**Questão 5:** Por que a análise experimental de algoritmos é importante e como ela é realizada?

**Resposta 5:** A análise experimental valida as conclusões teóricas sobre o desempenho dos algoritmos. Ela envolve a execução dos algoritmos em cenários reais e a medição do tempo de execução e uso de recursos. Experimentos controlados são projetados para explorar diferentes cenários e validar as análises teóricas.
