import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def aes_criptografar(texto, chave):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(chave), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Pad the input data using PKCS7
    padder = padding.PKCS7(128).padder()
    texto_padded = padder.update(texto.encode()) + padder.finalize()

    texto_cifrado = encryptor.update(texto_padded) + encryptor.finalize()
    return texto_cifrado

def aes_descriptografar(texto_cifrado, chave):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(chave), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    texto_padded = decryptor.update(texto_cifrado) + decryptor.finalize()

    # Unpad the decrypted data using PKCS7
    unpadder = padding.PKCS7(128).unpadder()
    texto = unpadder.update(texto_padded) + unpadder.finalize()

    return texto.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description='AES - Criptografar e Descriptografar Mensagens')
    parser.add_argument('acao', choices=['criptografar', 'descriptografar'], help='Ação a ser realizada (criptografar ou descriptografar)')
    parser.add_argument('mensagem', type=str, help='Mensagem a ser processada')
    parser.add_argument('chave', type=str, help='Chave AES (16, 24 ou 32 caracteres)')

    args = parser.parse_args()

    chave = args.chave.encode('utf-8')

    if len(chave) not in [16, 24, 32]:
        print('A chave deve ter 16, 24 ou 32 caracteres.')
        return

    if args.acao == 'criptografar':
        resultado = aes_criptografar(args.mensagem, chave)
        print(f'Mensagem Criptografada: {resultado.hex()}')
    elif args.acao == 'descriptografar':
        texto_cifrado = bytes.fromhex(args.mensagem)
        resultado = aes_descriptografar(texto_cifrado, chave)
        print(f'Mensagem Descriptografada: {resultado}')

if __name__ == "__main__":
    main()
