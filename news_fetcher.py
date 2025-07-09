from GoogleNews import GoogleNews

def get_google_news():
    googlenews = GoogleNews(lang='en', period='1d')
    googlenews.search("cryptocurrency OR bitcoin OR ethereum")
    result = googlenews.result()
    
    headlines = []
    for r in result[:10]:
        headlines.append(f"Google: {r['title']}")
    return headlines
