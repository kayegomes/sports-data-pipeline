import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extract.extract_matches import extract_matches
from src.transform.transform_matches import transform_matches
from src.transform.dim_teams import create_dim_teams
from src.transform.fact_matches import create_fact_matches
from src.quality.data_checks import run_data_checks
def run():

    print("Iniciando pipeline")

    extract_matches()

    df = transform_matches()
    run_data_checks(df)
    dim_teams = create_dim_teams(df)
    
    fact_matches = create_fact_matches(df,dim_teams)
    
    print(fact_matches.head())
    
    

    print("Pipeline finalizado")


if __name__ == "__main__":
    run()