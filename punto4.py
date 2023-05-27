import pandas as pd
from sklearn.cluster import KMeans

# Carga los datos del archivo "encuesta.csv" en un objeto DataFrame llamado "data".
data = pd.read_csv('encuesta.csv')

# Crea un nuevo objeto DataFrame llamado "datos2" que contiene todas las columnas de "data" excepto las que se especifican en la lista de columnas a eliminar.
datos2 = data.drop(columns=['Marca temporal', '¿Cuántas mascotas tienes?', '¿Qué tipo de mascotas tienes?', '¿Cuál es la personalidad de tu mascota?', '¿Qué es lo que necesitas saber antes de tener una mascota?', '¿Tienes afiliada a tu mascota a EPS?', '¿Tienes afiliada a tu mascota a la funeraria?', '¿Llevas a tu mascota a la guardería?', '¿Con qué frecuencia llevas a tu mascota a la guardería?', '¿Es fácil para ti dejar a tu mascota en la guardería?', '¿En que rango de valor están los gastos de tu mascota mensualmente?', '¿Tienes alguna persona que te ayude a pagar los gastos de tu mascota?',
                   '¿Cuántas veces al día sacas a tu mascota a dar un paseo?', '¿Cuántas veces al día le das de comer a tu mascota', '¿Cuántas veces por mes le compras comida, juguetes o accesorios a tu mascota?', '¿Cada cuánto bañas a tu mascota?', '¿Tu mascota es obediente?', 'De 1 a 5 ¿Qué tan amorosa es tu mascota?', '¿Qué tanto disfrutas pasear con tu mascota?', '¿De qué color es tu mascota?', 'Tu mascota hace sus necesidades en:', '¿Qué es lo que más te gusta de tu mascota?', 'Del físico de tu mascota ¿Qué es lo que más te gusta?'], inplace=False)

# Renombra las columnas de "datos2" según los nombres especificados en el diccionario de renombramiento.
datos2.rename(columns={
              '¿Te gustan los animales domésticos?': 'Me Gustan', '¿Tienes mascotas?': 'Mascotas'}, inplace=True)

# Establece el número de clústeres que se desean crear en 2.
k = 2
# Crea un objeto KMeans llamado "modelo" con el número de clústeres especificado en "k" y una semilla aleatoria de 7.
modelo = KMeans(n_clusters=k, random_state=7)
# Aplica el algoritmo de clustering KMeans al DataFrame "datos2" y devuelve las etiquetas de clúster para cada fila de datos.
Etiqueta = modelo.fit_predict(datos2)
# Agrega una nueva columna llamada "Cluster" al DataFrame "datos2" que contiene las etiquetas de clúster para cada fila de datos.
datos2['Cluster'] = Etiqueta
# Imprime el DataFrame "datos2" con la columna "Cluster" agregada.
print(datos2)
