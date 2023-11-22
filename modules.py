import numpy as np
from numpy.random import randint

class AG:
    def longitude(linf,lsup,precisao):
        # Calcula a Longitude necessária para um indivíduo dado um intervalo e precisão.
        Lind = np.log2(((lsup-linf)*10**precisao))
        Lind = np.ceil(Lind)
        return Lind.astype(int)
    
    def decode(genotipo):
        # Transforma valores binários em números decimais.
        fenotipo = []
        for i in range(len(genotipo)):
            ind = [str(x) for x in genotipo[i]]
            ind = int(''.join(ind),2)
            fenotipo.append(ind)
            
        fenotipo = np.array(fenotipo)
        return fenotipo
    
    def create_pop(Nind, Lind):
        # Cria uma população uniforme com N indivíduos e Longitude (dimensão) L.
        genotipo = np.random.randint(0,2,(Nind,Lind))
        genotipo = np.array(genotipo)
        return genotipo
    
            
    def fitness(fenX, fenY):
        # Calcula a aptidão dos indivíduos quanto à FO.
        fit = 21.5 + fenX*np.sin(4*np.pi*fenX) + fenY*np.sin(20*np.pi*fenY)
        return fit

    def select(fit):
        # Seleciona pares de indivíduos pelo método proporcional.
        prob = fit/sum(fit)
        ind = len(fit)
        pair = np.random.choice(ind,2,p=prob,replace=False)
        return pair

    def cross(genotipo, pair, Pmut):
        # Realiza o cruzamento pontual de um par de indivíduos, com uma probabilidade de mutação.
        cut = np.random.randint(1,len(genotipo[0]),1)

        tail0 = genotipo[pair[1],cut[0]:].copy()
        tail1 = genotipo[pair[0],cut[0]:].copy()

        genotipo[pair[0],cut[0]:] = tail0
        if np.random.binomial(1,p=Pmut) == 1:
            mut = np.random.randint(0,len(genotipo[0]),1)
            if genotipo[pair[0],mut] == 0:
                genotipo[pair[0],mut] = 1
            else:
                genotipo[pair[0],mut] = 0

        genotipo[pair[1],cut[0]:] = tail1
        if np.random.binomial(1,p=Pmut) == 1:
            mut = np.random.randint(0,len(genotipo[0]),1)
            if genotipo[pair[1],mut] == 0:
                genotipo[pair[1],mut] = 1
            else:
                genotipo[pair[1],mut] = 0

        return genotipo



