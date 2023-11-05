### Capítulo 8 - Programação Dinâmica

A programação dinâmica nos dá uma maneira de projetar algoritmos personalizados que pesquisam sistematicamente todas as possibilidades (garantindo assim a correção) enquanto armazenam os resultados para evitar a recomputação (proporcionando assim eficiência). Ao armazenar as consequências de todas as decisões possíveis e usar essas informações de forma sistemática, a quantidade total de trabalho é minimizada.

A programação dinâmica é geralmente o método certo para problemas de otimização em objetos combinatórios que têm uma ordem inerente da esquerda para a direita entre os componentes. Os objetos da esquerda para a direita incluem: cadeias de caracteres, árvores com raízes, polígonos e sequências inteiras.

### 8.1 Cache vs. Computação

A programação dinâmica é essencialmente uma troca de espaço por tempo. Recomputar repetidamente uma determinada quantidade é inofensivo, a menos que o tempo gasto para fazer isso atrapalhe o desempenho. Então, é melhor armazenar os resultados do cálculo inicial e procurá-los em vez de recalculá-los novamente.

### 8.1.1 Números de Fibonacci por Recursão

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

### 8.1.2 Números de Fibonacci por Cache



### 8.1.3 Números de Fibonacci por Programação Dinâmica


### 8.1.4 Coeficientes Binomiais

### 8.2 Correspondência aproximada de strings


### 8.2.1 Editar distância por recursão


### 8.2.2 Editar distância por programação dinâmica

### 8.2.3 Reconstruindo o Caminho

### 8.2.4 Variedades de distância de edição

### 8.3 Sequência Crescente Mais Longa

### 8.5 O Problema de Partição

### 8.6 Analisando gramáticas livres de contexto


### 8.6.1 Triangulação de Peso Mínimo

### 8.7 Limitações da programação dinâmica: TSP

### 8.7.1 Quando os algoritmos de programação dinâmica estão corretos?

### 8.7.2 Quando os algoritmos de programação dinâmica são eficientes?



##
