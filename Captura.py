from scapy.all import sniff
import matplotlib.pyplot as plt
from Pachet import Pachet
from scapy.layers.inet import IP, UDP, TCP, Ether
import json

class Captura:
    _instance = None
    pachete = []

    @staticmethod
    def getInstance():
        if Captura._instance == None:
            Captura()
        return Captura._instance

    def __init__(self):
        if Captura._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Captura._instance = self

    def efectuare_captura(self, text):
        if text == "tcp":
            self.pachete = sniff(count=50, filter="tcp",prn=lambda x: x.summary())
        elif text == "udp":
            self.pachete = sniff(count=50, filter="udp", prn=lambda x: x.summary())
        else:
            self.pachete = sniff(count=50, prn=lambda x: x.summary())

    def numara_udp(self):
        udp = "UDP"
        nr_udp = 0

        for pachet in self.pachete:
            if pachet.haslayer(UDP):
                nr_udp = nr_udp + 1

        return nr_udp

    def numara_tcp(self):
        tcp = "TCP"
        nr_tcp = 0

        for pachet in self.pachete:
            if pachet.haslayer(TCP):
                nr_tcp = nr_tcp + 1

        return nr_tcp

    def determina_tcp_udp(self):

        lista_tcp_udp = []
        for pachet in self.pachete:
            if pachet.haslayer(UDP) or pachet.haslayer(TCP):
                lista_tcp_udp.append(pachet)

        return lista_tcp_udp

    def salveaza_json(self, fisier):

        lista_tcp_udp = self.determina_tcp_udp()
        sir_pentru_json = ""
        for pachet in lista_tcp_udp:
            if pachet.haslayer(TCP):
                p = Pachet(pachet[Ether].dst,
                           pachet[Ether].src,
                           pachet[IP].dst,
                           pachet[IP].src,
                           pachet[IP].version,
                           pachet[IP].proto,
                           pachet[TCP].sport,
                           pachet[TCP].dport,
                           None,
                           None
                           )
                sir_pentru_json = sir_pentru_json + " " + p.__str__()
            elif pachet.haslayer(UDP):
                p = Pachet(pachet[Ether].dst,
                           pachet[Ether].src,
                           pachet[IP].dst,
                           pachet[IP].src,
                           pachet[IP].version,
                           pachet[IP].proto,
                           pachet[TCP].sport,
                           pachet[TCP].dport,
                           None,
                           None
                           )
                sir_pentru_json = sir_pentru_json + " " + p.__str__()

        with open(fisier, "w") as f:
            json.dump(sir_pentru_json, f)


###TESTARE ##
#
# captura = Captura()
# captura.efectuare_captura(None)
# # l = captura.determina_tcp_udp()
# # for pachet in l:
# #     print(pachet.show())
# #
# # if l[0].haslayer(UDP):
# #     p = Pachet(l[0][Ether].dst, None, None, None, None, None,
# #                None, None, None, None)
# #
# # print(p.__str__())
# captura.salveaza_json()