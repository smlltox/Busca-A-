import time

from Algorithm.Algorithm import Algorithm
from Problem.Jogo8.Estado import Estado
from Tree.Arvore import Arvore


class BFS(Algorithm):
    def __init__(self, estado_inicial: Estado, objetivo: Estado):
        super().__init__("BFS", Arvore(estado_inicial), objetivo)

    def encontrar_solucao(self):
        inicio = time.time()
        analisar = [self.arvore_busca]
        while True:
            # Se lista está vazia, instância não possui solução
            if not analisar:
                break
            # Retira primeiro elemento, simulando uma fila
            arvore = analisar.pop(0)
            self.estados_analisados += 1
            # Verifica se estado analisado é objetivo
            if not self.eh_objetivo(arvore.estado):
                analisar.extend(self.expandir(arvore))
            else:
                self.solucao = arvore.retornar_acoes()
                break
        fim = time.time()
        self.tempo_execucao = fim - inicio
