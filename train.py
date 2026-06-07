import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from feature_extraction import extract_features

# URL MODEL -------------------
url_df = pd.read_csv("dataset/urls.csv")
X_url = url_df["url"].apply(extract_features).tolist()
y_url = url_df["label"]

url_model = RandomForestClassifier()
url_model.fit(X_url, y_url)

# EMAIL MODEL -------------------
email_df = pd.read_csv("dataset/emails.csv")

vectorizer = CountVectorizer()
X_email = vectorizer.fit_transform(email_df["text"])
y_email = email_df["label"]

email_model = RandomForestClassifier()
email_model.fit(X_email, y_email)

# SAVE MODELS -------------------
with open("model/url_model.pkl", "wb") as f:
    pickle.dump(url_model, f)

with open("model/email_model.pkl", "wb") as f:
    pickle.dump(email_model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ URL + Email models trained!")