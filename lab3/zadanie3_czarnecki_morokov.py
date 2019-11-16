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


def moooeeeep(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


if __name__ == '__main__':
    out = upload_public_key()
    print(moooeeeep(out))