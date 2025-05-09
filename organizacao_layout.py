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
    

def grids():
    root = tk.Tk()
    root.title("ORGANIZAÇÃO")
    root.geometry("500x800")
    root.config(bg="#f2f2f2")
     # Grid()    
    grid_lbl = tk.Label(root, text="GRID", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descGrid = tk.Label(root, text='''.grid(  )
    # Organiza os widgets em uma grade
    # EXEMPLO: ORGANIZAR OS WIDGETS EM UMA GRADE''').pack()
    grid_frame = tk.Frame(root, bg="lightgreen", width=200, height=60)
    grid_frame.pack(row=10, column=0, padx=10, pady=10)
    grid_frame2 = tk.Frame(root, bg="lightyellow", width=200, height=60)
    grid_frame2.pack(row=10, column=1, padx=10, pady=10)
    grid_frame3 = tk.Frame(root, bg="lightpink", width=200, height=60)
    grid_frame3.pack(row=11, column=0, padx=10, pady=10)
    grid_frame4 = tk.Frame(root, bg="lightgray", width=200, height=60)
    grid_frame4.pack(row=11, column=1, padx=10, pady=10)


def place():

    root = tk.Tk()
    root.title("ORGANIZAÇÃO")
    root.geometry("500x800")
    root.config(bg="#f2f2f2")

    # Place()
    place_lbl = tk.Label(root, text="PLACE", font="Arial,16,Bold").pack(padx=200, anchor="w")   
    descPlace = tk.Label(root, text='''.place(  )
    # Organiza os widgets em posições absolutas
    # EXEMPLO: ORGANIZAR OS WIDGETS EM POSIÇÕES ABSOLUTAS''').pack()

    label = tk.Label(root, text="PLACE", font="Arial,16,Bold").pack(padx=200, anchor="w")

    
    place_frame = tk.Frame(root, bg="lightblue", width=200, height=60)
    place_frame.place(x=50, y=50)   
    place_frame2 = tk.Frame(root, bg="lightgreen", width=200, height=60)
    place_frame2.place(x=50, y=150) 
    place_frame3 = tk.Frame(root, bg="lightyellow", width=200, height=60)
    place_frame3.place(x=50, y=250)
    place_frame4 = tk.Frame(root, bg="lightpink", width=200, height=60)
    place_frame4.place(x=50, y=350)
    place_frame5 = tk.Frame(root, bg="lightgray", width=200, height=60)
    place_frame5.place(x=50, y=450)
    place_frame6 = tk.Frame(root, bg="lightblue", width=200, height=60)
    place_frame6.place(x=50, y=550)
    place_frame7 = tk.Frame(root, bg="lightgreen", width=200, height=60)
    place_frame7.place(x=50, y=650)
    place_frame8 = tk.Frame(root, bg="lightyellow", width=200, height=60)
    place_frame8.place(x=50, y=750)


def organizacao2():

    root = tk.Tk()
    root.title("ORGANIZAÇÃO SIMPLES")
    root.geometry("500x800")
    root.config(bg="#f2f2f2")
  
    # Pack()
    pack_lbl = tk.Label(root, text="PACK", font="Arial,16,Bold").pack(padx=200, anchor="w")
    descPack = tk.Label(root, text='''.pack(  )
    # Organiza os widgets em relação ao seu pai
    # EXEMPLO: ORGANIZAR OS WIDGETS EM RELAÇÃO AO SEU PAI''').pack()
    pack_frame = tk.Frame(root, bg="lightblue", width=200, height=60)   
    pack_frame.pack(padx=10, pady=10)


    btn_grig = tk.Button(root, text="GRID", command=grids).pack(padx=10, pady=10)

    btn_place = tk.Button(root, text="PLACE", command=place).pack(padx=10, pady=10)

   



    










