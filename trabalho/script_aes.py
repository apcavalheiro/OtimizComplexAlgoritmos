import argparse
import time
import matplotlib.pyplot as plt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def ajustar_tamanho_chave(chave, tamanho):
    chave_bytes = chave.encode('utf-8')
    if len(chave_bytes) < tamanho:
        return chave_bytes.ljust(tamanho, b'\0')  # Preencher com zeros à direita se a chave for muito curta
    return chave_bytes[:tamanho]  # Truncar se a chave for muito longa

def aes_criptografar(texto, chave):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(chave), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    texto_padded = padder.update(texto.encode()) + padder.finalize()

    texto_cifrado = encryptor.update(texto_padded) + encryptor.finalize()
    return texto_cifrado

def aes_descriptografar(texto_cifrado, chave):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(chave), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    texto_padded = decryptor.update(texto_cifrado) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    texto = unpadder.update(texto_padded) + unpadder.finalize()

    return texto.decode('utf-8')

def avaliar_aes(tamanho_mensagem, chave):
    mensagem = 'A' * tamanho_mensagem  # Mensagem de exemplo

    tempos_criptografar = []
    tempos_descriptografar = []

    chave_bytes = ajustar_tamanho_chave(chave, 32)  # Sempre ajustar para 32 bytes (256 bits)

    for _ in range(10):  # Executar 10 vezes para média
        inicio_criptografar = time.time()
        aes_criptografar(mensagem, chave_bytes)
        fim_criptografar = time.time()
        tempos_criptografar.append(fim_criptografar - inicio_criptografar)

        texto_cifrado = aes_criptografar(mensagem, chave_bytes)

        inicio_descriptografar = time.time()
        aes_descriptografar(texto_cifrado, chave_bytes)
        fim_descriptografar = time.time()
        tempos_descriptografar.append(fim_descriptografar - inicio_descriptografar)

    return sum(tempos_criptografar) / 10, sum(tempos_descriptografar) / 10

def gerar_grafico_aes(tamanhos_mensagem, chaves_aes, salvar=False):
    fig, axs = plt.subplots(2, 1, figsize=(8, 10))

    for chave_aes in chaves_aes:
        tempos_cript, tempos_dec = [], []
        for tamanho in tamanhos_mensagem:
            tempo_cript, tempo_dec = avaliar_aes(tamanho, chave_aes)
            tempos_cript.append(tempo_cript)
            tempos_dec.append(tempo_dec)

        axs[0].plot(tamanhos_mensagem, tempos_cript, label=f'Criptografia - Chave {chave_aes}')
        axs[1].plot(tamanhos_mensagem, tempos_dec, label=f'Descriptografia - Chave {chave_aes}')

    axs[0].set_xlabel('Tamanho da Mensagem')
    axs[0].set_ylabel('Tempo (s)')
    axs[0].set_title('Desempenho do AES - Criptografia')
    axs[0].legend()

    axs[1].set_xlabel('Tamanho da Mensagem')
    axs[1].set_ylabel('Tempo (s)')
    axs[1].set_title('Desempenho do AES - Descriptografia')
    axs[1].legend()

    plt.tight_layout()

    if salvar:
        relatorio_path = "relatorio_aes.txt"
        with open(relatorio_path, 'w') as relatorio:
            relatorio.write("Desempenho do AES\n\n")
            relatorio.write("Tamanho da Mensagem\tChave\tTempo Criptografia (s)\tTempo Descriptografia (s)\n")

            for chave_aes in chaves_aes:
                for tamanho in tamanhos_mensagem:
                    tempo_cript, tempo_dec = avaliar_aes(tamanho, chave_aes)
                    relatorio.write(f"{tamanho}\t{chave_aes}\t{tempo_cript}\t{tempo_dec}\n")

        print(f"Relatório salvo em: {relatorio_path}")

        grafico_path = "grafico_aes.png"
        plt.savefig(grafico_path)
        print(f"Gráfico salvo em: {grafico_path}")
    else:
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Avaliação de Desempenho do AES')
    parser.add_argument('--tamanhos_mensagem', nargs='+', type=int, default=[100, 500, 1000], help='Tamanhos de mensagem para avaliação')
    parser.add_argument('--chaves_aes', nargs='+', type=str, default=["chaveAES128", "chaveAES192", "chaveAES256"], help='Chaves AES para avaliação')
    parser.add_argument('--salvar', action='store_true', help='Salvar o gráfico e o relatório em vez de exibi-los')

    args = parser.parse_args()
    gerar_grafico_aes(args.tamanhos_mensagem, args.chaves_aes, args.salvar)
