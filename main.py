from news_fetcher import get_all_news
from sentiment.analyzer import analyze_sentiment
from trading.signal_generator import generate_trade_signal

def main():
    print("📡 Fetching news...")
    all_news = get_all_news()
    
    print("🧠 Analyzing sentiment...")
    positive_news = []
    for news in all_news:
        sentiment = analyze_sentiment(news)
        if sentiment == "positive":
            positive_news.append(news)
    
    print("📈 Generating trading signal...")
    signal = generate_trade_signal(positive_news)
    
    print(f"\n📰 Positive News:\n{positive_news}\n")
    print(f"📊 Trade Signal: {signal}")

if __name__ == "__main__":
    main()
