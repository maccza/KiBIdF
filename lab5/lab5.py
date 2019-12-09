from fastecdsa.curve import Curve
from collections import namedtuple
from fastecdsa import keys
from fastecdsa import curve as c
from xml.dom import minidom
from fastecdsa import encoding as enc

def parseXML(imput_patch):
    eliptic_curve = namedtuple("eliptic_curve",["name","p","a","b","q","gx","gy"])
    
    xmldoc = minidom.parse(imput_patch)
    
    parameterslist = xmldoc.getElementsByTagName('ElipticCurve')
    for parameter in parameterslist:
        name = parameter.getElementsByTagName("name")[0]
        name = str(name.childNodes[0].data)
        p = parameter.getElementsByTagName('p')[0]
        p = int(p.childNodes[0].data)
        a = parameter.getElementsByTagName('a')[0]
        a = int(a.childNodes[0].data)
        b = parameter.getElementsByTagName('b')[0]
        b = int(b.childNodes[0].data)
        q = parameter.getElementsByTagName('q')[0]
        q = int(q.childNodes[0].data)
        gx = parameter.getElementsByTagName('gx')[0]
        gx = int(gx.childNodes[0].data)
        gy = parameter.getElementsByTagName('gy')[0]
        gy = int(gy.childNodes[0].data)
        
    return eliptic_curve(name,p,a,b,q,gx,gy)

def create_curve(parameters):
    curve = Curve(parameters.name,
                    parametres.p,
                    parameters.a,
                    parameters.b,
                    parameters.q,
                    parameters.gx,
                    parametres.gy)
    return curve
def generate_keys(curve):
    ecdsa_keys = namedtuple("ecdsa_keys",["public_key","private_key"])
    priv_key,pub_key = keys.gen_keypair(curve)

    return ecdsa_keys(pub_key,priv_key)
if __name__ == "__main__":
    parametres = parseXML("parameters.xml")
    curve = create_curve(parametres)
    keys = generate_keys(curve)