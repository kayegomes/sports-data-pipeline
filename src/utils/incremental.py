import os

def get_last_run():

    path = "data/metadata/last_run.txt"

    if not os.path.exists(path):
        return None

    with open(path) as f:
        return f.read().strip()


def update_last_run(date):

    with open("data/metadata/last_run.txt", "w") as f:
        f.write(date)