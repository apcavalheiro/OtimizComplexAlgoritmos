import tkinter as tk

# Função para criptografar usando a Cifra de César
def cifra_de_cesar(texto, chave):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            texto_cifrado += chr((ord(char) - shift + chave) % 26 + shift)
        else:
            texto_cifrado += char
    return texto_cifrado

# Função para cifrar o texto quando o botão "Cifrar" é pressionado
def cifrar_texto():
    texto_original = entrada_texto.get()
    chave = int(entrada_chave.get())
    texto_cifrado = cifra_de_cesar(texto_original, chave)
    label_resultado["text"] = "Texto Cifrado: " + texto_cifrado

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Cifra de César")

entrada_label = tk.Label(janela, text="Texto Original:")
entrada_label.pack()

entrada_texto = tk.Entry(janela)
entrada_texto.pack()

chave_label = tk.Label(janela, text="Chave (deslocamento):")
chave_label.pack()

entrada_chave = tk.Entry(janela)
entrada_chave.pack()

botao_cifrar = tk.Button(janela, text="Cifrar", command=cifrar_texto)
botao_cifrar.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()