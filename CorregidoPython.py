
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(total):
    descuento = 0 # Inicialización obligatoria
    if total > 1000:
        descuento = total * 0.10
    return descuento

def mostrar_resumen(productos, total, descuento):
    print("\n--- Resumen de compra ---")
    for nombre, subtotal in productos:
        print(f"Producto: {nombre} | Subtotal: ${subtotal:.2f}")
    
    print("-" * 25)
    print(f"Total: ${total:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"Total a pagar: ${total - descuento:.2f}")

# Programa principal
productos = []
total_general = 0

for i in range(3):
    print(f"\nIngreso de producto {i+1}")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    subtotal = calcular_subtotal(precio, cantidad)
    total_general += subtotal
    productos.append([nombre, subtotal]) # Se corrigió el append

descuento = calcular_descuento(total_general)
mostrar_resumen(productos, total_general, descuento)