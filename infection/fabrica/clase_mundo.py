class Mundo:
    
    def __init__(self, n_columnas, n_filas):

        self.numero_columnas = n_columnas
        self.numero_filas = n_filas

        self.mapa = np.zeros((n_filas, n_columnas), dtype=int)

    def ocupacion_inicial(self, ocupacion):

        numero_celdas_ocupadas = ocupacion * self.numero_columnas * self.numero_filas
        numero_celdas_ocupadas = int(numero_celdas_ocupadas)

        contador  = 0

        while contador<numero_celdas_ocupadas:

            ii = np.random.randint(0,self.numero_filas)
            jj = np.random.randint(0,self.numero_columnas)

            if (self.mapa[ii,jj]==0):
                self.mapa[ii,jj]=1
                contador = contador + 1
