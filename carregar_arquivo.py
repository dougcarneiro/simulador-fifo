import os

from processo import Processo


def carregar_processos(arquivo):
    processos = []
    if not os.path.exists(arquivo):
        print(f"O arquivo {arquivo} não existe.")
        return processos

    with open(arquivo, "r") as f:
        next(f)
        for linha in f:
            try:
                nome, tempo_chegada, tempo_execucao = linha.strip().split(",")
                processos.append(
                    Processo(nome, int(tempo_chegada), int(tempo_execucao))
                )
            except Exception:
                pass
    return processos
