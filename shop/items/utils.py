def get_cart_total_price(session_cart):
    total = 0
    for item in session_cart.values():
        total += float(item['price']) * int(item['quantity'])
    return total
