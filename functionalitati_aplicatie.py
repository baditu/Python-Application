from Captura import Captura

captura = Captura()
def button_click():
        captura.efectuare_captura(None)

def evaluare_entry(entry):
        try:
                if entry.get() == "tcp" or entry.get() == "udp":
                        captura.efectuare_captura(entry.get())
        except:
                if entry.get() != "tcp" or entry.get() != "udp":
                        entry.insert(0, "Eroare!")

def entry_pentru_fisier(entry_fisier):
        captura.salveaza_json(entry_fisier.get())