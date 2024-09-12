import time


def fifo(processos, pular_espera):
    tempo_atual = 0
    total_espera = 0
    total_turnaround = 0
    total_resposta = 0
    print("\nExecução dos Processos:")

    for processo in processos:
        if tempo_atual < processo.tempo_chegada:
            tempo_atual = processo.tempo_chegada

        if not processo.tempo_resposta:
            processo.tempo_resposta = tempo_atual - processo.tempo_chegada
            total_resposta += processo.tempo_resposta

        processo.tempo_espera = tempo_atual - processo.tempo_chegada
        processo.tempo_termino = tempo_atual + processo.tempo_execucao
        processo.tempo_turnaround = processo.tempo_termino - processo.tempo_chegada

        total_espera += processo.tempo_espera
        total_turnaround += processo.tempo_turnaround

        print(f"Processo {processo.nome}:")
        print(f"    Tempo de Chegada: {processo.tempo_chegada}")
        print(f"    Tempo de Execução: {processo.tempo_execucao}")
        print(f"    Tempo de Espera: {processo.tempo_espera}")
        print(f"    Tempo de Resposta: {processo.tempo_resposta}")
        print(f"    Executando...")

        for i in range(1, processo.tempo_execucao + 1):
            if not pular_espera:
                time.sleep(1)
            print(f"    {i}/{processo.tempo_execucao}")

        print(f"    Tempo de Término: {processo.tempo_termino}")
        print(f"    Tempo de Turnaround: {processo.tempo_turnaround}\n")

        tempo_atual = processo.tempo_termino

    media_espera = total_espera / len(processos)
    media_turnaround = total_turnaround / len(processos)
    media_resposta = total_resposta / len(processos)

    return processos, media_espera, media_turnaround, media_resposta


def exibir_resultados(processos, media_espera, media_turnaround, media_resposta):
    print("\nResumo da Execução:")
    print(
        f"{'Processo':<10} {'Tempo Execução':<15} {'Tempo Espera':<12} {'Turnaround':<12} {'Tempo Resposta':<14}"
    )
    for processo in processos:
        print(
            f"{processo.nome:<10} {processo.tempo_execucao:<15} {processo.tempo_espera:<12} {processo.tempo_turnaround:<12} {processo.tempo_resposta:<14}"
        )

    print(f"\nTempo Médio de Espera: {media_espera:.2f}")
    print(f"Tempo Médio de Turnaround: {media_turnaround:.2f}")
    print(f"Tempo Médio de Resposta: {media_resposta:.2f}")


def main(processos, pular_espera=False):
    if processos:
        processos.sort(key=lambda p: p.tempo_chegada)
        processos_executados, media_espera, media_turnaround, media_resposta = fifo(
            processos, pular_espera
        )
        exibir_resultados(
            processos_executados, media_espera, media_turnaround, media_resposta
        )
