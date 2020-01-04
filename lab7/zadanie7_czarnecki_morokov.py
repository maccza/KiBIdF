from scapy.sendrecv import sniff
import hexdump

def sniff_random_value(host=None, counts=10):
    s = sniff(count=counts, filter=host)

    out_type_protocol = []
    out_source_port = []
    out_header_checksum = []
    out_sequence_number = []
    out_total_length = []
    out_payload_length = []

    for i in range(counts):
        packet = bytes(s[i])
        mm = hexdump.dump(packet).split(' ')
        if mm[12]+mm[13] == '0800':
            if mm[23] == '11':
                out_type_protocol.append('IPv4, UDP')
                out_payload_length.append(None)
                out_sequence_number.append(None)
                out_header_checksum.append(mm[24]+' '+mm[25])
                out_source_port.append(mm[34]+' '+mm[35])
                out_total_length.append(mm[16]+' '+mm[17])
            elif mm[23] == '06':
                out_type_protocol.append('IPv4, TCP')
                out_payload_length.append(None)
                out_sequence_number.append(mm[38]+' '+mm[39]+' '+mm[40]+' '+mm[41])
                out_header_checksum.append(mm[24] + ' ' + mm[25])
                out_source_port.append(mm[34] + ' ' + mm[35])
                out_total_length.append(mm[16] + ' ' + mm[17])
        else:
            out_type_protocol.append('IPv6')
            out_payload_length.append(mm[18]+' '+mm[19])
            out_sequence_number.append(None)
            out_header_checksum.append(None)
            out_source_port.append(None)
            out_total_length.append(None)

    for j in range(len(out_type_protocol)):
        print(f'\nNumer pakietu: {j}. Zarejestrowano nastepujace losowe wartosci:')
        print(f'1. Typ protokolu: {out_type_protocol[j]}')
        print(f'2. Payload length (only IPv6): {out_payload_length[j]}')
        print(f'3. Sequence number (only TCP): {out_sequence_number[j]}')
        print(f'4. Header checksum: {out_header_checksum[j]}')
        print(f'5. Source port: {out_source_port[j]}')
        print(f'6. Total length: {out_total_length[j]}')


if __name__ == "__main__":
    """
    Przyklad uzycia:
    sniff_random_value(host='host 10.2.11.20', counts=30)
    """
    sniff_random_value(counts=30) # caly ruch w sieci, pierwsze 30 pakietow zlapanych