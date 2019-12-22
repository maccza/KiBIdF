import scapy
from scapy.sendrecv import sniff
import codecs

if __name__ == "__main__":
    s = sniff(count=2, filter='tcp')
    wyn = str(s[0])
    print(wyn)
    print(len(wyn.split('\\x')))
    #wyn = wyn.split('\\n')
    #print(wyn.split('\\x'))
    #print(codecs.encode(bytes(s[1]), encoding='HEX'))
    # TODO: 1. Separacja split("\\x")
    # TODO: 2. Sprawdzic w Wareshark na ktorym elemencie: Typ protokolu TCP/IP etc
    # Todo: gdzie wystepuje seq number, nr portu