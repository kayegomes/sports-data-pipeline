import requests
import json

API_KEY = "0957b7eb83904fcf899098f9bc4a0854"

headers = {
    "X-Auth-Token": API_KEY
}

url = "https://api.football-data.org/v4/competitions/PL/matches"


def extract_matches():

    response = requests.get(url, headers=headers)

    data = response.json()

    with open("data/raw/matches.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Dados extraídos com sucesso")