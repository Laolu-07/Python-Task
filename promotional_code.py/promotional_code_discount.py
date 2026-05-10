def get_discounted_price(item , price , promo_code):
    code = promo_code.strip()
    promo = code.upper()
    
    if(promo == "SAVE10"):
        discount = price * 0.1
        new_price = price - discount

    elif(promo == "HALFOFF"):
        discount = price * 0.5
        new_price = price - discount

    else:
        new_price = price
    
    return new_price

