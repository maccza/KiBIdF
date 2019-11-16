import ssl
from OpenSSL import crypto
from xml.dom import minidom

def upload_public_key():
    xmldoc = minidom.parse('zadanie3_domens.xml')
    itemlist = xmldoc.getElementsByTagName('domena')
    text_file = open("klucze_publiczne.txt", "w")
    keys = []
    for domena in itemlist:
        hostname = str(domena.attributes['id'].value)
        print(hostname)
        port = 443
        cert = ssl.get_server_certificate((hostname, port))
        crtObj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        pubKeyObject = crtObj.get_pubkey()
        pubKeyString = crypto.dump_publickey(crypto.FILETYPE_PEM, pubKeyObject)
        pubkey = pubKeyString.decode("utf-8")
        text_file.write(hostname)
        text_file.write("\n")
        text_file.write(pubkey)
        text_file.write("\n")
        keys.append(pubkey)
    text_file.close()
    return keys


def check_the_same(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    out = list(seen_twice)
    return list(seen_twice)


if __name__ == '__main__':
    out = upload_public_key()
    same = check_the_same(out)
    if len(same) == 0:
        print("\nBrak duplikatow wsrod pobranych kluczy.")
    else:
        print("\nTe klucze publiczne sa zduplikowane:\n")
        print(same)