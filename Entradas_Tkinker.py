import tkinter as tk

# COMANDOS DE ENTRADA

root = tk.Tk() 
root.title("ENTRADAS")
root.geometry("800x800")
root.config(bg="#f2f2f2")


#comando de entrada...
#  Entry 
# (campo de texto de LINHA UNICA..)
#  EXEMPLO: DIGITE SEU NOME:

ent_entry_lbl = tk.Label(root, text="ENTRY").pack(padx=5, pady=5)
entrada = tk.Entry(root)
entrada.pack(padx=10, pady=10)


#Text
# Area de texto multilinha, útil para comentarios ou textos longos
#EXEMPLO: DIGITE UMA MENSAGEM LONGA:
msg_text_lbl = tk.Label(root, text="TEXT").pack(padx=5, pady=5)
msg_text = tk.Text(root, height=5, width=30)
msg_text.pack(padx=10, pady=10)


#Spinbox
#Entrada com SETAS PARA SIMBOLIZAR NUMEROS
#EXEMPLO: ESCOLHER IDADE ENTRE 0 E 100
spin_lbl= tk.Label(root, text="SPINBOX").pack(padx=5, pady=5)
spin_text = tk.Spinbox(root, from_=0, to=1000)
spin_text.pack(padx=10, pady=10)



#Checkbox
# Caixa de seleçãoque retorna 1 (marcado) ou 0 (desmarcado)
#EXEMPLO: ACEITAR TERMOS E CONDIÇÕES
checkbox_lbl= tk.Label(root, text="CHECKBOX").pack(padx=5, pady=5)
var = tk.IntVar() 
check = tk.Checkbutton(root, text= "ACEITAR TERMOS E CONDIÇÕES", variable=var)
check.pack(padx=10, pady=10)


#Radiobutton
# Permite selecionar apenas uma entre varias opçoes
#EXEMPLO: Escolher entre masculino e feninino
sexo = tk.StringVar()
tk.Radiobutton(root,text='MASCULINO', variable=sexo).pack()
tk.Radiobutton(root, text='FEMININO', variable=sexo).pack()






root.mainloop()