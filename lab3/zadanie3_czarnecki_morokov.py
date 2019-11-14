import socket, ssl
import OpenSSL
from OpenSSL import crypto
import re


hostname = 'www.pw.edu.pl'
port = 443
cert = ssl.get_server_certificate((hostname, port))



#cert is the encrypted certificate int this format -----BEGIN -----END
crtObj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
pubKeyObject = crtObj.get_pubkey()
pubKeyString = crypto.dump_publickey(crypto.FILETYPE_PEM,pubKeyObject)
pubKeyString = str(pubKeyString)
# wynik = re.match(r'-----BEGIN PUBLIC KEY-----\n(.*)==\n-----END PUBLIC KEY-----\n', pubKeyString)
# wynik = re.match(r''(.*)'', pubKeyString)
# print(wynik)
wynik = pubKeyString[0]
print(cert)
print(pubKeyString)