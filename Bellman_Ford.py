from texttable import Texttable

class Topologia:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, n_nodo):
        nodo = Nodo(n_nodo)
        self.nodos[n_nodo] = nodo

    def obtener_nodo(self, n_nodo):
        return self.nodos[n_nodo]

    def agregar_arista(self, ori_nodo, lle_nodo, peso=1):
        self.nodos[ori_nodo].agregar_nodo_ady(self.nodos[lle_nodo], peso)

    def __len__(self):
        return len(self.nodos)

    def __iter__(self):
        return iter(self.nodos.values())

    def arista_existe(self, ori_nodo, lle_nodo):
        return self.nodos[ori_nodo].es_adyacente(self.nodos[lle_nodo])

class Nodo:
    def __init__(self, n_nodo):
        self.n_nodo = n_nodo
        self.nodo_ady = {}

    def obtener_nodo(self):
        return self.n_nodo

    def agregar_nodo_ady(self, lle_nodo, peso):
        self.nodo_ady[lle_nodo] = peso

    def obtener_nodos_ady(self):
        return self.nodo_ady.keys()

    def obtener_peso(self, lle_nodo):
        return self.nodo_ady[lle_nodo]

    def es_adyacente(self, dest):
        return dest in self.nodo_ady

def bellman_ford(topologia, nodo_ori):
    distancia = dict.fromkeys(topologia, float('inf'))
    distancia[nodo_ori] = 0

    for _ in range(len(topologia) - 1):
        for nodo in topologia:
            for nod_adya in nodo.obtener_nodos_ady():
                distancia[nod_adya] = min(distancia[nod_adya], distancia[nodo] + nodo.obtener_peso(nod_adya))

    return distancia

def crearGrafo():
    g = Topologia()
    while True:
        usuario_input = input('Acciones: insertar nodo/insertar arista/bellman-Ford/mostrar/terminar: ').split()  #Acciones aceptados por el programa

        proceso = usuario_input[0].lower()
        if proceso == "insertar":  # este proceso sirve para agregar nodos o aristas
            subproceso = usuario_input[1]
            if subproceso == 'nodo':  # este subproceso sirve para agregar nodos
                key = int(usuario_input[2])
                if key not in g:
                    g.agregar_nodo(key)
                else:
                    print('Vertice propuesto ya existe.')
            elif subproceso == 'arista':  # este subproceso sirve para agregar aristas
                src = int(usuario_input[2])
                dest = int(usuario_input[3])
                weight = int(usuario_input[4])
                if src not in g.nodos:
                    print('El nodo {} no se encontro en la topología'.format(src))
                elif dest not in g.nodos:
                    print('El nodo {} no se encontro en la topología'.format(dest))
                else:
                    if not g.arista_existe(src, dest):
                        g.agregar_arista(src, dest, weight)
                    else:
                        print('Arista propuesta ya existe.')

        elif proceso == 'bellman-ford':  # este proceso sirve para el claculo del algoritmo de Bellman Ford, indicando los nodos
            key = int(usuario_input[1])
            nodo_ori = g.obtener_nodo(key)
            distancia = bellman_ford(g, nodo_ori)

            nodos = []
            for nodo in distancia:
                nodos.append((nodo.obtener_nodo(), distancia[nodo]))
            nodos = sorted(nodos, key=lambda tup: tup[0])

            t = Texttable()
            fila = ["Nodo"]
            fila2 = ["Distancia"]
            for nodo in nodos:
                fila.append(nodo[0])
                fila2.append(nodo[1])
            t.add_row(fila)
            t.add_row(fila2)
            print(t.draw())

        elif proceso == "mostrar":  # este proceso muestra todos los nodos y aristas ingresados en el grafo
            print('Nodos: ')
            for v in g:
                print(v.obtener_nodo())  #Imprime los nodos que se colocaron con la función Insertar nodo
            print()

            print('Aristas: ')
            for v in g:
                for dest in v.obtener_nodos_ady():
                    w = v.obtener_peso(dest)
                    print('(src={}, dest={}, peso={}) '.format(v.obtener_nodo(),
                                                               dest.obtener_nodo(), w))
            print()  #Imprime los nodos que se colocaron con la función Insertar arista

        elif proceso == 'terminar':  # este proceso termina el programa
            break

def main():
    crearGrafo()

if __name__ == "__main__": main()