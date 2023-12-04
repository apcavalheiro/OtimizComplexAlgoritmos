import argparse
import time
import matplotlib.pyplot as plt

def cifra_de_cesar(texto, chave):
    resultado = ''
    for caractere in texto:
        if caractere.isalpha():
            maiuscula = caractere.isupper()
            caractere = chr((ord(caractere) + chave - ord('A' if maiuscula else 'a')) % 26 + ord('A' if maiuscula else 'a'))
        resultado += caractere
    return resultado

def avaliar_cifra_cesar(tamanho_mensagem, chave):
    mensagem = 'A' * tamanho_mensagem  # Mensagem de exemplo

    tempos_codificacao = []
    tempos_decodificacao = []

    for _ in range(10):  # Executar 10 vezes para média
        inicio_codificacao = time.time()
        cifra_de_cesar(mensagem, chave)
        fim_codificacao = time.time()
        tempos_codificacao.append(fim_codificacao - inicio_codificacao)

        inicio_decodificacao = time.time()
        cifra_de_cesar(mensagem, -chave)  # Decodificar usando chave negativa
        fim_decodificacao = time.time()
        tempos_decodificacao.append(fim_decodificacao - inicio_decodificacao)

    return sum(tempos_codificacao) / 10, sum(tempos_decodificacao) / 10

def salvar_relatorio(tamanhos_mensagem, chaves, resultados, nome_arquivo='relatorio.txt'):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Relatório de Avaliação da Cifra de César\n\n")

        for i, chave in enumerate(chaves):
            arquivo.write(f"Chave: {chave}\n")
            arquivo.write("Tamanho da Mensagem | Tempo de Codificação (s) | Tempo de Decodificação (s)\n")
            arquivo.write("-" * 60 + "\n")

            for j, tamanho in enumerate(tamanhos_mensagem):
                tempo_codificacao, tempo_decodificacao = resultados[i][j]
                arquivo.write(f"{tamanho:^20} {tempo_codificacao:^28.6f} {tempo_decodificacao:^28.6f}\n")

            arquivo.write("\n")

def gerar_grafico_cifra_cesar(tamanhos_mensagem, chaves, salvar=False):
    resultados = []

    for chave in chaves:
        tempos_cod, tempos_decod = [], []
        for tamanho in tamanhos_mensagem:
            tempo_codificacao, tempo_decodificacao = avaliar_cifra_cesar(tamanho, chave)
            tempos_cod.append(tempo_codificacao)
            tempos_decod.append(tempo_decodificacao)

        resultados.append(list(zip(tempos_cod, tempos_decod)))

    fig, axs = plt.subplots(2, 1, figsize=(8, 10))

    for i, chave in enumerate(chaves):
        tempos_cod, tempos_decod = zip(*resultados[i])
        axs[0].plot(tamanhos_mensagem, tempos_cod, label=f'Codificação - Chave {chave}')
        axs[1].plot(tamanhos_mensagem, tempos_decod, label=f'Decodificação - Chave {chave}')

    axs[0].set_xlabel('Tamanho da Mensagem')
    axs[0].set_ylabel('Tempo (s)')
    axs[0].set_title('Desempenho da Cifra de César - Codificação')
    axs[0].legend()

    axs[1].set_xlabel('Tamanho da Mensagem')
    axs[1].set_ylabel('Tempo (s)')
    axs[1].set_title('Desempenho da Cifra de César - Decodificação')
    axs[1].legend()

    plt.tight_layout()

    if salvar:
        plt.savefig('grafico_cifra_cesar.png')
        salvar_relatorio(tamanhos_mensagem, chaves, resultados, nome_arquivo='relatorio_cifra_cesar.txt')
    else:
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Avaliação de Desempenho da Cifra de César')
    parser.add_argument('--tamanhos_mensagem', nargs='+', type=int, default=[100, 500, 1000], help='Tamanhos de mensagem para avaliação')
    parser.add_argument('--chaves', nargs='+', type=int, default=[3, 5, 7], help='Chaves para avaliação')
    parser.add_argument('--salvar', action='store_true', help='Salvar o gráfico e o relatório em vez de exibi-los')

    args = parser.parse_args()
    gerar_grafico_cifra_cesar(args.tamanhos_mensagem, args.chaves, args.salvar)
