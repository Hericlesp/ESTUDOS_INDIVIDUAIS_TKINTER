import tkinter as tk




# # comando do scroollbar...

# wind = tk.Tk()
# wind.title("Exemplo com Scrollbar")

# # Título e descrição
# tk.Label(wind, text="SCROLLBAR", font=("Arial", 16, "bold")).pack(padx=10, anchor="w")
# tk.Label(wind, text='''Scrollbar(widget)   
# Adiciona uma barra de rolagem a um widget.
# Exemplo: adicionar uma barra de rolagem a um Frame.''').pack(anchor="w", padx=10)

# # Container principal
# container = tk.Frame(wind)
# container.pack(fill="both", expand=True)

# # Canvas (área rolável)
# canvas = tk.Canvas(container, height=300)
# canvas.pack(side="left", fill="both", expand=True)

# # Scrollbar vertical
# scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Frame interno (conteúdo que será rolado)
# scrollable_frame = tk.Frame(canvas)

# # Adiciona o frame ao canvas
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# # Configurações de rolagem
# canvas.configure(yscrollcommand=scrollbar.set)

# # Atualiza o scrollregion automaticamente com o tamanho do conteúdo
# def on_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))

# scrollable_frame.bind("<Configure>", on_configure)

# # Habilita scroll com a roda do mouse
# def _on_mousewheel(event):
#     canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows e Linux
# canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
# canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down

# # Adiciona conteúdo (exemplo: muitos Labels)
# for i in range(50):
#     tk.Label(scrollable_frame, text=f"Item {i+1}").pack(anchor="w")






# COMANDOS DE ORGANIZAÇÃO
def organizacao1():

    root = tk.Tk()
    root.title("ORGANIZAÇÃO")
    root.geometry("500x800")
    root.config(bg="#f2f2f2")
    # Frame
    frame_lbl = tk.Label(root, text="FRAME", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descFrame = tk.Label(root, text='''.Frame(  )
    # Cria um contêiner para organizar outros widgets
    # EXEMPLO: CRIAR UM FRAME PARA ORGANIZAR OUTROS WIDGETS''').pack()
    frame = tk.Frame(root, bg="lightblue", width=200, height=60)
    frame.pack(padx=10, pady=10)    

    # Canvas
    canvas_lbl = tk.Label(root, text="CANVAS", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descCanvas = tk.Label(root, text='''.Canvas(  )
    # Área de desenho para criar formas, imagens ou gráficos
    # EXEMPLO: CRIAR UM CANVAS PARA DESENHAR''').pack() 
    canvas = tk.Canvas(root, bg="lightgreen", width=200, height=60)
    canvas.pack(padx=10, pady=10)

    # PanedWindow
    panedwindow_lbl = tk.Label(root, text="PANEDWINDOW", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descPanedWindow = tk.Label(root, text='''.PanedWindow(  )
    # Cria uma janela com divisões ajustáveis
    # EXEMPLO: CRIAR UMA JANELA COM DIVISÕES AJUSTÁVEIS''').pack()
    panedwindow = tk.PanedWindow(root, bg="lightyellow", width=200, height=60) 
    panedwindow.pack(padx=10, pady=10)

    # LabelFrame
    labelframe_lbl = tk.Label(root, text="LABEFRAME", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descLabelFrame = tk.Label(root, text='''.LabelFrame(  )
    # Cria um frame com um rótulo
    # EXEMPLO: CRIAR UM FRAME COM UM RÓTULO''').pack()
    labelframe = tk.LabelFrame(root, text="LABEL FRAME", bg="lightpink", width=400, height=50)
    labelframe.pack(padx=10, pady=10)

    # Toplevel
    toplevel_lbl = tk.Label(root, text="TOPLEVEL", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descToplevel = tk.Label(root, text='''.Toplevel(  )
    # Cria uma nova janela independente
    # EXEMPLO: CRIAR UMA NOVA JANELA INDEPENDENTE''').pack()
    def open_toplevel():
        toplevel = tk.Toplevel(root)
        toplevel.title("Toplevel Window")
        toplevel.geometry("400x200")
        toplevel.config(bg="lightgray")
        toplevel_lbl = tk.Label(toplevel, text="Toplevel", font="Arial,16,Bold").pack(padx=10, anchor="w")
        descToplevel = tk.Label(toplevel, text='''.Toplevel(  )
        # Cria uma nova janela independente
        # EXEMPLO: CRIAR UMA NOVA JANELA INDEPENDENTE''').pack()
        toplevel_frame = tk.Frame(toplevel, bg="lightblue", width=200, height=60)  
        toplevel_frame.pack(padx=10, pady=10)
    bnt_toplevel = tk.Button(root, text="OPEN", command=open_toplevel).pack(padx=10, pady=10)

def organizacao2():

    root = tk.Tk()
    root.title("ORGANIZAÇÃO")
    root.geometry("500x800")
    root.config(bg="#f2f2f2")
    # Frame









