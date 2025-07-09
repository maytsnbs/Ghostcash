def generate_trade_signal(positive_news):
    if len(positive_news) >= 5:
        return "LONG 🔼"
    elif len(positive_news) <= 1:
        return "SHORT 🔽"
    else:
        return "NEUTRAL ⏸"
