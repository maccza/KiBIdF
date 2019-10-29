class LCG:
    def __init__(self,seed):
        self.seed = seed
        self.last_results = self.seed
    def change_seed(self,new_seed):
        self.seed = new_seed
        self.last_results = self.seed
    def lcg(self,par_a,par_c,par_m):
        pseudo_random_number = (par_a*self.last_results+1)%par_m
        self.last_results = pseudo_random_number
        return pseudo_random_number
if __name__ == "__main__":
    lcg = LCG(1000000)
    for i in range(100):
        print(lcg.lcg(345,125,677))