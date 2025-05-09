import tkinter as tk

def acao():
    # Criação da janela principal
    root = tk.Tk()
    root.title("AÇÕES")
    root.geometry("300x300")
    root.config(bg="#f2f2f2")

    # Título e descrição
    intro = tk.Label(root, text="AÇÕES", font=("Arial", 16, "bold")).pack(padx=10, anchor="w")

    intro_b =tk.Label(root, text='''AÇÕES (widget, command)
    Adiciona uma ação a um widget. 
    Exemplo: adicionar uma ação a um botão.''').pack(anchor="w", padx=10)

    def acao_func():
        print("Ação executada!")
        # Aqui você pode adicionar a lógica que deseja executar quando o botão for pressionado  

    # Botão com ação
    acao_button = tk.Button(root, text="Clique aqui", command=acao_func)
    acao_button.pack(pady=10)


    
    

             