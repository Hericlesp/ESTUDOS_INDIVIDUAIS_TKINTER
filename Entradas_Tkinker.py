import tkinter as tk
from tkinter import ttk

# COMANDOS DE ENTRADA

root = tk.Tk() 
root.title("ENTRADAS")
root.geometry("800x800")
root.config(bg="#f2f2f2")


#comando de entrada...
ent_entry_lbl = tk.Label(root, text="ENTRY", font="Arial,16,Bold").pack(padx=200, anchor="w")
descEntry = tk.Label(root, text='''.Entry()
campo de texto de LINHA UNICA..
 EXEMPLO: DIGITE SEU NOME:''').pack()
entrada = tk.Entry(root)
entrada.pack(padx=10)

msg_text_lbl = tk.Label(root, text="TEXT", font="Arial,16,Bold").pack(padx=200, anchor="w")
descText = tk.Label(root, text='''.Text()
Area de texto multilinha, útil para comentarios ou textos longos
EXEMPLO: DIGITE UMA MENSAGEM LONGA:''').pack()
msg_text = tk.Text(root, height=5, width=30)
msg_text.pack(padx=10)

spin_lbl= tk.Label(root, text="SPINBOX", font="Arial,16,Bold").pack(padx=200, pady=5, anchor="w")
descspin= tk.Label(root, text='''.Spinbox(  , from_=0, to=100)
Campo de texto com setas para aumentar ou diminuir o valor
Entrada com SETAS PARA SIMBOLIZAR NUMEROS
EXEMPLO: ESCOLHER IDADE ENTRE 0 E 100''').pack()
spin_text = tk.Spinbox(root, from_=0, to=1000)
spin_text.pack(padx=10)


checkbox_lbl= tk.Label(root, text="CHECKBOX", font="Arial,16,Bold").pack(padx=200, pady=5, anchor="w")
descCheckbox= tk.Label(root, text=''' .CHECKBUTTON(   , text= '' , variable=var)
Caixa de seleçãoque retorna 1 (marcado) ou 0 (desmarcado)
EXEMPLO: ACEITAR TERMOS E CONDIÇÕES''').pack()
var = tk.IntVar() 
check = tk.Checkbutton(root, text= "ACEITAR TERMOS E CONDIÇÕES", variable=var)
check.pack(padx=10)


radiobutton_lbl= tk.Label(root, text="RADIOBUTTON", font="Arial,16,Bold").pack(padx=200, anchor="w")
descRadiobutton= tk.Label(root, text=''' .Radiobutton(   , text= '' , variable=var)
Permite selecionar apenas uma entre varias opçoes
EXEMPLO: Escolher entre masculino e feninino''').pack()
sexo = tk.StringVar()
tk.Radiobutton(root,text='MASCULINO', variable=sexo).pack()
tk.Radiobutton(root, text='FEMININO', variable=sexo).pack()


combobox_lbl= tk.Label(root, text="COMBOBOX", font="Arial,16,Bold").pack(padx=200, anchor="w")
desccombobox= tk.Label(root, text=''' .Combobox(   , value = [ texto, texto, testo])
COMBOBOX (DO TTK)
Menu suspenso para selecionar uma opção entre várias
EXEMPLO: ESCOLHER UMA COR:''').pack()
combo = ttk.Combobox(root, values=["VERDE", "AZUL", "AMARELO", "VERMELHO"])
combo.pack(padx=10)


root.mainloop()