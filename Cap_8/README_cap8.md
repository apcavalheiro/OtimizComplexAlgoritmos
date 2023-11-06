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

Figura 8.1: A árvore de computação para calcular números de Fibonacci recursivamente

### 8.1.2 Números de Fibonacci por Cache

Podemos armazenar (ou armazenar em cache) explicitamente os resultados de cada cálculo de Fibonacci F (k) em uma estrutura de dados de tabela indexada pelo parâmetro k. A chave para evitar a recomputação é verificar explicitamente o valor antes de tentar computá-lo:

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

![image](https://github.com/apcavalheiro/OtimizComplexAlgoritmos/assets/142835210/3f690a34-84da-4769-b251-5e86eb2dc878)

Figura 8.2: A árvore de computação de Fibonacci ao armazenar valores em cache.




### 8.1.3 Números de Fibonacci por Programação Dinâmica


### 8.1.4 Coeficientes Binomiais

### 8.2 Correspondência Aproximada de Strings


### 8.2.1 Editar Distância por Recursiva


### 8.2.2 Editar Distância por Programação Dinâmica

### 8.2.3 Reconstruindo o Caminho

### 8.2.4 Variedades de Distância de Edição

### 8.3 Sequência Crescente Mais Longa

### 8.5 O Problema de Partição

### 8.6 Analisando Gramáticas Livres de Contexto


### 8.6.1 Triangulação de Peso Mínimo

### 8.7 Limitações da programação dinâmica: TSP

### 8.7.1 Quando os algoritmos de programação dinâmica estão corretos?

### 8.7.2 Quando os algoritmos de programação dinâmica são eficientes?



##
