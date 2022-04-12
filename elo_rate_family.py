class elo():
    def __init__(self,eloA,eloB,W,K=32):
        self.eloA = eloA
        self.eloB = eloB
        self.W = W
        self.K = K


    #胜率计算
    def win_rate(self):
        #x=双方elo分差
        x = self.eloA - self.eloB
        print('双方elo分差%d'% x)
        #Px为A胜率
        Px = 1/(1+(10/(x/400))) 
        print('胜率=%d' % Px)
        Px_B = 1 - Px
        print('B胜率=%d' % Px_B)


    def after_elo(self):
        self.Ro = self.eloA
        Rn = self.Ro + self.K * (self.W - self.Px)
        print('比赛后elo分数:%d' % Rn)



if __name__ == '__main__':
    a = elo(1200,10,1)
    a.win_rate()