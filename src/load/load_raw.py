from google.cloud import bigquery
import pandas as pd
from datetime import datetime, timezone

def load_csv_to_raw():
    csv_path = r"C:\Users\ligomes\Downloads\sports-data-pipeline\data\processed\matches_clean.csv"

    df = pd.read_csv(csv_path)
    df['_ingested_at'] = datetime.now(timezone.utc)

    client = bigquery.Client(project="project-ac917c6a-54c0-486f-937")
    table_id = "project-ac917c6a-54c0-486f-937.raw.matches"

    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print(f"Dados carregados com sucesso em {table_id}")
    print(f"Linhas carregadas: {len(df)}")

if __name__ == "__main__":
    load_csv_to_raw()