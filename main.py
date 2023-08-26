from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import scrolledtext
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import rcParams

####PARTE 2
def apertar_botao1():
    print("plotar")




# --- Raiz ---
root = tk.Tk()
root.geometry('1920x1080+0+0')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("MV Odontologia")
root.configure(background='black')
# ------------

####PARTE 3
nb = ttk.Notebook(root, style='TNotebook')
nb.grid(row=0, column=0, sticky='nsew')

tb1 = Frame(nb)
tb2 = Frame(nb)
tb3 = Frame(nb)


nb.add(tb1, text="Home")
nb.add(tb2, text="Quem Somos")
nb.add(tb3, text="Agendar Consulta")




RH = 0.19

fundo = PhotoImage(file=r'odon.png')
background_label = Label(tb1, image=fundo)
background_label.place(x=4, y=4, relwidth=1.6, relheight=0.6)



#tb1 ----------------------------------------------------------
text1 = Label(tb1,
                  text=("+55 41 3244-5500"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="blue", cursor="ibeam")
text1.place(x=1300, y=500)

text1 = Label(tb1,
                  text=("Telefone:"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="black", cursor="ibeam")
text1.place(x=1200, y=500)


text2 = Label(tb1,
                  text=("Dentista e Consultório Odontológico em Curitiba"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="red", cursor="ibeam")
text2.place(x=10, y=26)
#tb 2 -------------------------------------------- quem somos---------------------
text2 = Label(tb2,
                  text=("Quem Somos"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="blue", cursor="ibeam")
text2.place(x=10, y=20)

text2 = Label(tb2,
                  text=(" O sorriso é uma expressão"
                        " tão fundamental da nossa identidade, autoconfiança e bem-estar, e é incrível como os dentes desempenham um papel crucial nisso tudo. Com o passar dos anos, minha admiração por essa áre"
                        "a da saúde só cresceu, e hoje, como alguém que compartilha desse"),
                  bd="1", font=("ARIAL", 7, "bold"), fg="blue", cursor="ibeam")
text2.place(x=5, y=60)


#tb 3 -------------------------------------------- agendamento de consultas-------
text1 = Label(tb3,
                  text=("Escolha um horario melhor para sua consulta:"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="black", cursor="ibeam")
text1.place(x=10, y=20)

text2 = Label(tb3,
                  text=("Escolha uma data melhor para sua consulta:"),
                  bd="0", font=("ARIAL", 15, "bold"), fg="black", cursor="ibeam")
text2.place(x=10, y=80)

caixaautor = StringVar()
caixaautorchosen = ttk.Combobox(tb3, width=15,
                                        textvariable=caixaautor)
caixaautorchosen["values"] = ("Nenhum", "12h", "15h")
caixaautorchosen.place(x=10, y=50, width=290, height=25)
caixaautorchosen.current(0)

caixaautor = StringVar()
caixaautorchosen = ttk.Combobox(tb3, width=15,
                                        textvariable=caixaautor)
caixaautorchosen["values"] = ("Nenhum", "Dia 30", "Dia 2")
caixaautorchosen.place(x=10, y=110, width=290, height=25)
caixaautorchosen.current(0)


botao19 = Button(tb3, text='Concluir', command=apertar_botao1)
botao19.place(x=10, y=150, width=90, height=30)

root.mainloop()
