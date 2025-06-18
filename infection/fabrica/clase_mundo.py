import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
cmap=ListedColormap(['white', 'gray', 'red'])

class Mundo:
    
    def __init__(self, n_filas, n_columnas):

        self.numero_columnas = n_columnas
        self.numero_filas = n_filas

        self.mapa = np.zeros((n_filas, n_columnas), dtype=int)

        self.ocupacion = 0.0
        self.numero_personas = 0
        self.ocupacion_infectada = 0.0
        self.numero_personas_infectadas = 0

    def ocupacion_inicial(self, ocupacion):

        numero_celdas_ocupadas = ocupacion * self.numero_columnas * self.numero_filas
        numero_celdas_ocupadas = int(numero_celdas_ocupadas)

        aux_lista = []
        for ii in range(self.numero_filas):
            for jj in range(self.numero_columnas):
                aux_lista.append([ii,jj])

        np.random.shuffle(aux_lista)

        for kk in range(numero_celdas_ocupadas):
            ii=aux_lista[kk][0]
            jj=aux_lista[kk][1]
            self.mapa[ii,jj]=1

        self.ocupacion = ocupacion
        self.numero_personas = numero_celdas_ocupadas

        pass

    def infecto_paciente_cero(self):

        aux = (self.mapa==2)
        if aux.sum()>0:
            ya_infectados = np.argwhere(aux)
            if len(ya_infectados)>0:
                for ii,jj in ya_infectados:
                    self.mapa[ii,jj]=1

        posibles_pacientes_cero=[]

        for ii in range(self.mapa.shape[0]):
            for jj in range(self.mapa.shape[1]):
                if self.mapa[ii,jj]==1:
                    posibles_pacientes_cero.append([ii,jj])

        nn = np.random.randint(0, len(posibles_pacientes_cero))

        paciente_cero=posibles_pacientes_cero[nn]

        ii, jj = paciente_cero

        self.mapa[ii,jj]=2

        self.numero_personas_infectadas = 1
        self.ocupacion_infectada = self.numero_personas_infectadas/self.numero_personas


        pass

    def veo_mapa(self):

        plt.imshow(self.mapa, origin='lower', cmap=cmap)
        return plt.show()

    def propago_infeccion(self):

        lista_nuevos_infectados = np.argwhere(self.mapa==2).tolist()

        aux_list = []

        while len(lista_nuevos_infectados)>0:
        
            for infectado in lista_nuevos_infectados:
        
                vecinos = []
        
                for incremento in [[1,1], [1,0], [1,-1],
                                   [0,1], [0,-1],
                                   [-1,1], [-1,0], [-1,-1]]:
                    posible_vecino = np.array(infectado)+np.array(incremento)
                    ii = posible_vecino[0]
                    jj = posible_vecino[1]
                    if ii>=0 and ii<self.numero_filas:
                        if jj>=0 and jj<self.numero_columnas:
                            if self.mapa[ii, jj]==1:
                                self.mapa[ii, jj]=2
                                aux_list.append([int(ii),int(jj)])
        
            lista_nuevos_infectados = aux_list
            aux_list = []
        
        self.numero_personas_infectadas = (self.mapa == 2).sum()
        self.ocupacion_infectada = self.numero_personas_infectadas/self.numero_personas


        pass


