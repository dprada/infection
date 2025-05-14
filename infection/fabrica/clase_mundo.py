import numpy as np

class Mundo:
    
    def __init__(self, n_columnas, n_filas):

        self.numero_columnas = n_columnas
        self.numero_filas = n_filas

        self.mapa = np.zeros((n_filas, n_columnas), dtype=int)

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

        pass

    def infecto_paciente_cero(self):

        posibles_pacientes_cero=[]

        for ii in range(self.mapa.shape[0]):
            for jj in range(self.mapa.shape[1]):
                if self.mapa[ii,jj]==1:
                    posibles_pacientes_cero.append([ii,jj])

        nn = np.random.randint(0, len(posibles_pacientes_cero))
        paciente_cero=posibles_pacientes_cero[nn]

        print(paciente_cero)
        self.mapa[paciente_cero]=2

        pass
