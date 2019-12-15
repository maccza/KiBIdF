from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from xml.dom import minidom

class ElipticCryptogtaphy:
    
    def __init__(self, xml = "settings.xml"):
        super().__init__()
        self.set_settings_xml(xml)
        self.name = self.read_xml_settings()
        self.eliptic_curve = self.set_eliptic_curve
        self._priv_key = None
    
    def read_xml_settings(self):
        xmldoc = minidom.parse(self.xml_settings)
        parameterslist = xmldoc.getElementsByTagName('ElipticCurve')
        name = None
        for parameter in parameterslist:
            name = parameter.getElementsByTagName("name")[0]
            name = str(name.childNodes[0].data)
        return name

    def set_settings_xml(self, xml = "settings.xml"):
        self.xml_settings = xml

    @property
    def set_eliptic_curve(self):
        if self.name in ec._CURVE_TYPES:
            return ec._CURVE_TYPES[self.name]
        else:
            print("Błąd w xml")

    def create_private_kay(self):
        self._priv_key  = ec.generate_private_key(self.eliptic_curve, default_backend())
    
    @property 
    def private_key(self):
        return self._priv_key
    
    @property 
    def public_key(self):
        return self.private_key.public_key()

    @staticmethod
    def signature(eliptic_curve, data):
        if  isinstance(eliptic_curve, ElipticCryptogtaphy):
            private_key = eliptic_curve.private_key
            signature_ = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
            return signature_
        else:
            return None


if __name__ == '__main__':
    t = ElipticCryptogtaphy()
    t.create_private_kay()
    sig_ = ElipticCryptogtaphy.signature(t, b"this is some data I'd like to sign")
    print(t.public_key)
    print(sig_)