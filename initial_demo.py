"""A small classroom demo using 2025-26 Premier League player summaries."""

from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Change this name to show another player in the recording.
PLAYER = "Enzo Fernández"
FOLDER = Path(__file__).resolve().parent

# 1. Read the shooting data (the first CSV row is a grouping header).
data = pd.read_csv(FOLDER / "shooting.csv", skiprows=1)
print("1. DATA INGESTION")
print("Read", len(data), "players from shooting.csv")

# 2. Keep players with at least five full-match equivalents.
#    A forward is any player whose position includes FW.
data = data[data["90s"] >= 5].copy()
data["forward"] = data["Pos"].str.contains("FW").astype(int)
data["over_2_5"] = (data["Sh/90"] > 2.5).astype(int)

# Save a small, readable table in this same folder.
columns = ["Player", "Squad", "Pos", "Age", "90s", "SoT/90",
           "Sh/90", "forward", "over_2_5"]
data = data[columns]
data.to_csv(FOLDER / "players_for_demo.csv", index=False)
print("\n2. STORAGE AND FEATURES")
print("Saved", len(data), "rows to players_for_demo.csv and uploaded to AWS S3")
print("Inputs: age, playing time (90s), shots on target/90, forward (0/1)")
print("Answer: over_2_5 = 1 when season shots/90 is above 2.5")

# 3. Keep 25% of players aside to check the model.
#    The answer column is NOT given to the model as an input.
inputs = ["Age", "90s", "SoT/90", "forward"]
X_train, X_test, y_train, y_test = train_test_split(
    data[inputs], data["over_2_5"], test_size=0.25,
    random_state=42, stratify=data["over_2_5"]
)
model = DecisionTreeClassifier(max_depth=3, min_samples_leaf=10,
                               random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
always_under = (y_test == 0).mean()
print("\n3. TRAINING AND CHECK")
print("Trained a small decision tree on", len(X_train), "players")
print("Checked it on", len(X_test), "different players")
print(f"Model accuracy: {accuracy:.1%}")
print(f"Always guessing UNDER: {always_under:.1%}")

# 4. Show one example using the player's known season statistics.
selected = data[data["Player"].str.casefold() == PLAYER.casefold()]
if selected.empty:
    print("\nPlayer not found:", PLAYER)
else:
    player = selected.iloc[[0]]
    label = "OVER" if model.predict(player[inputs])[0] == 1 else "UNDER"
    print("\n4. EXAMPLE OUTPUT")
    print("Player:", player.iloc[0]["Player"])
    print("Input values:", player[inputs].iloc[0].to_dict())
    print("Model class:", label, "2.5 season shots per 90")
    print("Recorded season shots/90:", player.iloc[0]["Sh/90"])

print("\nThis is a season-summary demo, NOT a next-match forecast.")
