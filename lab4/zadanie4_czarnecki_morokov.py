def product(X):
       if len(X) == 0: return 1
       while len(X) > 1:
         X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
       return X[0]
def producttree(X):
       result = [X]
       while len(X) > 1:
         X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
         result.append(X)
       return result
def remaindersusingproducttree(n,T):
       result = [n]
       for t in reversed(T):
         result = [result[floor(i/2)] % t[i] for i in range(len(t))]
       return result
def remainders(n,X):
       return remaindersusingproducttree(n,producttree(X))
     # example:

def batchgcd_simple(X):
       R = remainders(product(X),[n^2 for n in X])
       return [gcd(r/n,n) for r,n in zip(R,X)]
def batchgcd_faster(X):
       prods = producttree(X)
       R = prods.pop()
       while prods:
         X = prods.pop()
         R = [R[floor(i/2)] % X[i]**2 for i in range(len(X))]
       return [gcd(r/n,n) for r,n in zip(R,X)]

def open_file(imput_path):
       public_key = []
       with open(imput_path) as publics_key:
              for i in publics_key:
                     
                     public_key.append(int(i.split("\n")[0],0))
                     # print(type(int(i.split("\n")[0],0)))
       return public_key

keys = open_file('klucze_sparsowane.txt')

print(batchgcd_faster(keys))
