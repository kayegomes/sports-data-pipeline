import json
import pandas as pd


def transform_matches():

    with open("data/raw/matches.json", encoding="utf-8") as f:
        data = json.load(f)

    matches = data["matches"]

    rows = []

    for match in matches:

        rows.append({
            "date": match["utcDate"],
            "matchday": match["matchday"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_score": match["score"]["fullTime"]["home"],
            "away_score": match["score"]["fullTime"]["away"],
            "winner": match["score"]["winner"],
            "status": match["status"]
        })

    df = pd.DataFrame(rows)

    df["date"] = pd.to_datetime(df["date"])

    df.to_csv("data/processed/matches_clean.csv", index=False)

    print("Transformação concluída")

    return df