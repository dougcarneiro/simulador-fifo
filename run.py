import argparse

from main import main
from carregar_arquivo import carregar_processos


DEFAULT_FILE_PATH = "./processos.csv"

parser = argparse.ArgumentParser(
    prog="simulador-fifo",
    description=("Simulação do algoritimo de escalonamento de processos FIFO"),
    add_help=True,
)
parser.add_argument("--file", "-f")
parser.add_argument(
    "--skip", "-s", action=argparse.BooleanOptionalAction, default=False
)

args = parser.parse_args()

processos = carregar_processos(DEFAULT_FILE_PATH if not args.file else args.file)

if __name__ == "__main__":
    try:
        main(processos, args.skip)
    except KeyboardInterrupt:
        print("\nTchauzinho... :)")
