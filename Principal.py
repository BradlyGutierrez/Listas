
from cmath import exp
from Clases import Producto as prod, ListaProd as lst
listaProd = lst()
def menu():
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Buscar por código")
    print("5. Mostrar registros")
    print("6. Buscar por nombre")
    print("7. Buscar por precio")
    print("8. Salir")
    op = int(input("Escriba su opcion: "))
    return op


def agregarProducto():
    print("Agregar Datos del producto")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    desc = input("Descripción: ")
    precio = input("Precio: ")
    existencia = int(input(("Existencia: ")))
    existenciaMinima = int(input("ExistenciaMinima : "))

    producto = prod(codigo,nombre,desc, precio,existencia,existenciaMinima)
    listaProd.agregarElem(producto);


def modificarRegistro():
    print("Editar Producto")
    cod = input("Codigo: ")
    prodct, pos = listaProd.buscarCodigo(cod)
    print(f"""Nombre Actual: {prodct.nombre}
precio actual: {prodct.precio}
Descripcion: {prodct.descp}
Existe: {prodct.exist}
Existencia Minima: {prodct.existMinima}""")
    print("Nuevos Datos")
    newNombre = input("Nombre: ")
    newDesc = input("Descripción: ")
    newPrecio = input("Precio: ")
    newExistencia = input(("Existencia: "))
    newExistenciaMinima = int(input("ExistenciaMinima : "))

    newProd=prod(newNombre,newDesc, newPrecio,newExistencia,newExistenciaMinima)
    lst.editarElelmento(newProd,pos);

def eliminarRegistro():
    print("Eliminar registro")
    cod = input("Codigo: ")
    prdct, pos = listaProd.buscarCodigo(cod)
    print(f"""Realmente desea Eliminar el registro {prdct}""")
    resp = input("SI-NO")
    if resp.upper() == "SI":
        listaProd.eliminarElemento(prdct)
    else:
        print("Operación cancelada")

def buscarPorCod():
    print("Buscar Producto")
    cod = input("Código: ")
    try:
        producto, pos = listaProd.buscarCodigo(cod)
 
        if producto.codigo != None:
            print(producto)
    except Exception as ex:
        print("Error al buscar código", str(ex))
        
        
        

def buscarPorNombre():
    print("Buscar registro")
    nombre = input("Nombre: ")
    try: 
        est, pos = listaProd.buscarPorNombre(nombre)
        if est.nom != None:
            print(est)
    except Exception as ex: 
        print(str(ex))
    

def buscarPorPrecio():
    print("Buscar registro")
    precio = input("Precio: ")
    try: 
        prdct, pos = listaProd.buscarPorPrecio(precio)
        if prdct.price != None:
            print(prdct)
    except Exception as ex: 
        print(str(ex))



def mostrarRegistros():
    try:
        for prod in listaProd.lista: 
            if prod.exist < prod.existeMinima:
                print("="*30)
                print(prod)
                print("="*30)
    except Exception as ex: 
        print("Error", str(ex))

def main():
    op = 0;
    while(op != 10):
        op = menu()
        if op == 1: agregarProducto()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: buscarPorCod()
        elif op == 5: mostrarRegistros()
        elif op == 6: buscarPorNombre()
        elif op == 7: buscarPorPrecio()
        elif op == 8: print("Ciao, ciao")
        else: print("Opcion no valida")

main()