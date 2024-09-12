class Processo:
    def __init__(self, nome, tempo_chegada, tempo_execucao):
        self.nome = nome
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.tempo_espera = 0
        self.tempo_termino = 0
        self.tempo_turnaround = 0
        self.tempo_resposta = None
