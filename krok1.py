import pandas as pd
import plotly.express as px

# načítanie CSV bez hlavičky
df = pd.read_csv("steam.csv", header=None, names=["UserID", "Game", "Action", "Hours", "Unknown"])
print("Ukážka dát:")
print(df.head())

# KROK 2 – Úprava dát
df_play = df[df["Action"] == "play"]

top_games = (
    df_play.groupby("Game")["Hours"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 najhranejších hier:")
print(top_games)

# KROK 3 – Vizualizácia grafu
fig = px.bar(
    x=top_games.index,
    y=top_games.values,
    labels={"x": "Názov hry", "y": "Počet hodín"},
    title="Top 10 najhranejších hier na Steame",
)

fig.show()
