from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    if result["label"] == "POSITIVE" and result["score"] > 0.85:
        return "positive"
    return "neutral"
