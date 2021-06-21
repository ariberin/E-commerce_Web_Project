class Carrito:

    def __init__(self, request):

        self.request = request
        self.session = request.session
        
        carrito = self.session.get("carrito")

        if not carrito:
            carrito = self.session['carrito'] = {}
        #else:

        self.carrito = carrito
    
    def agregar(self, producto):

        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.titulo,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for k, v in self.carrito.items():
                if k == str(producto.id):
                    v["cantidad"] += 1
                    v["precio"] = float(v["precio"])+producto.precio
                    break
        
        self.guardar()

    def guardar(self):

        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):

        producto.id = str(producto.id)

        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar()
    
    def restar(self, producto):

        for k, v in self.carrito.items():
            if k == str(producto.id):
                v["cantidad"] -= 1
                v["precio"] = float(v["precio"])-producto.precio
                if v["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar()
    
    def limpiar(self):

        self.session["carrito"] = {}
        self.session.modified = True
