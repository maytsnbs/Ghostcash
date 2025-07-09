def get_google_news():
    googlenews = GoogleNews(lang='en', period='1d')
    googlenews.search("altcoin OR memecoin OR pepe OR shiba OR dogecoin")
    result = googlenews.result()
    
    headlines = []
    for r in result[:10]:
        headlines.append(f"Google: {r['title']}")
    return headlines
