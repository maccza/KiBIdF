from pynewhope import newhope
from collections import namedtuple

new_hope_private_key = namedtuple("new_hope_private_key",["private_key","public_message"])
new_hope_shared_key = namedtuple("new_hope_shared_key",["shared_key","shared_message"])

def gen_private_key():
    
    private_key, message = newhope.keygen()
    
    _private_key = new_hope_private_key(private_key,message)
    
    return _private_key

def recived_messege(message):

    shared_key, message = newhope.sharedB(message)

    _shared_key_key = new_hope_shared_key(shared_key,message)
    
    return _shared_key_key

def shared_secret(messege,new_hope_private_key):

    shared_secret_key = newhope.sharedA(messege,new_hope_private_key.private_key)

    return shared_secret_key
def verify(shared_key,secred_key):
    if secred_key == shared_key.shared_key:
        print("\nSuccessful key exchange! Keys match.")
    else:
        print("\nError! Keys do not match.")


if __name__ == "__main__":
    t = gen_private_key()
    w=recived_messege(t.public_message)
    o = shared_secret(w.shared_message,t)
    verify(w,o)
