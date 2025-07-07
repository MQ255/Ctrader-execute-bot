def place_order(symbol, direction, volume, sl, tp):
    print(f"تنفيذ صفقة {direction} على {symbol} بحجم {volume} لوت، وقف خسارة {sl} نقطة وهدف {tp} نقطة.")
    
    # هنا يتم وضع الكود الفعلي للتنفيذ عبر Spotware Open API
    # حالياً هو تجريبي
    result = {
        "status": "executed",
        "symbol": symbol,
        "direction": direction,
        "volume": volume,
        "sl": sl,
        "tp": tp
    }
    return result
