class Producto: 
    def __init__(self,cod,nom,desc,price,exist, existMin) :
        self.codigo = cod
        self.nom = nom 
        self.desc = desc
        self.price = price
        self.exist = exist
        self.existeMinima = existMin
    def __str__(self) :
        return f"""Código: {self.codigo}
nombre: {self.nom}
Descripción: {self.desc}
Precio: {self.price}
Existe: {self.exist}
Existencia minima: {self.existeMinima}"""

class ListaProd: 
    def __init__(self): 
        self.lista = []
    def agregarElem(self,dato):
        try:
            self.lista.append(dato)
        except Exception as ex: 
            print("Ocurrió un error inesperado", str(ex))

    def editarElelmento(self, producto,posicion):
        try:
            self.lista[posicion] = producto
        except Exception as ex:
            print("Error al agregar el producto: ", str(ex))

    def eliminarElemento(self, pos):    
        try:
            self.lista.remove(pos)
        except Exception as ex: 
            print("Error al eliminar: ", str(ex))
    
    def buscarCodigo(self,cod):
        try:
            pos = 0
            for prod in self.lista:
                if prod.codigo == cod:
                    print("Producto encontrado...")
                    return prod, pos
                pos+=1
            else:
                print("No se encontró el producto...")        
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))
    
    def buscarPorNombre(self, nombre):
        
        try: 
            pos = 0
            for producto in self.lista:
                if  producto.nom== nombre:
                    print("Producto encontrado")
                    return producto, pos
                pos +=1
            else:
                print("No se encontro el producto")
        except Exception  as ex: 
            print("Error al buscar", str(ex)) 
    
    def buscarPorPrecio(self, precio):
        pos = 0
        try: 
            for producto in self.lista:
                if  producto.price== precio:
                    print("Producto encontrado")
                    return producto, pos
                pos +=1
            else:
                print("No se encontro el producto")
        except Exception  as ex: 
            print("Error al buscar", str(ex)) 
    
