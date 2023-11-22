from modules import AG
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros iniciais
precisao = 4
xlinf, xlsup = -3, 12.1
ylinf, ylsup = 4.1, 5.8
Nind = 10
Pmut = .5
Tmax = 1000

# Calculando a Longitude
Lx = AG.longitude(xlinf,xlsup,precisao)
Ly = AG.longitude(ylinf,ylsup,precisao)

# Criando a População Inicial
genX, genY = AG.create_pop(Nind,Lx), AG.create_pop(Nind,Ly)
decX, decY = AG.decode(genX), AG.decode(genY)

fenX, fenY = xlinf + decX*((xlsup-xlinf)/((2**Lx)-1)), ylinf + decY*((ylsup-ylinf)/((2**Ly)-1)) 

fit = AG.fitness(fenX, fenY)
T = 0
Tlist = []

# Ciclo Evolutivo
optimum = [0]
while T <= (Tmax -1):
    # Seleção
    pair = AG.select(fit)
    # Cruzamento e Mutação
    genX, genY = AG.cross(genX, pair, Pmut), AG.cross(genY, pair, Pmut)
    # Avaliar nova Geração
    decX, decY = AG.decode(genX), AG.decode(genY)
    fenX, fenY = xlinf + decX*((xlsup-xlinf)/((2**Lx)-1)), ylinf + decY*((ylsup-ylinf)/((2**Ly)-1)) 

    fit = AG.fitness(fenX, fenY)
    
    T += 1
    Tlist.append(T)
    print('Generation fittest: ',fit.max())
    if fit.max() > max(optimum):
        optimum.append(fit.max())
    else:
        optimum.append(max(optimum))

best_index = np.argmax(fit)
result_X, result_Y = fenX[best_index], fenY[best_index]

print(f'Best results are for X:',result_X,'and Y:',result_Y)
print(f'Resulting in:',max(optimum))

optimum.pop(0)
plt.plot(Tlist, optimum)
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.title('Evolução')
plt.show()




