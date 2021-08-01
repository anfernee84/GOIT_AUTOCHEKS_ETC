DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer): 
    
    if "discount" in customer:
        if customer.get("discount") != 0:
            return price * (1 - customer["discount"])
        elif customer.get("discount") == 0:
            return price
    else:
        return price * (1 - DEFAULT_DISCOUNT) 




print(get_discount_price_customer(4, {"name": "Boris"}))
    
    
        
    
        
    