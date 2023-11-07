import tkinter as tk
from cryptography.fernet import Fernet

# Chave Fernet válida
chave = b'MWVqsaTYKCg3sWVQZ22NE8KUxW_6SpOybkN-CRFdaSo='

# Função para cifrar usando AES
def cifrar_aes(texto, chave):
    fernet = Fernet(chave)
    texto_bytes = texto.encode()
    texto_cifrado = fernet.encrypt(texto_bytes)
    return texto_cifrado

# Função para cifrar o texto quando o botão "Cifrar" é pressionado
def cifrar_texto_aes():
    texto_original = entrada_texto_aes.get()
    texto_cifrado = cifrar_aes(texto_original, chave)
    texto_cifrado_str = texto_cifrado.decode()
    texto_cifrado_entry.delete(0, tk.END)
    texto_cifrado_entry.insert(0, texto_cifrado_str)

# Configuração da interface gráfica para AES
janela_aes = tk.Tk()
janela_aes.title("AES (Advanced Encryption Standard)")

entrada_label_aes = tk.Label(janela_aes, text="Texto Original:")
entrada_label_aes.pack()

entrada_texto_aes = tk.Entry(janela_aes)
entrada_texto_aes.pack()

botao_cifrar_aes = tk.Button(janela_aes, text="Cifrar", command=cifrar_texto_aes)
botao_cifrar_aes.pack()

texto_cifrado_entry = tk.Entry(janela_aes)
texto_cifrado_entry.pack()

label_resultado_aes = tk.Label(janela_aes, text="")
label_resultado_aes.pack()

janela_aes.mainloop()
