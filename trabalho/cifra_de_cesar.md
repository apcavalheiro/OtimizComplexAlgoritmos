# Cifra de César - Codificação e Decodificação

Este é um exemplo simples de implementação da Cifra de César em Python. O código permite codificar e decodificar mensagens usando a Cifra de César.

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/apcavalheiro/OtimizComplexAlgoritmos.git
cd OtimizComplexAlgoritmos/trabalho/
```

2. Execute o script `cifra_de_cesar.py` com argumentos da linha de comando:

```bash
python cifra_de_cesar.py codificar "Mensagem a ser codificada" 3
```

Substitua `"Mensagem a ser codificada"` pela mensagem que você deseja codificar e `3` pelo número de posições de deslocamento na cifra.

Para decodificar:

```bash
python cifra_de_cesar.py decodificar "Texto-codificado" 3
```

Substitua `"Texto-codificado"` pelo texto codificado e `3` pelo mesmo número de posições usado para codificar.

## Exemplo

### Codificar

```bash
python cifra_de_cesar.py codificar "Hello, Caesar!" 3
```

Saída:

```
Mensagem Codificada: Khoor, Fdhvd!
```

### Decodificar

```bash
python cifra_de_cesar.py decodificar "Khoor, Fdhvd!" 3
```

Saída:

```
Mensagem Decodificada: Hello, Caesar!
```

## Observações

- Este é um exemplo educacional da Cifra de César. Não é adequado para fins de segurança real.
- Mantenha a chave (número de deslocamento) em segredo para garantir a segurança da cifra.
- Este código trata apenas letras do alfabeto e não afeta caracteres não alfabéticos.


Para salvar o relatório em um arquivo de texto (txt), você pode adicionar o argumento `--salvar` quando executar o script. Aqui está como você pode fazer isso:

```bash
python script_cifra_cesar.py --tamanhos_mensagem 100 500 1000 --chaves 3 5 7 --salvar
```

Se você não fornecer `--salvar`, o script exibirá o gráfico e os resultados no console, mas não salvará em um arquivo. Se você fornecer `--salvar`, ele salvará o gráfico como `grafico_cifra_cesar.png` e o relatório como `relatorio_cifra_cesar.txt`.

Agora, para documentar o código em um formato `readme.md`, você pode criar um arquivo chamado `readme.md` no mesmo diretório do seu projeto e adicionar o seguinte conteúdo:

# Avaliação de Desempenho da Cifra de César

Este script Python avalia o desempenho da Cifra de César, medindo os tempos de codificação e decodificação para diferentes tamanhos de mensagem e chaves.

## Requisitos

- Python 3.x
- Bibliotecas Python: matplotlib

## Como Usar

Execute o script `script_cifra_cesar.py` com os seguintes argumentos:

```bash
python script_cifra_cesar.py --tamanhos_mensagem 100 500 1000 --chaves 3 5 7 --salvar
```

Isso gerará um gráfico de desempenho e salvará os resultados em um arquivo de relatório.

## Parâmetros

- `--tamanhos_mensagem`: Tamanhos de mensagem para avaliação.
- `--chaves`: Chaves para avaliação.
- `--salvar`: Opcional. Se fornecido, salva o gráfico e o relatório em vez de exibi-los.

## Resultados

Os resultados incluem tempos de codificação e decodificação para cada tamanho de mensagem e chave. O gráfico e o relatório são gerados para análise.
