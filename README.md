# Administración main.py
# Aquí te explico línea por línea lo que hace el código:

## 1. Importamos las librerías necesarias para el ejemplo: pandas y LinearRegression de sklearn.linear_model.
```
import pandas as pd
from sklearn.linear_model import LinearRegression
```
## 2. Cargamos los datos de ventas desde un archivo CSV utilizando la función read_csv de Pandas.
```
sales_data = pd.read_csv('sales_data.csv')
```
## 3. Creamos un objeto de modelo de regresión lineal utilizando la clase LinearRegression de sklearn.linear_model.
```
model = LinearRegression()
```
## 4. Creamos un diccionario que mapea cada mes a un valor numérico.
```
month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
```
## 5. Aplicamos el diccionario al mes en la columna 'Month' del conjunto de datos utilizando la función map de Pandas.
```
sales_data['Month'] = sales_data['Month'].map(month_to_num)
```
## 6. Entrenamos el modelo utilizando los valores numéricos del mes y los ingresos.
```
model.fit(sales_data[['Month']], sales_data['Revenue'])
```
## 7. Hacemos una predicción para el mes de diciembre utilizando el modelo entrenado.
```
prediction = model.predict([[12]])
```
## 8. Imprimimos la predicción formateada con dos decimales.
```
print('The predicted revenue for December is $ {:.2f}'.format(prediction[0]))
```

# Finazas finanzas.py

# Este código carga datos históricos de precios de acciones en un dataframe de pandas, lo divide en conjuntos de entrenamiento y prueba, crea un modelo de regresión lineal y lo ajusta al conjunto de entrenamiento. Luego, utiliza el modelo para hacer predicciones sobre el conjunto de prueba y finalmente imprime las predicciones

# Aquí está la explicación línea por línea:

## 1. En estas líneas, se importan las bibliotecas de pandas y scikit-learn. Pandas es una biblioteca de Python que se utiliza para el análisis de datos y la manipulación de datos estructurados, mientras que scikit-learn es una biblioteca de aprendizaje automático que se utiliza para crear modelos de aprendizaje automático.
```
df = pd.read_csv('stock_prices_sample.csv')
```
## 2. Esta línea carga los datos históricos de precios de acciones en un dataframe de pandas llamado df. Los datos se leen desde un archivo CSV llamado stock_prices_sample.csv.
```
train_data = df[:-100]
test_data = df[-100:]
```
## 3. Estas líneas dividen los datos en conjuntos de entrenamiento y prueba. Los últimos 100 registros se utilizan como datos de prueba y el resto se utiliza como datos de entrenamiento.
```
model = LinearRegression()
model.fit(train_data[['OPEN', 'HIGH', 'LOW']], train_data['CLOSE'])
```
## 4. Estas líneas crean un modelo de regresión lineal utilizando la clase LinearRegression de scikit-learn y lo ajustan al conjunto de entrenamiento. El modelo utiliza las columnas 'OPEN', 'HIGH' y 'LOW' como características y la columna 'CLOSE' como la variable objetivo.
```
predictions = model.predict(test_data[['OPEN', 'HIGH', 'LOW']])
```
## 5. sta línea utiliza el modelo entrenado para hacer predicciones sobre el conjunto de prueba. Las predicciones se almacenan en la variable predictions.
```
print(predictions)
```
## 6. Finalmente, esta línea imprime las predicciones de precios de acciones para el conjunto de prueba.
