import tkinter as tk
import Saidas_Exibicao
import Entradas_Tkinker
import organizacao_layout

main = tk.Tk()
main.title("MAIN")
main.geometry("500x300")        
main.config(bg="#f2f2f2")

btn_entradas = tk.Button(main, text="ENTRADAS", command=Entradas_Tkinker.entradas).grid(row= 2, column= 0,padx=10, pady=10)

btn_saidas = tk.Button(main, text="SAIDAS", command=Saidas_Exibicao.saidas).grid(row= 2, column= 1,padx=10, pady=10)

btn_ACAO = tk.Button(main, text="AÇÕES").grid(row= 2, column= 2,padx=10, pady=10)

btn_LAYOUT = tk.Button(main, text="LAYOUT \n 001", command=organizacao_layout.organizacao1).grid(row= 3, column= 0,padx=10, pady=10)



main.mainloop()
