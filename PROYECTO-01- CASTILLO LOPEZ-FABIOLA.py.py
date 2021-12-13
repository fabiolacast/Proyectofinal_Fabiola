Usuario = "Administrador LifeStore"
Contrasena = "LifeStore2020"
Username = input('Ingrese su nombre de usuario: \n > ')
Password = input('Ingrese su contraseña: \n > ')
if Username == Usuario:
    if Password == Contrasena:
        print("Acceso correcto, bienvenido")
    else:
        print("Contraseña incorrecta")     
else:
    print("Usuario no encontrado, intente nuevamente")

while Password not in Contrasena:
  while Username not in Usuario:
      break

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
prod_ventas = []
cantidad_prod= len(lifestore_products)
for id in range (cantidad_prod):
  verdad_id = id + 1
  renglon = [verdad_id,0]
  prod_ventas.append (renglon)

meses = ['/01/', '/02/', '/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']
#for venta in lifestore_sales:
    #fecha_venta = venta[3]
    #if meses[2] in fecha_venta:
        #print(fecha_venta)
    #id_prod = venta[1]
    #prod_ventas[id_prod - 1][1] = prod_ventas[id_prod - 1][1] + 1
#print (prod_ventas)

 # Ventas sin reembolso
ventas = []
for sale in lifestore_sales:
   refund = sale[4]
   if refund == 1:
        continue
   else:
        ventas.append(sale)
# print(ventas)
#for venta in ventas:
    # print(venta)

meses = ['/01/', '/02/', '/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']
    
ventas_por_mes = []
for mes in meses:
    lista_vacia = []
    ventas_por_mes.append(lista_vacia)

for venta in ventas:
    id_venta = venta[0]
    fecha = venta[3]
    contador_de_mes = 0
    for mes in meses:
        if mes in fecha:
            ventas_por_mes[contador_de_mes].append(id_venta)
            continue
        contador_de_mes = contador_de_mes + 1 

# print(ventas_por_mes)


ganancias_mensuales = []
for venta_mensual in ventas_por_mes:
    ganancia_del_mes = 0
    for id_venta in venta_mensual:
        indice_de_venta = id_venta - 1
        info_de_venta = lifestore_sales[indice_de_venta]

        id_prod = info_de_venta[1]
        indice_de_prod = id_prod - 1
        info_del_prod = lifestore_products[indice_de_prod]
        precio_de_prod = info_del_prod[2]
        ganancia_del_mes = ganancia_del_mes + precio_de_prod
    ganancias_mensuales.append(ganancia_del_mes)

#print(ganancias_mensuales)
ganancia_mes = []
for mes, ganancia in enumerate(ganancias_mensuales):
    sublista = [ganancia, mes]
    ganancia_mes.append(sublista)


# lista_prev.sort(reverse=True)
# print('Ahora en orden: ')
# for lista in lista_prev:
#     print(lista)


cantidad_ventas_mensuales = []
for mes, venta_mensual in enumerate(ventas_por_mes):
    cant_ventas_mensuales = len(venta_mensual)
    sublista = [cant_ventas_mensuales, mes]
    cantidad_ventas_mensuales.append(sublista)

# for cant in cantidad_ventas_mensuales:
#     print(cant)

cantidad_ventas_mensuales.sort(reverse=True)

#for par in cantidad_ventas_mensuales:
 #print(par)

prod_reviews = []
for prod in lifestore_products:
    id_prod = prod[0]
    sublista = [id_prod, 0 , 0]
    prod_reviews.append(sublista)
for venta in lifestore_sales:
    id_prod = venta[1]
    review = venta[2]
    
    indice = id_prod - 1
    prod_reviews[indice][1] += review
    prod_reviews[indice][2] += 1
    
for indice, lista in enumerate(prod_reviews):
   suma = lista[1]
   cant = lista[2]
   if cant > 0:
       calf_prom = suma / cant
       prod_reviews[indice][1] = calf_prom

mejores_calificados = []
for lista in prod_reviews:
    sublista = [lista[1], lista[0]]
    mejores_calificados.append(sublista)

mejores_calificados.sort(reverse=True)

mejores_vendidos= []
for lista in prod_reviews:
    sublista = [lista[2], lista[0], lista[1]]
    mejores_vendidos.append(sublista)

mejores_vendidos.sort(reverse=True)

peores_calificados = []
for lista in prod_reviews:
    sublista = [lista[1], lista[0]]
    peores_calificados.append(sublista)

peores_calificados.sort (reverse=False)

menos_vendidos= []
for lista in prod_reviews:
    sublista = [lista[2], lista[0], lista[1]]
    menos_vendidos.append(sublista)

menos_vendidos.sort (reverse=False)
    
menu_principal = int(input( "Menú principal: \n 1- Productos mejor evaluados \n 2- Ventas mensuales \n 3- Productos más vendidos \n 4- Productos peor evaluados \n 5- Ganancias mensuales \n 6- Productos menos vendidos \n 7- Salir"))
if menu_principal == 1:
  print("Mostrando productos mejor evaluados")
  for rev in mejores_calificados [:5]:
        print(rev)
elif menu_principal == 2:
  print("Mostrando Ventas mensuales")
  contador_de_mes = 0
  for venta_mensual in ventas_por_mes:
    print(f'En el mes de {meses[contador_de_mes]} hubo {len(venta_mensual)} ventas')
    contador_de_mes = contador_de_mes + 1    
elif menu_principal == 3:
  print("Mostrando productos más vendidos")
  for vendidos in mejores_vendidos[:5]:
        print(vendidos)
elif menu_principal == 4:
  print ("Mostrando productos peor evaluados")
  for calif in peores_calificados [54:59]:
        print(calif)
elif menu_principal == 5:
  print ("Mostrando Ganancias mensuales")
  for ganancia in ganancia_mes:
    print(ganancia)
elif menu_principal == 6:
  print ("Mostrando productos menos vendidos")
  for menos in menos_vendidos [:5]:
        print(menos)
elif menu_principal == 7:
  print ("Gracias por su visita, vuelva pronto")
else:
  print ("Digite una opción válida")