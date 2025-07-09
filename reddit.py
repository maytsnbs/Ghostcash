def get_reddit_news():
    feed_url = "https://www.reddit.com/r/CryptoMoonShots/.rss"
    feed = feedparser.parse(feed_url)
    
    headlines = []
    for entry in feed.entries[:10]:
        headlines.append(f"Reddit: {entry.title}")
    return headlines
