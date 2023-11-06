### Capítulo 8 - Programação Dinâmica

A programação dinâmica nos dá uma maneira de projetar algoritmos personalizados que pesquisam sistematicamente todas as possibilidades (garantindo assim a correção) enquanto armazenam os resultados para evitar a recomputação (proporcionando assim eficiência). Ao armazenar as consequências de todas as decisões possíveis e usar essas informações de forma sistemática, a quantidade total de trabalho é minimizada.

A programação dinâmica é geralmente o método certo para problemas de otimização em objetos combinatórios que têm uma ordem inerente da esquerda para a direita entre os componentes. Os objetos da esquerda para a direita incluem: cadeias de caracteres, árvores com raízes, polígonos e sequências inteiras.

### 8.1 Cache vs. Computação

A programação dinâmica é essencialmente uma troca de espaço por tempo. Recomputar repetidamente uma determinada quantidade é inofensivo, a menos que o tempo gasto para fazer isso atrapalhe o desempenho. Então, é melhor armazenar os resultados do cálculo inicial e procurá-los em vez de recalculá-los novamente.

### 8.1.1 Números de Fibonacci por Recursiva

Os números de Fibonacci foram originalmente definidos pelo matemático italiano Fibonacci no século XIII para modelar o crescimento das populações de coelhos. Um algoritmo de função recursiva escrito em C se parece com isto:

```
long fib_r(int n)
{
	if (n == 0) return(0);
	if (n == 1) return(1);
	return(fib_r(n-1) + fib_r(n-2));
}
```
![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/19896dc0-b67f-4413-ab72-284160727d2b)

Figura 8.1: A árvore de computação para calcular números de Fibonacci recursivamente.

### 8.1.2 Números de Fibonacci por Cache

Podemos armazenar (ou armazenar em cache) explicitamente os resultados de cada cálculo de Fibonacci F (k) em uma estrutura de dados de tabela indexada pelo parâmetro k. A chave para evitar a recomputação é verificar explicitamente o valor antes de tentar computá-lo:

```
#define MAXN 45 /* largest interesting n */

#define UNKNOWN -1 /* contents denote an empty cell */

long f[MAXN+1]; /* array for caching computed fib values */

long fib_c(int n)

{
	
 if (f[n] == UNKNOWN)
 
		f[n] = fib_c(n-1) + fib_c(n-2);
return(f[n]);

}

long fib_c_driver(int n)

{

	int i; /* counter */
	f[0] = 0;
	f[1] = 1;
	for (i=2; i<=n; i++) f[i] = UNKNOWN;
 
	return(fib_c(n));
}
```
![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/3f690a34-84da-4769-b251-5e86eb2dc878)

Figura 8.2: A árvore de computação de Fibonacci ao armazenar valores em cache.
### 8.1.3 Números de Fibonacci por Programação Dinâmica

Podemos calcular Fn em tempo linear mais facilmente, especificando explicitamente a ordem de avaliação da relação de recorrência:

```
long fib_dp(int n)
{
	int i; /* counter */
	long f[MAXN+1]; /* array to cache computed fib values */

	f[0] = 0;
	f[1] = 1;
	for (i=2; i<=n; i++) f[i] = f[i-1]+f[i-2];
	
	return(f[n]);
}
```
### 8.1.4 Coeficientes Binomiais

Uma maneira mais estável de calcular coeficientes binomiais é usar a relação de recorrência implícita na construção do triângulo de Pascal:

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/05c0603c-7c27-4eb4-890b-956ff27b2698)

Figura 8.3: Ordem de avaliação do coeficiente binomial em M [5, 4] (l). Condições de inicialização A-K, avaliações de recorrência 1-10. 

### 8.2 Correspondência Aproximada de Strings

Existem três tipos naturais de mudanças:

• **Substituição** - Substitua um único caractere do padrão P por um caractere diferente no texto T, como alterar “shot” para “spot”.

• **Inserção** - insira um único caractere no padrão P para ajudá-lo a corresponder ao texto T, como alterar “ago” para “agog”.

• **Exclusão** - Exclua um único caractere do padrão P para ajudá-lo a corresponder ao texto T, como alterar “hour” para “our”.

### 8.2.1 Editar Distância por Recursiva

Podemos definir um algoritmo recursivo usando a observação de que o último caractere na string deve ser correspondido, substituído, inserido ou excluído. Cortar os caracteres envolvidos nesta última operação de edição deixa um par de strings menores. Sejam i e j o último caractere do prefixo relevante de P e T, respectivamente. Existem três pares de strings mais curtas após a última operação, correspondendo às strings após uma correspondência / substituição, inserção ou exclusão. Se soubéssemos o custo de edição desses três pares de strings menores, poderíamos decidir qual opção leva à melhor solução e escolher essa opção de acordo. 

```
#define MATCH 0 /* enumerated type symbol for match */
#define INSERT 1 /* enumerated type symbol for insert */
#define DELETE 2 /* enumerated type symbol for delete */

int string_compare(char *s, char *t, int i, int j)
{
	int k; /* counter */
	int opt[3]; /* cost of the three options */
	int lowest_cost; /* lowest cost */
	
	if (i == 0) return(j * indel(’ ’));
	
	if (j == 0) return(i * indel(’ ’));
	
	opt[MATCH] = string_compare(s,t,i-1,j-1) + match(s[i],t[j]);
	opt[INSERT] = string_compare(s,t,i,j-1) + indel(t[j]);
	opt[DELETE] = string_compare(s,t,i-1,j) + indel(s[i]);

	lowest_cost = opt[MATCH];
	for (k=INSERT; k<=DELETE; k++)
		if (opt[k] < lowest_cost) lowest_cost = opt[k];

	return( lowest_cost );
}
```

### 8.2.2 Editar Distância por Programação Dinâmica

Uma implementação de programação dinâmica baseada em tabela desse algoritmo é fornecida abaixo. A tabela é uma matriz bidimensional m onde cada um dos | P | · | T | células contém o custo da solução ideal para um subproblema, bem como um ponteiro pai explicando como chegamos a este local:

```
typedef struct {
custo interno; / * custo de alcançar esta célula * /
int parent; /* célula parental */
} célula;

célula m [MAXLEN + 1] [MAXLEN + 1]; / * tabela de programação dinâmica * /
```
![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/da193c00-2531-4ecb-993a-3a4fbc2b8e26)

Figura 8.4: Exemplo de uma matriz de programação dinâmica para editar o cálculo da distância, com o caminho de alinhamento ideal destacado em negrito.

### 8.2.3 Reconstruindo o Caminho

A reconstrução dessas decisões é feita caminhando para trás a partir do estado de objetivo, seguindo o ponteiro pai de volta para uma célula anterior. Repetimos esse processo até chegarmos de volta à célula inicial. 

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/91fba545-b0a8-43a2-8980-8fa686a559aa)


Figura 8.5: Matriz principal para edição de cálculo de distância, com o caminho de alinhamento ideal destacado em negrito.

### 8.2.4 Variedades de Distância de Edição

Eles se enquadram em quatro categorias:

• **Inicialização da tabela** - As funções row init e column init inicializam a linha zero e a coluna da tabela de programação dinâmica, respectivamente. Para o problema de distância de edição de string, as células (i, 0) e (0, i) correspondem a strings de comprimento-i correspondentes à string vazia. 

• **Custos de penalidade** - As funções match (c, d) e indel (c) apresentam os custos para transformar o caractere c em d e inserir / excluir o caractere c. Para distância de edição padrão, a correspondência não deve custar nada se os caracteres forem idênticos e, caso contrário; enquanto indel retorna 1 independentemente de qual seja o argumento. 

• **Identificação da célula objetivo** - A célula objetivo da função retorna os índices da célula que marca o ponto final da solução. Para editar a distância, isso é definido pelo comprimento das duas strings de entrada.

• **Ações de rastreamento** - As funções combinam, inserem e excluem realizam as ações apropriadas para cada operação de edição durante o rastreamento. Para editar a distância, isso pode significar imprimir o nome da operação ou personagem envolvido, conforme determinado pelas necessidades do aplicativo.

• **Correspondência de substring** - suponha que desejamos encontrar onde um padrão curto P ocorre melhor em um texto longo T - digamos, procurando por “Skiena” em todos os seus erros ortográficos (Skienna, Skena, Skina, ...) em um arquivo longo.

• **Subsequência comum mais longa** - talvez estejamos interessados em encontrar a sequência de caracteres mais longa e dispersa incluída em ambas as sequências. Uma subsequência comum é definida por todas as correspondências de caracteres idênticos em um traço de edição. Para maximizar o número de tais correspondências, devemos evitar a substituição de caracteres não idênticos.  

• **Subsequência Monótona Máxima** - Uma sequência numérica aumenta monotonicamente se o iº elemento for pelo menos tão grande quanto o (i - 1) o elemento. O problema da subsequência monotônica máxima busca deletar o menor número de elementos de uma string de entrada S para deixar uma subsequência monotonicamente crescente. Uma subsequência crescente mais longa de 243517698 é 23568.

### 8.3 Sequência Crescente Mais Longa

• O comprimento da sequência crescente mais longa em s1, s2, ..., sn − 1 parece útil saber. Na verdade, esta será a sequência crescente mais longa em S, a menos que sn estenda alguma sequência crescente do mesmo comprimento.

• Precisamos saber o comprimento da sequência mais longa que sn irá estender. Para ter certeza de que sabemos disso, realmente precisamos do comprimento da sequência mais longa que qualquer valor possível para sn pode estender.

### 8.5 O Problema de Partição

Suponha que três funcionários tenham a tarefa de examinar uma estante de livros em busca de uma determinada informação. Para realizar o trabalho de forma justa e eficiente, os livros devem ser divididos entre os três trabalhadores. Para evitar a necessidade de reorganizar os livros ou separá-los em pilhas, é mais simples dividir a estante em três regiões e atribuir cada região a um trabalhador.

Mas qual é a maneira mais justa de dividir a prateleira? Se todos os livros tiverem o mesmo comprimento, o trabalho será bem fácil. Basta dividir os livros em regiões de tamanhos iguais,
100 100 100 | 100 100 100 | 100 100 100
para que todos tenham 300 páginas para lidar.

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/2750d520-0679-4b6a-babb-032ffdfef0a0)

Figura 8.9: Uma gramática livre de contexto (l) com uma árvore de análise associada (r).

### 8.6 Analisando Gramáticas Livres de Contexto

Os compiladores identificam se o programa fornecido é legal na linguagem de programação e recompensam você com erros de sintaxe, caso contrário. Isso requer uma descrição precisa da sintaxe da linguagem, normalmente fornecida por uma gramática livre de contexto.

Analisar uma determinada sequência de texto S de acordo com uma dada gramática livre de contexto G é o problema algorítmico de construir uma árvore de análise de substituições de regras definindo S como um único símbolo não terminal de G.

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/b08e9afa-ebec-409f-9358-adc0bf025cb2)

A Figura 8.10: Dois triangulações diferentes de um dado convexa sete-gon.

### 8.6.1 Triangulação de Peso Mínimo

Uma triangulação de um polígono P = {v1, ..., vn, v1} é um conjunto de diagonais sem intersecção que divide o polígono em triângulos. Dizemos que o peso de uma triangulação é a soma dos comprimentos de suas diagonais. Conforme mostrado na Figura 8.10, qualquer polígono dado pode ter muitas triangulações diferentes. Procuramos encontrar sua triangulação de peso mínimo para um dado polígono p. A triangulação é um componente fundamental da maioria dos algoritmos geométricos.

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/bde3df34-c7ff-4ec3-99ae-28e40bcaea3d)

Figura 8.11: Selecionando o vértice k para emparelhar com uma aresta (i, j) do polígono.

### 8.7 Limitações da programação dinâmica: TSP

### 8.7.1 Quando os algoritmos de programação dinâmica estão corretos?

### 8.7.2 Quando os algoritmos de programação dinâmica são eficientes?
