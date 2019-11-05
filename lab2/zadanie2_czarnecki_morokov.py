import random
class LCG:
    def __init__(self,seed):
        self.seed = seed
        self.last_results = self.seed
    def change_seed(self,new_seed):
        self.seed = new_seed
        self.last_results = self.seed
    def lcg(self,par_a,par_m):
        pseudo_random_number = (par_a*self.last_results+1)%par_m
        self.last_results = pseudo_random_number
        return pseudo_random_number
if __name__ == "__main__":
    seed = random.getrandbits(4096)
    lcg = LCG(seed)
    mod_gen = random.getrandbits(4096)
    file_to_save = open("krypto.txt","w+")
    for i in range(10):
        file_to_save.write(str(lcg.lcg(345,mod_gen)))
        file_to_save.write("\n")
    file_to_save.close()
        