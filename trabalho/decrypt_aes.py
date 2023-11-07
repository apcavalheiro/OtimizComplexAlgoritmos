import tkinter as tk
from cryptography.fernet import Fernet

# Chave Fernet válida (cole a chave que você gerou anteriormente aqui)
chave = b'MWVqsaTYKCg3sWVQZ22NE8KUxW_6SpOybkN-CRFdaSo='

# Função para decifrar usando AES
def decifrar_aes(texto_cifrado):
    fernet = Fernet(chave)
    texto_decifrado_bytes = fernet.decrypt(texto_cifrado)
    texto_decifrado = texto_decifrado_bytes.decode()
    return texto_decifrado

# Função para decifrar o texto quando o botão "Decifrar" é pressionado
def decifrar_texto_aes():
    texto_cifrado = entrada_texto_cifrado_aes.get()
    texto_decifrado = decifrar_aes(texto_cifrado)
    label_resultado_decifrado_aes["text"] = "Texto Decifrado: " + texto_decifrado

# Configuração da interface gráfica para a descriptografia do AES
janela_decifrar_aes = tk.Tk()
janela_decifrar_aes.title("AES Decifrar")

entrada_label_cifrado_aes = tk.Label(janela_decifrar_aes, text="Texto Cifrado:")
entrada_label_cifrado_aes.pack()

entrada_texto_cifrado_aes = tk.Entry(janela_decifrar_aes)
entrada_texto_cifrado_aes.pack()

botao_decifrar_aes = tk.Button(janela_decifrar_aes, text="Decifrar", command=decifrar_texto_aes)
botao_decifrar_aes.pack()

label_resultado_decifrado_aes = tk.Label(janela_decifrar_aes, text="")
label_resultado_decifrado_aes.pack()

janela_decifrar_aes.mainloop()
