import numpy as np
import sys   
sys.setrecursionlimit(1000000)

class Graph_bi_match(object):
    def __init__(self,G,label_x,label_y):
        self.G = G
        self.label_x = label_x
        self.label_y = label_y
        self.match_list = [-1 for _ in range(len(label_y))]

    def match(self,v,current):
        for i in self.G[v]:
            if i == current:continue
            if self.match_list[i] == -1 or self.match(self.match_list[i],i):
                self.match_list[i] = v
                return True
        return False
    
    def hungarian(self):
        num = 0
        for i in range(self.G.__len__()):
            self.match(i,-1)
        
        for i in range(self.match_list.__len__()):
            if self.match_list[i] == -1:
                continue
            print("%s <--match--> %s:" %(self.label_x[self.match_list[i]],self.label_y[i]))
            num = num + 1
        return num

if __name__ == "__main__":
    G={}
    G[0] = [0,1,2]
    G[1] = []
    G[2] = [2]
    G[3] = [2,3]


    label_x = np.array([0,1,2,4])
    label_y = np.array([0,1,2,3,4])

    res = Graph_bi_match(G,label_x,label_y).hungarian()
    print(res)


