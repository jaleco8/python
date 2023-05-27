import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("encuesta.csv")

marca_temporal = pd.DataFrame(datos, columns=["Marca temporal"])
te_gustan_los_animales_domesticos = pd.DataFrame(datos, columns=["¿Te gustan los animales domésticos?"])
tienes_mascotas = pd.DataFrame(datos, columns=["¿Tienes mascotas?"])
tipos_mascotas = pd.DataFrame(datos, columns=["¿Qué tipo de mascotas tienes?"])
personalidad_mascotas = pd.DataFrame(datos, columns=["¿Cuál es la personalidad de tu mascota?"])
necesidades_mascotas = pd.DataFrame(datos, columns=["¿Qué es lo que necesitas saber antes de tener una mascota?"])
EPS_mascotas = pd.DataFrame(datos, columns=["¿Tienes afiliada a tu mascota a EPS?"])
funeraria_mascotas = pd.DataFrame(datos, columns=["¿Tienes afiliada a tu mascota a la funeraria?"])
guarderia_mascotas = pd.DataFrame(datos, columns=["¿Llevas a tu mascota a la guardería?"])
frecuencia_guarderia_mascotas = pd.DataFrame(datos, columns=["¿Con qué frecuencia llevas a tu mascota a la guardería?"])
facilidad_guarderia_mascotas = pd.DataFrame(datos, columns=["¿Es fácil para ti dejar a tu mascota en la guardería?"])
gastos_mensuales_mascotas = pd.DataFrame(datos, columns=["¿En que rango de valor están los gastos de tu mascota mensualmente?"])
ayuda_gastos_mascotas = pd.DataFrame(datos, columns=["¿Tienes alguna persona que te ayude a pagar los gastos de tu mascota?"])
paseo_mascotas = pd.DataFrame(datos, columns=["¿Cuántas veces al día sacas a tu mascota a dar un paseo?"])
comidas_mascotas = pd.DataFrame(datos, columns=["¿Cuántas veces al día le das de comer a tu mascota"])
compras_mascotas = pd.DataFrame(datos, columns=["¿Cuántas veces por mes le compras comida, juguetes o accesorios a tu mascota?"])
baño_mascotas = pd.DataFrame(datos, columns=["¿Cada cuánto bañas a tu mascota?"])
obediente_mascotas = pd.DataFrame(datos, columns=["¿Tu mascota es obediente?"])
amorosa_mascotas = pd.DataFrame(datos, columns=["De 1 a 5 ¿Qué tan amorosa es tu mascota?"])
disfrutar_paseo_mascotas = pd.DataFrame(datos, columns=["¿Qué tanto disfrutas pasear con tu mascota?"])
color_mascotas = pd.DataFrame(datos, columns=["¿De qué color es tu mascota?"])
necesidades_mascotas = pd.DataFrame(datos, columns=["Tu mascota hace sus necesidades en:"])
aspecto_favorito_mascotas = pd.DataFrame(datos, columns=["¿Qué es lo que más te gusta de tu mascota?"])
aspecto_fisico_favorito_mascotas = pd.DataFrame(datos, columns=["Del físico de tu mascota ¿Qué es lo que más te gusta?"])

perros = np.count_nonzero(tipos_mascotas == 'perro')
gatos = np.count_nonzero(tipos_mascotas == 'gato')
numero_animales = [gatos, perros]

tipo_animales = ["gatos", "perros"]
plt.bar(tipo_animales, numero_animales, color= ["pink", "purple", "k", "g"])
plt.title ("Mascotas mas comunes")
plt.xlabel ("Tipo de mascota")
plt.ylabel ("Cantidad")
plt.show()

# Parse datos del numero de veces que se el da comida
una_vez = np.count_nonzero(comidas_mascotas == '1')
dos_vez = np.count_nonzero(comidas_mascotas == '2')
tres_vez = np.count_nonzero(comidas_mascotas == '3')
cuatro_vez = np.count_nonzero(comidas_mascotas == '4')
cinco_vez = np.count_nonzero(comidas_mascotas == '5')
array_se_le_da_comida = [una_vez, dos_vez,tres_vez, cuatro_vez, cinco_vez]

# Pase datos del numero de veces que se le compra comida
compra_una_ves = np.count_nonzero(compras_mascotas == 1.0)
compra_dos_ves = np.count_nonzero(compras_mascotas == 2.0)
compra_tres_ves = np.count_nonzero(compras_mascotas == 3.0)
compra_cuatro_ves = np.count_nonzero(compras_mascotas == 4.0)
compra_cinco_ves = np.count_nonzero(compras_mascotas == 5.0)
array_compra_comida = [compra_una_ves, compra_dos_ves, compra_tres_ves, compra_cuatro_ves, compra_cinco_ves]

plt.scatter(array_se_le_da_comida, array_compra_comida)
plt.show()

# 
rango_1 = np.count_nonzero(gastos_mensuales_mascotas == "de $0 a $50.000")
rango_2 = np.count_nonzero(gastos_mensuales_mascotas == "de $50.000 a $200.000")
rango_3 = np.count_nonzero(gastos_mensuales_mascotas == "de $200.000 a $500.000")
rango_4 = np.count_nonzero(gastos_mensuales_mascotas == "más de $500.000")
array_rangos = [rango_1, rango_2, rango_3, rango_4]

rangos = ["De $0 a $50.000", "De $50.000 a $200.000", "De $200.000 a $500.000", "Más de $500.000"]

plt.pie(array_rangos, labels = rangos)
plt.show() 

# Vamos a crear dos listas de datos para generar un grafico
amoroso = np.count_nonzero(personalidad_mascotas == "Amoroso")
juguetón = np.count_nonzero(personalidad_mascotas == "Juguetón")
tierno = np.count_nonzero(personalidad_mascotas == "Tierno")
perezoso = np.count_nonzero(personalidad_mascotas == "perezoso")
gruñón = np.count_nonzero(personalidad_mascotas == "gruñón")

array_personalidades = [amoroso, juguetón, tierno, perezoso, gruñón]
personalidades = ["Amoroso", "Jugueton", "Tierno", "Perezoso", "Gruñon"]


#@title Vamos a crear dos listas de datos para generar un grafico
plt.barh(personalidades, array_personalidades, color= ["blue", "black", "red", "green"])
plt.title("Personalidades de las mascotas") #plt.title sirve para poner titulo al grafico
plt.ylabel("Tipo de personalidad")
plt.xlabel("Cantidad")
plt.show()
