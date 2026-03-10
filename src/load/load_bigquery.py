from google.cloud import bigquery
import pandas as pd

def load_bigquery():

    client = bigquery.Client()

    table_id = "seu-projeto.dataset.matches"

    df = pd.read_csv("data/processed/matches_clean.csv")

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    print("Dados carregados no BigQuery")