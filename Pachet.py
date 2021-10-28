import json

class Pachet:
    def __init__(self,
                 Ethernet_dst,
                 Ethernet_src,
                 IP_dst,
                 IP_src,
                 IP_version,
                 IP_proto,
                 TCP_sport,
                 TCP_dport,
                 UDP_sport,
                 UDP_dport
                 ):
        self.Ethernet_dst = Ethernet_dst
        self.Ethernet_src = Ethernet_src
        self.IP_dst = IP_dst
        self.IP_src = IP_src
        self.IP_version = IP_version
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UDP_sport = UDP_sport
        self.UDP_dport = UDP_dport

    def __str__(self):
        json_string = json.dumps(self.__dict__)
        return json_string


# ## TESTATRE ##
#
# p = Pachet(223, 112, 111, 222, "IPv4", "IP", 229, 134, 666, 777)
# print(p.__str__())
# print(type(p.__str__()))
