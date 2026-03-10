def run_data_checks(df):

    print("\nRunning data quality checks...")

    if df.empty:
        raise ValueError("Dataset vazio!")

    if df["home_team"].isnull().sum() > 0:
        raise ValueError("Home team com valores nulos")

    if df["away_team"].isnull().sum() > 0:
        raise ValueError("Away team com valores nulos")

    if df["home_score"].isnull().sum() > 0:
        print("Aviso: jogos ainda não finalizados")

    print("Data quality checks passaram!")