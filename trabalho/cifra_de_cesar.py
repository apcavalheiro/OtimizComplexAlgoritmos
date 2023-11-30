import argparse

def cifra_de_cesar(texto, chave):
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            maiuscula = caractere.isupper()
            caractere = chr((ord(caractere) + chave - ord('A' if maiuscula else 'a')) % 26 + ord('A' if maiuscula else 'a'))
        resultado += caractere
    return resultado

def main():
    parser = argparse.ArgumentParser(description='Cifra de César - Codificar e Decodificar Mensagens')
    parser.add_argument('acao', choices=['codificar', 'decodificar'], help='Ação a ser realizada (codificar ou decodificar)')
    parser.add_argument('mensagem', type=str, help='Mensagem a ser processada')
    parser.add_argument('chave', type=int, help='Chave de deslocamento para a cifra de César')
    
    args = parser.parse_args()

    if args.acao == 'codificar':
        resultado = cifra_de_cesar(args.mensagem, args.chave)
        print(f'Mensagem Codificada: {resultado}')
    elif args.acao == 'decodificar':
        resultado = cifra_de_cesar(args.mensagem, -args.chave)  # Decodificar usando chave negativa
        print(f'Mensagem Decodificada: {resultado}')

if __name__ == "__main__":
    main()
