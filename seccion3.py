#!/usr/local/bin/python2.7

""" seccion2.py: Programa que resuelve el problema presentado en la seccion 2 de la tarea 3 de redes, 2014-1"""

def algoritmo(G,origen):
	d = {}
	p = {}
	for nodo in G:
		d[nodo] = float('Inf')
		p[nodo] = None
	d[origen] = 0

	for i in range(len(G)-1):
		for nodo in G:
			for vecino in G[nodo]:
				if d[vecino] > d[nodo] + G[nodo][vecino]:
					d[vecino] = d[nodo] + G[nodo][vecino]
					p[vecino] = nodo
	return d,p

def main():
	grafo = {
		'a': { 'b': 1, 'g': 4, 'i': 10 },
		'b': { 'a': 1, 'c': 9, 'e': 8 },
		'c': { 'b': 9, 'd': 2},
		'd': { 'c': 2, 'e': 9, 'f': 4, 'i': 2},
		'e': { 'b': 8, 'd': 9, 'f': 2, 'i': 1},
		'f': { 'd': 4, 'e': 2, 'h': 6},
		'g': { 'a': 4, 'h': 7},
		'h': { 'f': 6, 'g': 7}, 	# enlace con i eliminado
		'i': { 'a':10, 'd': 2, 'e': 1} 	# enlace con h eliminado
	}
	distancia = {}
	predecesor = {}

	for nodo in grafo:
		distancia[nodo], predecesor[nodo] = algoritmo(grafo,nodo)

	print ('Via\Distancia', grafo.keys())
	print ('-'*60)
	
	for nodo in grafo:
		print (str(nodo),' |',' '*8,distancia[nodo].values())

	return 0

if __name__ == '__main__': main()
