import pandas as pd
# importamos el algoritmo kMeans para realizar clustering
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score  # métrica de silhouette
import matplotlib.pyplot as plt  # librería para graficar

datos = pd.read_csv('/content/drive/MyDrive/Mall_Customers.csv')
print(datos)

datos2 = datos.drop(columns=['CustomerID', 'Gender'], inplace=False)
print(datos2)

datos2.rename(columns={
              'Age': 'Edad', 'Annual Income (k$)': 'Ingresos Anuales [miles US$]', 'Spending Score (1-100)': 'Calificación gastos [1-100]'}, inplace=True)
print(datos2)

# Vamos a realizar un ensayo de agrupamiento usando el algoritmo k-Means. La elección del número de grupos (clusters) la realiza el usuario. El número de cluster deseado es k = 2

k = 2  # defino el número de clusters
modelo = KMeans(n_clusters=k, random_state=7)  # configurar el algoritmo kMeans
Etiqueta = modelo.fit_predict(datos2)
datos2['Cluster'] = Etiqueta
print(datos2)
# ---
centroides = pd.DataFrame(modelo.cluster_centers_)
print(centroides)
# ---
grupo0 = datos2[datos2['Cluster'] == 0]
grupo1 = datos2[datos2['Cluster'] == 1]

print(grupo0)
print(grupo1)
# ---
datos2.drop(columns=['Cluster'], inplace=True)
Nc = range(2, 25)
Elbow = []  # creamos una lista vacía para guardar el score del Elbow
score_silhouette = []  # creamos una lista vacía para guardar el score del Silhouette

for contador in Nc:
    modelo = KMeans(n_clusters=contador, random_state=7)
    Elbow.append(modelo.fit(datos2).score(datos2))  # calcula el elbow
    etiqueta = modelo.fit_predict(datos2)
    score_silhouette.append(silhouette_score(datos2, etiqueta))
plt.plot(Nc, Elbow, marker='*', color='red')
plt.title('Elbow')
plt.xlabel('Número de clusters')
plt.grid()  # poner cuadricula
plt.show()
plt.plot(Nc, score_silhouette, marker='*', color='pink')
plt.title('Score silhouette')
plt.xlabel('Número de clusters')
plt.show()

k = 6  # defino el número de clusters
modelo = KMeans(n_clusters=k, random_state=7)  # configurar el algoritmo kMeans
Etiqueta = modelo.fit_predict(datos2)
datos2['Cluster'] = Etiqueta
print(datos2)
# ---
grupo0 = datos2[datos2['Cluster'] == 0]
grupo1 = datos2[datos2['Cluster'] == 1]
grupo2 = datos2[datos2['Cluster'] == 2]
grupo3 = datos2[datos2['Cluster'] == 3]
grupo4 = datos2[datos2['Cluster'] == 4]
grupo5 = datos2[datos2['Cluster'] == 5]
# ---
centroides = pd.DataFrame(modelo.cluster_centers_)
centroides.rename(columns={
                  0: 'Edad', 1: 'Ingresos Anuales [miles US$]', 2: 'Calificación gastos [1-100]'}, inplace=True)
print(centroides)

# Parte 2: Inclusión variable categórica sexo para la construcción de los cluster

datos2.drop(columns=['Cluster'], inplace=True)
datos2['Sexo'] = datos['Gender']
a = datos['Gender'] == 'Male'
b = datos['Gender'] == 'Female'
datos2.Sexo[a] = '1'
datos2.Sexo[b] = '2'
print(datos2)

# ---

datos2['Sexo'] = datos2.Sexo.astype('int64')
datos2.info()
print(datos2)

# Realizar una segmentación por clusters usando el algoritmo k-Means. El número de grupos o segmentos debe ser elegido considerando la métrica del Elbow y del Silloutte. Adicionalmente, realice un analisis de cada uno de los grupos obtenidos realizando una descripción del mismo con base en los centroides modelo.cluster_centers.

k = 6  # defino el número de clusters
modelo = KMeans(n_clusters=k, random_state=7)  # configurar el algoritmo kMeans
Etiqueta = modelo.fit_predict(datos2)
datos2['Cluster'] = Etiqueta
print(datos2)

# ---
grupo0 = datos2[datos2['Cluster'] == 0]
grupo1 = datos2[datos2['Cluster'] == 1]
grupo2 = datos2[datos2['Cluster'] == 2]
grupo3 = datos2[datos2['Cluster'] == 3]
grupo4 = datos2[datos2['Cluster'] == 4]
grupo5 = datos2[datos2['Cluster'] == 5]
# ---
centroides = pd.DataFrame(modelo.cluster_centers_)
centroides.rename(columns={
                  0: 'Edad', 1: 'Ingresos Anuales [miles US$]', 2: 'Calificación gastos [1-100]', 3: 'Sexo'}, inplace=True)
print(centroides)
