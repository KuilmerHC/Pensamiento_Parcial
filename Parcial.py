# Programa de procesamiento de compras tienda virtual

num_pedidos = int(input("Cuantos pedidos va a ingresar: "))
lista_pedidos = []
p_enviados = 0
p_pendiente = 0
total_ventas = 0
mayor_pedido = 0





for i in range (num_pedidos):
    print(f"Pedido #{i + 1}" )
    nombre = input("Ingrese el nombre de cliente: ")
    valor_total = float(input("Ingrese el valor total del pedido: "))
    estado = input("Ingrese el estado del pedido (pendiente, enviado o cancelado): ")
    pedido = [nombre, valor_total, estado]
    lista_pedidos.append(pedido)    
    
    
print(lista_pedidos)


for i in range (0, num_pedidos):
    if (lista_pedidos[i][2] == "enviado"):
        p_enviados += 1

for i in range (0, num_pedidos):
    if (lista_pedidos[i][2] == "pendiente"):
        p_pendiente += 1
        
porcentaje_pendiete = p_pendiente / num_pedidos
    
for i in range(0, num_pedidos):
    if(lista_pedidos[i][2] == "enviado"):
        total_ventas += lista_pedidos[i][1]
        
for i in range(0, num_pedidos):
    if (lista_pedidos[i][1] > mayor_pedido):
        mayor_pedido = lista_pedidos[i][1]
        cliente_mayor = lista_pedidos[i][0]
              
    
print("-----------------------------------------------------")
print("Resumen de Pedidos")
print(f"Total de pedido procesados: {num_pedidos}.")
print(f"Total de pedidos enviados: {p_enviados}")
print(f"Total de ventas ${total_ventas}")
print(f"El mayor pedido fue de la persona {cliente_mayor}")

if(porcentaje_pendiete > 0,70):
    print("Alerta: muchos pedidos sin procesar")
print("-----------------------------------------------------")




    
    