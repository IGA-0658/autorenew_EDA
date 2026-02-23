#Tratamiento de datos
import pandas as pd
import numpy as np

#Visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns

# ----- Función para realizar un análisis rápido de un DataFrame -----

def analisis_rapido(df, n=5):

    """
    Función que proporciona un análisis rápido de un DataFrame.
    Parámetros:
    df: DataFrame a analizar.
    n: Número de filas (por defecto = 5)
    
    """

    print(f"Las {n} primeras columnas son:")
    display(df.head(n))
    print("Información básica del DataFrame:")
    display(df.info())
  
    print(f"El número de duplicados es: {df.duplicated().sum()}")
    display(df.isna().mean().round(4) * 100)


# ----- Función para realizar un análisis exploratorio de datos (EDA) rápido -----

def eda(df, n=2):
  num_cols = df.select_dtypes(include='number').columns
  cat_cols = df.select_dtypes(include=['object', 'category']).columns

  print("Variables numéricas:\n\n", num_cols)
  print("\nColumnas categóricas:\n\n", cat_cols)

  print("Veamos las estadísticas básicas:\n")

  display(df.describe().T.round(n))
  display(df.describe(include=['category', 'object']).T.round(n))

  for col in cat_cols:
    print(f" \n----------- Estamos analizando la columna: '{col}' -----------\n")
    print(f"Valores únicos: {df[col].unique()}\n")
    print("Frecuencias de los valores únicos de las categorías:")
    display(df[col].value_counts())

# ----- Función para visualizar las variables categóricas -----

    print("Countplots de las columnas categóricas:\n")
    for col in cat_cols:

        if df[col].nunique() > 200: #si es mayor no muestro grafico
            print(f"La columna {col} tiene demasiadas categorías: {df[col].nunique()}\n\n")
            continue

        num_categories = df[col] . nunique()
        width = max(7, num_categories * 0.5)
        height = 3

        plt. figure(figsize=(width, height))
        sns. countplot (x=df[col], order=df [col].value_counts ( ) . index)

        plt. title(f'Grafico de barras de {col}')
        plt.xlabel(col)
        plt. ylabel('Frecuencia')
        plt.xticks(rotation=90)

        plt. show()
        
    print("Histogramas:\n")
    for col in num_cols:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[col], bins=30, edgecolor='black')

        plt. title(f'Distribucion de {col}')
        plt.xlabel(col)
        plt. ylabel('Frecuencia')

        plt.show()

    print("Vamos con los boxplots:\n")
    for col in num_cols:
        plt.figure(figsize=(10, 1))
        sns . boxplot (x=df [col] )

        plt.xlabel(col)
        plt. ylabel('Frecuencia')
        plt.title(f'Distribucion de {col}')

        plt. show()


# ----- Función para visualizar la matriz de correlación -----

def matriz_correlacion(df):

    # Calcular la matriz de correlación
    corr_matrix = df.corr(numeric_only=True)

    # Crear la figura
    #plt.figure(figsize=(3, 3))
    plt.figure(figsize=corr_matrix.shape)
    # Crear una máscara para mostrar solo la parte triangular
    mask = np. triu(np.ones_like(corr_matrix, dtype=bool))
    # Graficar el mapa de calor
    sns. heatmap(corr_matrix,
    annot=True,
    vmin =- 1,
    vmax=1,
    mask=mask,
    cmap='cool')

    plt. show()