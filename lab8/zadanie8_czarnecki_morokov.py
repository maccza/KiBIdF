from scapy.sendrecv import sniff
import hexdump

def sniff_random_value(name_file):
    s = sniff(offline=name_file)

    cisco = 0
    win = 0
    unix = 0
    android_or_ios = 0
    lumia = 0

    for i in range(len(s)):
        packet = bytes(s[i])
        mm = hexdump.dump(packet).split(' ')
        if mm[12]+mm[13] == '0800':
            if mm[23] == '11' or mm[23] == '06':
                if int(mm[22], 16) == 255:
                    cisco += 1
                elif int(mm[22], 16) == 128 or int(mm[22], 16) == 120:
                    win += 1
                elif int(mm[22], 16) == 64 or int(mm[22], 16) == 63:
                    unix += 1
                elif int(mm[22], 16) == 65:
                    android_or_ios += 1
                elif int(mm[22], 16) == 130:
                    lumia +=1

    print(f'\nCalkowita liczba pakietow: {len(s)}')
    print(f'Liczba zidentyfikowanych OS: {cisco+win+unix+android_or_ios+lumia}')
    print(f'\nCisco: {cisco}. \nWindows: {win}. \nUnix: {unix}. \nAndroid/iOS: {android_or_ios}. \nLumia: {lumia}.')


if __name__ == "__main__":
    sniff_random_value(name_file='ruch_sieciowy.pcapng')