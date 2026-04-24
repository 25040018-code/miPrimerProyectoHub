
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(total):
    if total > 1000:
        return total * 0.10
    return 0

def mostrar_resumen(nombres, subtotales, total, descuento):
    print("\n--- Resumen de compra ---")
    for i in range(len(nombres)):
        print(f"Producto: {nombres[i]} | Subtotal: ${subtotales[i]:.2f}")
    
    print("-" * 30)
    print(f"Total general: ${total:.2f}")
    print(f"Descuento aplicado: -${descuento:.2f}")
    print(f"Total a pagar: ${total - descuento:.2f}")

# --- Programa Principal ---
nombres = []
subtotales = []
total_general = 0
continuar = 's'

print("--- Sistema de Ventas (Python Modular) ---")

while continuar.lower() == 's':
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    # Llamada a función
    subtotal = calcular_subtotal(precio, cantidad)
    
    nombres.append(nombre)
    subtotales.append(subtotal)
    total_general += subtotal
    
    continuar = input("¿Desea agregar otro producto? (s/n): ")

# Cálculos finales
descuento = calcular_descuento(total_general)

# Mostrar resultados
mostrar_resumen(nombres, subtotales, total_general, descuento)