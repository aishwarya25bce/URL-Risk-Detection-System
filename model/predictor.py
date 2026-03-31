# model/predictor.py

import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict(features: dict) -> dict:
    """
    Predict using trained model
    """
    feature_list = [
    features.get("url_length", 0),
    features.get("num_dots", 0),
    features.get("num_hyphens", 0),
    features.get("has_https", 0),
    features.get("has_at", 0),
    features.get("digit_count", 0),
    features.get("has_keyword", 0),
    features.get("domain_length", 0),
    features.get("subdomain_count", 0),
    features.get("ip_flag", 0),
]
    

    prediction = model.predict([feature_list])[0]

    return {
        "prediction": int(prediction)
    }