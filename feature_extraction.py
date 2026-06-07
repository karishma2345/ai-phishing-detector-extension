import re

def extract_features(url):
    features = []

    # 1. Length of URL
    features.append(len(url))

    # 2. HTTPS check
    features.append(1 if "https" in url else 0)

    # 3. Count dots
    features.append(url.count("."))

    # 4. Suspicious keywords
    suspicious_words = ["login", "verify", "bank", "secure", "account", "update", "free"]
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    return features