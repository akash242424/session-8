def calculate_discount(cart_total, is_vip=False):
    if cart_total < 0:
        raise ValueError("Invalid total")
    
    if cart_total > 100: 
        base_discount = 0.20
    elif cart_total > 50: 
        base_discount = 0.10
    else:
        base_discount = 0.0

    if is_vip:
        base_discount += 0.05 
        
    return min(base_discount, 0.25)