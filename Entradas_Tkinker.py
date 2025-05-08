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


#sSpin
# Area de texto multilinha, útil para comentarios ou textos longos
#EXEMPLO: DIGITE UMA MENSAGEM LONGA:
msg_text_lbl = tk.Label(root, text="TEXT").pack(padx=5, pady=5)
msg_text = tk.Text(root, height=5, width=30)
msg_text.pack(padx=10, pady=10)




root.mainloop()