# import csv

# archivo = "./Productos.csv"
# columnas = ["nombreProducto","precio","cantidadMinimaComprar"]
# listaProductos = []
# writer = {}

# def convertirDiccionario():
#     with open(archivo) as csvfile:
#         reader = csv.DictReader(csvfile)  
#         for row in reader:
#             listaProductos.append(row)
        

# def crearCsv():
#     with open(archivo, mode='w') as file:
#         writer = csv.DictWriter(file, delimiter=',', fieldnames=columnas )
#         writer.writeheader()
#         for producto in listaProductos:
#             writer.writerow(producto)
#             print(producto)

# convertirDiccionario()
# crearCsv()
