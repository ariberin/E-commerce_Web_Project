def importe_total_carrito(request): #registrarlo para que se pueda usar en cualquiera lado

    total = 0
    if 'carrito' in request.session:
        for k, v in request.session['carrito'].items():
            total += (float(v["precio"]))
    
    return {"importe_total_carrito":total}