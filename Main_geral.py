import tkinter as tk
import acao
import Saidas_Exibicao
import Entradas_Tkinker
import organizacao_layout

main = tk.Tk()
main.title("MAIN")
main.geometry("300x300")        
main.config(bg="#f2f2f2")

intro = tk.Label(main, text="BEM VINDO!!! \n COMANDOS DE APRENDIZAGEM", font="Arial,16,Bold").grid(row=0, column=0, columnspan=3, padx=10, pady=10)


btn_entradas = tk.Button(main, text="ENTRADAS", command=Entradas_Tkinker.entradas).grid(row= 2, column= 0,padx=10, pady=10)

btn_saidas = tk.Button(main, text=" SAIDAS ", command=Saidas_Exibicao.saidas).grid(row= 2, column= 1,padx=10, pady=10)

btn_ACAO = tk.Button(main, text="  AÇÕES  ", command=acao.acao).grid(row= 2, column= 2,padx=10, pady=10)

btn_LAYOUT = tk.Button(main, text="  LAYOUT  \n SIMPLES", command=organizacao_layout.organizacao2).grid(row= 3, column= 0,padx=10, pady=10)

btn_LAYOUT = tk.Button(main, text="  LAYOUT  \n NIVEL 2", command=organizacao_layout.organizacao1).grid(row= 3, column= 1,padx=10, pady=10)


foot = tk.Label(main, text=" PRODUZIDO POR: \n HEXA \n SOLUÇÕES EMPRESARIAIS ", font="Arial,25").grid(row=6, column=0, columnspan=3, padx=10, pady=10)
main.mainloop()
