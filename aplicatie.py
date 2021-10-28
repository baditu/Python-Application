from tkinter import *
from Captura import Captura
from functionalitati_aplicatie import *
from scapy.layers.inet import IP, UDP, TCP, ICMP
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


## FEREASTRA SECUNDARA
class Fereastra_noua(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Statistics")
        self.geometry("200x200")
        label = Label(self, text="Statistics")
        label.pack()
        frameChartsLT = Frame(self)
        frameChartsLT.pack()
        pachete = ["TCP", "UDP"]
        udp = captura.numara_udp()
        tcp = captura.numara_tcp()
        print(tcp, udp)
        slices = [tcp, udp]
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.pie(slices, radius=1, labels=pachete, autopct='%0.2f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

# FACEM FEREASTRA PRINCIPALA
aplicatie_root_window = Tk()
aplicatie_root_window.title("Aplicatie Proiect Python")
aplicatie_root_window.geometry("600x400")
aplicatie_root_window.config(bg="#84dbd2")

# FACEM MENIU BAR-UL

menu_bar = Menu(aplicatie_root_window)
menu_bar.add_command(label="EXIT", command=aplicatie_root_window.quit)

label_introducere = Label(aplicatie_root_window,
                          text="Aplicatie proiect python",
                          bg="black",
                          fg="white",
                          height=2,
                          width=40,
                          font=("Arial", 20))

label_introducere.place(x=0, y=0)

button_captura = Button(aplicatie_root_window,
                        command=button_click,
                        text="CAPTURA",
                        font=("Arial", 18),
                        bg="#a81919",
                        fg="black",
                        width=20,
                        height=1
                        )

button_captura.place(x=0, y=100)

label = Label(aplicatie_root_window,
              text="Filtru",
              bg="black",
              fg="white",
              font=("Arial", 17),
              height=1
              )
label.place(x=0, y=200)

entry = Entry(aplicatie_root_window,
              bg="black",
              fg="white",
              font=("Arial", 19)
              )
entry.place(x=56, y=200)

button_captura_filtru = Button(aplicatie_root_window,
                         command=lambda: evaluare_entry(entry),
                         text="OK",
                         font=("Arial", 18),
                         bg="#a81919",
                         fg="black",
                         width=10,
                         height=1
                         )
button_captura_filtru.place(x=341, y=200)

show_statistics = Button(aplicatie_root_window,
                         text="Show Statistics",
                         font=("Arial", 18),
                         bg="white",
                         fg="black",
                         )

show_statistics.bind("<Button>", lambda e: Fereastra_noua(aplicatie_root_window))

show_statistics.place(x=0, y=350)

entry_for_path = Entry(aplicatie_root_window,
                       bg="black",
                       fg="white",
                       font=("Arial",19)
                       )
entry_for_path.place(x=0, y=290)

button_save_json = Button(aplicatie_root_window,
                          command=lambda: entry_pentru_fisier(entry_for_path),
                          text="Save as JSON",
                          font=("Arial", 18),
                          bg="white",
                          fg="black"
                          )
button_save_json.place(x=0, y=250)

aplicatie_root_window.config(menu=menu_bar)
aplicatie_root_window.mainloop()

