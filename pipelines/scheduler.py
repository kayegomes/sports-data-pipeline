import time
from run_pipeline import run

while True:

    print("Executando pipeline...")

    run()

    print("Aguardando próxima execução...")

    time.sleep(3600)