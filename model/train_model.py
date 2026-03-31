import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

from core.extractor import extract_features

# Load dataset
data = pd.read_csv("data/dataset.csv")
X = data["url"].apply(lambda u: list(extract_features(u).values())).tolist()
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")