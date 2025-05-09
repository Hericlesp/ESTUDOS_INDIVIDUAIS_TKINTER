import tkinter as tk


root = tk.Tk()
root.title("SAIDAS")
root.geometry("500x800")
root.config(bg="#f2f2f2")

# COMANDOS DE SAIDA

# Label
label_lbl = tk.Label(root, text="LABEL", font="Arial,16,Bold").pack(padx=200, anchor="w")
descLabel = tk.Label(root, text='''.Label(  , text= '' ) 
Exibe texto ou imagem em uma janela
EXEMPLO: EXIBIR NOME''').pack() 
label = tk.Label(root, text="NOME")
label.pack(padx=10) 

# Message
msg_lbl = tk.Label(root, text="MESSAGE", font="Arial,16,Bold").pack(padx=200, anchor="w")
descMessage = tk.Label(root, text='''.Message(  , text= '' )
Exibe texto ou imagem em uma janela
EXEMPLO: EXIBIR MENSAGEM''').pack() 
msg = tk.Message(root, text="MENSAGEM")
msg.pack(padx=10)       

root.mainloop()