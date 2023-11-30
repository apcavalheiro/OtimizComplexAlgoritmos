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
