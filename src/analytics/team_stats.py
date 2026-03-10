import pandas as pd

def team_stats(df):

    home_wins = df[df["winner"] == "HOME_TEAM"].groupby("home_team").size()

    print(home_wins.sort_values(ascending=False).head())